from __future__ import print_function
import json
import flask
import logging
import traceback
import model_serve as model
from logging.config import dictConfig

# The flask app for serving predictions:
app = flask.Flask(__name__)

config = json.load(open('config.json', 'r', encoding='utf-8'))
dictConfig(config['logger'])


@app.route('/ping', methods=['GET'])
def ping():
    """
    Determine if the container is working and healthy
    :return:
    json response
    """
    return flask.Response(response='service alive', status=200, mimetype='application/json')


@app.route('/invocations', methods=['POST'])
def predict():
    """
    :return:
    prediction of mental condition:
    1: yes
    0: no
    """
    try:
        input_ = flask.request.data
        input_decoded_ = [x for x in input_.decode().split('\n') if x]
        samples = [json.loads(entry) for entry in input_decoded_]
    except Exception as e:
        samples = list()
        app.logger.error(e)
        logging.error(traceback.format_exc())

    logging.info('{} queries received'.format(len(samples)))
    result_list = model.predict_batch(samples)

    result_dump = '\n'.join(map(json.dumps, result_list))
    return flask.Response(result_dump, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='8080', threaded=False)
