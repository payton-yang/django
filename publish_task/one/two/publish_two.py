from my_celery_config.one.two.three.instance.celery_instance_A_two import celery_app

# moduleB的任务发布 使用autodiscover_tasks寻找消费函数
from async_task.moduleB.taskb import sub, _sub

sub.delay(3, 1)
sub.apply_async(args=(100, 10))
celery_app.send_task(name='my_sub', args=(200, 100))
