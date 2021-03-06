# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
import os,time,unittest


#查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getatime(testreport+"\\"+fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    now = time.strftime("%y=%m-%d %H_%M_%S")
    filename = './bbs/report/'+now +'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title="魅族社区自动化测试报告",
                            description='环境：Windows 7 浏览器：chrome')
    discover  =  unittest.defaultTestLoader.discover('./bbs/test_case',pattern='*sta.py')
    runner.run(discover)
    fp.close()
    file_path = new_report('./bbs/report/')