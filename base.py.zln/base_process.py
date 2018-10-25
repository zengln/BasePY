# -*- coding:utf-8 -*-

'''
 多进程
'''

from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager
import os, time, random, queue, sys

'''
# 创建一个子进程
# 子程序要执行的代码
def run_proc(name):
    print('Run Child process %s (%s)' %(name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end')
'''

'''
# 启动大量子进程--进程池
def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f seconds' % (name, (end-start)))


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done')
    p.close()
    p.join()
    print('All subprocesses done')
'''
'''
# 进程间通信
# 写数据的进程执行代码
def write(q):
    print('Process to write %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue ' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码
def read(q):
    print('Process to read %s ' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue ' % value)

if __name__ == '__main__':
    # 父进程创建 Queue, 并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程 pw, 写入
    pw.start()
    # 启动子进程 pr, 读取
    pr.start()
    # 等待 pw 结束
    pw.join()
    # pr 进程里是死循环, 无法等待其结束, 只能强行终止
    pr.terminate()
'''

'''
# 分布式进程中的 task_master.py
# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从 BaseManager 继承的 QueueManager
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000,设置验证码'abc'
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue
manager.start()
#获得通过网络访问的 Queue 对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务进来
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d' % n)
    task.put(n)

# 从result队列读取结果
print('Try get results')
for i in range(10):
    r = result.get(timeout=10)
    print('Result %s' % r)

# 关闭
manager.shutdown()
print('master.exit')
'''

'''
分布式进程中的 task_worker.py
'''
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue,所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器
server_addr = '127.0.0.1'
print('Connect to server %s' % server_addr)
# 端口和验证码
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接
m.connect()
# 获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' %(n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty')

# 处理结束
print('work exit')