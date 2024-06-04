from flask import request, g
import time
import logging

def log_request(app):

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("AdminRequestLogger")

    @app.before_request
    def before_request_func():
        if request.blueprint == 'admin':
            g.start_time = time.time()
            logger.info(f"Admin Request: {request.method} {request.path}")

    @app.after_request
    def after_request_func(response):
        if request.blueprint == 'admin':
            elapsed_time = time.time() - g.start_time
            logger.info(f"Admin Response: {response.status_code} (took {elapsed_time:.2f}s)")
        return response