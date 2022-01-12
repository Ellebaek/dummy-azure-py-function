import azure.functions as func
from shared_code.custom_utils import say_hello
import logging
import os


def main(req: func.HttpRequest) -> str:
    logging.info('dummy function 01 (HTTP trigger) invoked.')
    user = req.params.get('user')
    # if name is not supplies say hello to default user
    if not user:
        user = os.environ["DEFAULT_USER"]
    return say_hello(user)
