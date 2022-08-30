import json
import time
import logging
import datetime
import traceback
from logging.config import dictConfig
from pipeline_modules import Query
from preprocessing_module import PreprocessingModule
from model_module import MODELModule

preprocess_time = 0
model_time = 0
config = json.load(open('config.json', 'r', encoding='utf-8'))
dictConfig(config['logger'])


def init_modules():
    global preprocessing
    global model

    start_time = time.time()
    logging.info('loading all modules')
    preprocessing = PreprocessingModule()
    model = MODELModule()
    logging.info("loaded all modules: {0:.2f}s".format(time.time() - start_time))


def predict_sample(req):
    global preprocess_time, model_time

    start_time = time.time()
    req = preprocessing.load_request(req).predict()
    end_time = time.time()
    preprocess_time += end_time - start_time

    start_time = time.time()
    req = model.load_request(req).predict()
    end_time = time.time()
    model_time += end_time - start_time

    return req


def predict_batch(queries):
    """
    Function to call product class to create the req object and use predict_sample function to do prediction
    """
    start_time = time.time()
    results = []
    for n, squery in enumerate(queries):
        try:
            req = Query(squery, timestamp=datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))
            req = predict_sample(req)
            results.append(req)
        except Exception as e:
            logging.error(
                'error processing - msg: {}, query: {}'.format(e, squery))
            logging.error(traceback.format_exc())

    logging.info('processed {p:.2%} of queries. time elapsed: {t:.2f} m'.format(
        p=float(len(results))/len(queries), t=(time.time() - start_time) / 60))

    return results


preprocessing, model = None, None

init_modules()
