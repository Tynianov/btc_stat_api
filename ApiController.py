from flask import Flask, Response, request
from flask_caching import Cache
from json import dumps
from BaseService import BaseService

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app)
JSON_MIME_TYPE = 'application/json'
base_servic = BaseService()

@app.route('/get_mined_blocks')
@app.cache.cached(timeout=60)
def get_mined_blocks():
    mined_blocks = base_servic.get_mined_blocks()
    base_servic.db_service.save_log(request.remote_addr, 1,mined_blocks)

    api_response = Response(dumps({"Mined blocks" : mined_blocks}),status=200,mimetype=JSON_MIME_TYPE)
    return api_response

@app.route('/get_av_time')
@app.cache.cached(timeout=60)
def get_av_time():
    av_time = base_servic.get_av_time()
    base_servic.db_service.save_log(request.remote_addr, 2,av_time)

    api_response = Response(dumps({"Average time between blocks" : av_time}),status=200,mimetype=JSON_MIME_TYPE)
    return api_response

@app.route('/get_tx_count')
@app.cache.cached(timeout=60)
def get_tx_count():
    tx_count = base_servic.get_tx_count()
    base_servic.db_service.save_log(request.remote_addr, 3, tx_count)

    api_response = Response(dumps({"Tx count" : tx_count}),status=200,mimetype=JSON_MIME_TYPE)
    return api_response

@app.route('/get_fee_count')
@app.cache.cached(timeout=60)
def get_fee_count():
    fee_count = base_servic.get_fee_count()
    base_servic.db_service.save_log(request.remote_addr, 4, fee_count)

    api_response = Response(dumps({"Fee amount" : fee_count}),status=200,mimetype=JSON_MIME_TYPE)
    return api_response

@app.route('/get_input_count')
@app.cache.cached(timeout=60)
def get_input_couunt():
    input_count = base_servic.get_input_count()
    base_servic.db_service.save_log(request.remote_addr, 5, input_count)

    api_response = Response(dumps({"Input count" : input_count}),status=200,mimetype=JSON_MIME_TYPE)
    return api_response

@app.route('/get_output_count')
@app.cache.cached(timeout=60)
def get_output_count():
    output_count = base_servic.get_output_count()
    base_servic.db_service.save_log(request.remote_addr, 6, output_count)

    api_response = Response(dumps({"Output count" : output_count}),status=200,mimetype=JSON_MIME_TYPE)
    return api_response

if __name__ == '__main__':
    app.run(debug = True)