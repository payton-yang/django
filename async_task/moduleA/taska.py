import time
from my_celery_config.one.two.three.instance.celery_instance_A_one import celery_app


@celery_app.task
def add(x, y):
    time.sleep(3)
    print(f'{x} + {y} = {x + y}')
    time.sleep(3)


@celery_app.task(name='求和')
def _add(x, y):
    time.sleep(3)
    print(f'{x} + {y} = {x + y}')
    time.sleep(3)
