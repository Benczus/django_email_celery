from time import sleep

from celery import shared_task


@shared_task
def sleep_until(duration):
    sleep(duration)
    return
