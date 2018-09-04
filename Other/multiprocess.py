# coding=utf-8
# multiprocessing 是用来管理和调用线程的包
import multiprocessing

# 定义线程中需要执行的方法
def proc1(pipe):
    pipe.send('hello')
    print('proc1 rec:',pipe.recv())

# 定义线程中需要执行的方法
def proc2(pipe):
    print('proc2 rec:',pipe.recv())
    pipe.send('hello,too')

# 主要执行的方法块
if __name__ == '__main__':
    multiprocessing.freeze_support() # 用来保证线程正常运行

    # 获取线程间的通信对象，可以简单理解为，获取一个公共的数据存储区，不同的线程都可以调用里面的数据
    pipe = multiprocessing.Pipe()

    # multiprocessing.Process 用来开启线程，并返回线程对象，接收两个参数：1.target:方法名；2.args:该方法接收的参数
    # 这里的args接收的是pipe[0],代表是从公共数据存储区取的数据
    p1 = multiprocessing.Process(target=proc1,args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))

    # start()用来启动线程
    p1.start()
    print("p1 is alive:", p1.is_alive())
    p2.start()
    # join()用来停止线程
    p1.join()
    print("p1 is alive:",p1.is_alive())
    p2.join()

    #这就把代码下载下来了 然后我教你怎么用吧现在？恩 比如现在修改代码 我添加了这一行注释 然后 我想提交修改。