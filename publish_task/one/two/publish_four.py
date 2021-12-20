from my_celery_config.one.two.three.instance.celery_instance_A_three import celery_app
from async_task.moduleC.task1.task1 import test_auto_share_celeryapp
from async_task.moduleC.task2.task2 import _test_auto_share_celeryapp

# moduleC下的task1和task2任务发布 使用shared_task寻找消费函数
test_auto_share_celeryapp.delay(5)
test_auto_share_celeryapp.apply_async(args=(5,))

_test_auto_share_celeryapp.delay(10, 20)
_test_auto_share_celeryapp.apply_async(args=(30, 40))

celery_app.send_task('task1', args=(50,))
celery_app.send_task('task2', args=(50, 60))
