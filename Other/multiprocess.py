# coding=utf-8
# multiprocessing 是用来管理和调用线程的包
import multiprocessing
import time

# 定义线程中需要执行的方法
def proc1(pipe):
    print("on proc1")
    #print(pipe.recv())
    pipe.send('hello')
    print('proc1 rec:',pipe.recv())

# 定义线程中需要执行的方法
def proc2(pipe):
    print("on proc2")
    print('proc2 rec:',pipe.recv())
    pipe.send('hello,too')

# 主要执行的方法块
if __name__ == '__main__':
    multiprocessing.freeze_support() # 用来保证线程正常运行

    # 获取线程间的通信对象，可以简单理解为，获取一个公共的数据存储区，不同的线程都可以调用里面的数据
    # 返回的pipe是元祖类型，里面包含两个值，为通道的两端 pipe[0]和pipe[1]
    # 获取Pipe对象时，可以接受一个参数duplex，该参数的值默认为True。
    # 当duplex = True，返回的pipe是双向通道，通道的两端均可以读写
    # 当duplex = False，获取到的通道对象为单向通道，pipe[0]只可以接受（读取）数据，pipe[1]只可以发送（写入）数据

    pipe = multiprocessing.Pipe()
    #pipe = multiprocessing.Pipe(duplex=False)
    #print("pipe type is :",type(pipe))
    #print("pipe[0] type is :",type(pipe[0]))
    #print("pipe[1] type is :", type(pipe[1]))

    # multiprocessing.Process 用来开启线程，并返回线程对象，接收两个参数：1.target:方法名；2.args:该方法接收的参数
    p1 = multiprocessing.Process(target=proc1,args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))

    # start()用来启动线程
    p1.start()

    for i in range(5):
        time.sleep(1)
        print("sleep ",i)
    else:
        print("wake up...")

    #print("p1 is alive:", p1.is_alive())
    p2.start()
    # join()用来停止线程
    p1.join()
    #print("p1 is alive:",p1.is_alive())
    p2.join()