import time
from my_celery_config.one.two.three.instance.celery_instance_A_two import celery_app


@celery_app.task
def sub(a, b):
    print(f'{a} - {b} = {a - b}')
    time.sleep(4)


@celery_app.task(name='my_sub')
def _sub(a, b):
    print(f'{a} - {b} = {a - b}')
    time.sleep(4)
