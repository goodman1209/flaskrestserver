import logging
import os
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
from flask import Flask
app = Flask(__name__)

import pypyodbc

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/hello/<username>')
def sayHello(username):
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    app.logger.info('Info')
    return 'Hello, ' + username

if __name__ == "__main__":

    if not os.path.exists('logs/'):
        os.makedirs('logs/')

    #setting for console log level
    logging.basicConfig(level=logging.DEBUG)
    rootLogger = logging.getLogger()
    formatter = logging.Formatter(
        "[%(asctime)s] [%(threadName)-12.12s] [%(levelname)-5.5s] [%(filename)s:%(lineno)d] %(message)s", "%Y-%m-%d %H:%M:%S")
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    rootLogger.addHandler(consoleHandler)
    handler = TimedRotatingFileHandler('logs/test.log', when="d", interval=1, backupCount=10)
    #handler = RotatingFileHandler(LOG_FILENAME, maxBytes=100000, backupCount=10)
    #setting for log file log level
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.run()