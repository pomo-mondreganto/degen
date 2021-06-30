import logging
import sys
from flask import Flask, request, jsonify
from typing import Callable

import models

try:
    from generated import decode

    decode: Callable[[models.DecodeRequest], models.DecodeResponse]
except ImportError:
    print(
        'Could not import "decode" function from the generated module. '
        'Please make sure you\'ve written the decoder correctly',
        file=sys.stderr,
    )
    sys.exit(1)

app = Flask(__name__)


@app.route('/decode', methods=['POST'])
@app.route('/decode/', methods=['POST'])
def decode():
    data = request.json
    req = models.DecodeRequest.parse_obj(data)
    resp = decode(req)
    return jsonify(resp.dict())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
