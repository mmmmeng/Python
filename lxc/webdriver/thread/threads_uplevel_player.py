from time import ctime,sleep
import threading

#创建超级播放器
def super_player(file_,time):
    for i in range(2):
        print('start palying: %s! %s' %(file_,ctime()))
        sleep(time)

#播放的文件与播放时长
lists = {'因为爱情.mp3':3,'阿凡达.mp4':4,'浮夸.mp3':5}

threads = []
files = range(len(lists))

#创建线程
for file_,time in lists.items():
    t = threading.Thread(target=super_player,args=(file_,time))
    threads.append(t)

if __name__ == '__main__':
    #启动线程
    for t in  files:
        threads[t].start()
    for t in files:
        threads[t].join()

    print('end:%s' %ctime())
