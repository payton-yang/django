# celery配置redis作为broker。redis有16个数据库，编号0~15，这里使用第1个。
broker_url = 'redis://127.0.0.1:6379/0'

# 配置rabbitMQ作为broker,可以把result_backend注释掉
# broker_url = 'amqp://guest:guest@localhost:5672//'

# 设置存储结果的后台
result_backend = 'redis://127.0.0.1:6379/0'

# 可接受的内容格式
accept_content = ["json"]
# 任务序列化数据格式
task_serializer = "json"
# 结果序列化数据格式
result_serializer = "json"

# 第一种方式找到消费函数, 添加任务函数所在文件路径
include = ['async_task.moduleA.taska']
