import logging
import json
from logging.config import dictConfig
from pipeline_modules import PipelineModule
from preprocessing_module import PreprocessingModule
import pandas as pd
from pickle import load

config = json.load(open('config.json', 'r', encoding='utf-8'))
dictConfig(config['logger'])
LOCAL_MODEL_FOLDER = 'model/rf_opt.pkl'
logging.info('Using local model from path: {}'.format(LOCAL_MODEL_FOLDER))

class MODELModule(PipelineModule):
    """wrapper for NER module"""

    _model = None

    def __init__(self):
        super().__init__()
        # Load model
        if self._model is None:
            try:
                self._model = load(open(LOCAL_MODEL_FOLDER, 'rb'))
            except Exception as e:
                logging.info(e)
                raise ValueError('Something wrong with model loading')

    def predict(self):
        def predict_map(req):
            # get prediction result
            pred_results = self._model.predict(req.preprocessed_input)
            req.predicted_mental_condition = int(pred_results[0])
            return req
        self.request = predict_map(self.request)
        return self.request.predicted_mental_condition
