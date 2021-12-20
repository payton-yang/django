from my_celery_config.one.two.three.instance.celery_instance_A_three import celery_app

# moduleC的任务发布 使用_task_from_fun寻找消费函数

# multi.delay(5)
# multi.apply_async(args=(5,))
# 这种情况下只能使用send_task 否则会提示AttributeError: 'function' object has no attribute 'delay'
celery_app.send_task('multi', args=(5,))
