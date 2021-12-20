## 目录结构

1. async_task  
   异步任务的文件目录
2. my_celery_config  
   celery配置文件和实例化
3. publish_task  
   发布任务的函数目录

## 实例化celery的2种方式

1. 单独抽取一个文件作为celery的配置文件 
   如: _celery_config.py 和 celery_instance_A.py
2. 用一个类装载celery的配置 
   如: celery_instance_B.py

## 启动celery的2种方式

1. 见celery_instance_A.py

## 三种发布任务方式

1. 见 publish_one.py

## 4种函数注册成celery消费任务的方式

1. app.task装饰器 + include
   请见_celery_config.py、celery_instance_A_one.py、publish_one.py

2. app.task装饰器 + autodiscover_tasks
   请见_celery_config.py、celery_instance_A_two.py、publish_two.py

3. app._task_from_fun 非装饰器方式
   _celery_config.py、celery_instance_A_three.py、publish_three.py

4. @shared_task装饰器
   请见_celery_config.py、celery_instance_A_four.py、publish_four.py

## 参考

https://github.com/Leonder/celery_demo

这个demo很厉害, 看完这个demo才算是真正入门celery
