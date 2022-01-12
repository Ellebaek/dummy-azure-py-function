import azure.functions as func
import logging


def main(req: func.HttpRequest,
         msg: func.Out[func.QueueMessage]) -> str:
    logging.info('dummy function 02 (HTTP trigger) processed a request.')
    message = req.params.get('body')
    msg.set(message)
    return message