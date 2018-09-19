'''
功能新增：用字典替换集合


'''
from datetime import datetime


def is_leap_year(year):
    '''判断year是否为闰年，是，返回true，否返回false'''

    is_leap = False

    if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):  #可以用if else语句用两个return，但是这样的程序会不够优雅
        return True

    return is_leap

def main():

    #根据用户输入的字符串转化为日期格式的数据
    input_date_str = input('请输入日期(yyyy-mm-dd)：')
    input_date = datetime.strptime(input_date_str,'%Y-%m-%d')


    #获得年月日
    year = input_date.year
    month = input_date.month
    day = input_date.day

    days_sum = day
    """
    # 月和每月的天数用字典表示
    month_days_dict = {1:31,
                       2:28,
                       3:31,
                       4:30,
                       5:31,
                       6:30,
                       7:31,
                       8:31,
                       9:30,
                       10:31,
                       11:30,
                       12:31}


    for i in range(1,month):
        days_sum += month_days_dict[i]

    """
    #每月的天数和月的字典表示
    day_month_dict = {31:{1,3,5,7,8,10,12},
                      30:{4,6,9,10},
                      28:{2}} #这个应该是最原始的


    for i in range(1,month):

        dicts = day_month_dict.items() #[(31, {1, 3, 5, 7, 8, 10, 12}), (30, {9, 10, 4, 6}), (28, 2)]

        for key,value in dicts: #字典和集合都是无序的，不能用索引的方式来取值
            if i in value:
                days_sum += key

    if is_leap_year(year) and month>2:
        days_sum +=1

    print('您输入的日期{}是当年的第{}天'.format(input_date_str,days_sum))


if __name__ == '__main__':
    main()

    '''
    ymb：
        首选按照我们刚才的思路，我们要计算所有月分加起来的天数，就需要知道每个月份有多少天对吧嗯嗯
         # month这个是月份数 为了计算所有月份天数，我们肯定要一个一个的加 所以我们只要循环一下就可以了，循环月份
          #range(1,10) 这个里面，可以写一个区间对不对 只要收尾都是数字就行 这样是1-10对吧不对1-9 10是不循环的哦？嗯那就不用减1了
        #假如month=3 range(1,3) 其实就是 1 2 对吧 没有三嗯 嗯 那就对了 我们只需要把之前月份的总天数累加出来，然后加上这个月的天数就好了
        # 先定一个总天数
        #i就是当天的月份数
            #接下来，我们要找出，这个月有多少天 找到以后，加到总天数上
            #找天数的过程，我们说要从字典里找到 我们根据items方法，可以获取到字典里的所有key和value
            #你刚才获取到的记过是 [(31, {1, 3, 5, 7, 8, 10, 12}), (30, {9, 10, 4, 6}), (28, 2)] 对吧 那么你看这个结果是什么类型的 列表
            #嗯 那列表里每个元素又是什么类型的 元祖
            #(31, {1, 3, 5, 7, 8, 10, 12})
            #(30, {9, 10, 4, 6})
            #(28, 2)
            #那么 这些元祖里面，第一个值，都是字典里面的key也就是天数 第二个值，是月份的集合对不嗯嗯
            #所以 我们要做的，首先，就是循环items返回的列表，然后，循环列表元素中的元祖，然后，循环元祖中第二个值（月份的集合），这样我们就能找到对应月份在那个里面了对不嗯嗯
            #这里的循环，我们可以直接在循环里面使用dict的key和value
                #value有两种类型，一种是集合的 一种的是只有一个2的对吧 所以我们要先判断value的类型，是集合的时候，我们再循环，如果是2，就直接取值了
                #或者直接判断是不是2就好了
                #我这里写错了吗 elif 这个后面要加条件，不然就用else 哦哦
                    #这里，我们要在集合里面，判断是否包含当前月份 我们去查一下，集合有没有相关方法可以直接判断是否包含某个元素 in就行 好
                     #当集合包含当前月份的时候，我们把天数赋给之前定义好的参数，然后跳出循环
                     #这里敷完值以后，跳出循环，进行加天数
                     #到这里，我们就加完一个月份的天数了。 然后一直循环，直到把所有的月份都加完
                     #到这里，我们就加完一个月份的天数了。 然后一直循环，直到把所有的月份都加完
        '''