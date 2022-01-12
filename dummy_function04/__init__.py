import datetime
import logging
import azure.functions as func


def main(timer_var: func.TimerRequest) -> None:
    # utc_timestamp = datetime.datetime.utcnow().replace(
    #    tzinfo=datetime.timezone.utc).isoformat()

    #if timer_var.past_due:
    #    logging.info('dummy function 04 timer is past due!')

    logging.info('dummy function 04 ran (timer trigger) at {0}', datetime.datetime.now())
