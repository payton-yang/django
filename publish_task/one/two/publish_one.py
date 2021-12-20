from async_task.moduleA.taska import add, _add
from my_celery_config.one.two.three.instance.celery_instance_A_one import celery_app

# moduleA的任务发布, 测试include方法寻找消费函数
add.delay(1, 2)  # 第一种发布方式

celery_app.send_task(name='求和', args=(100, 200))  # 第二种发布方式 必须提供一个name

add.apply_async(args=(111, 222))  # 第三种发布方式，这种入参更丰富可以添加任务控制参数。delay只能是函数本身的参数。
_add.apply_async(args=(110, 119))
