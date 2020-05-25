import json
from datetime import date, datetime, timedelta
from brl.models import Jtsb1


class DateEncoder(json.JSONEncoder):
    '''
    处理json格式
    '''

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
def gtime(t):
    t = t + ':00'
    return datetime.strptime(t, "%Y-%m-%d %H:%M:%S")


def get_time_data(data, starttime, endtime):
    if len(data) == 1:
        t1, t2 = gtime(starttime), gtime(endtime)
        user_time = Jtsb1.objects.filter(
            时间__range=(t1, t2)).values('%s' % data[0], '时间')
        return user_time
    elif len(data) == 2:
        t1, t2 = gtime(starttime), gtime(endtime)
        user_time = Jtsb1.objects.filter(
            时间__range=(t1, t2)).values('%s' % data[0],
                                       '%s' % data[1],
                                       '时间')
        return user_time
    elif len(data) == 3:
        t1, t2 = gtime(starttime), gtime(endtime)
        user_time = Jtsb1.objects.filter(
            时间__range=(t1, t2)).values('%s' % data[0],
                                       '%s' % data[1],
                                       '%s' % data[2],
                                       '时间')
        return user_time
    elif len(data) == 4:
        t1, t2 = gtime(starttime), gtime(endtime)
        user_time = Jtsb1.objects.filter(
            时间__range=(t1, t2)).values('%s' % data[0],
                                       '%s' % data[1],
                                       '%s' % data[2],
                                       '%s' % data[3],
                                       '时间')
        return user_time

    elif len(data) == 5:
        t1, t2 = gtime(starttime), gtime(endtime)
        user_time = Jtsb1.objects.filter(
            时间__range=(t1, t2)).values('%s' % data[0],
                                       '%s' % data[1],
                                       '%s' % data[2],
                                       '%s' % data[3],
                                       '%s' % data[4],
                                       '时间')
        return user_time
    elif len(data) == 6:
        t1, t2 = gtime(starttime), gtime(endtime)
        user_time = Jtsb1.objects.filter(
            时间__range=(t1, t2)).values('%s' % data[0],
                                       '%s' % data[1],
                                       '%s' % data[2],
                                       '%s' % data[3],
                                       '%s' % data[4],
                                       '%s' % data[5],
                                       '时间')
        return user_time
    elif len(data) == 7:
        t1, t2 = gtime(starttime), gtime(endtime)
        user_time = Jtsb1.objects.filter(
            时间__range=(t1, t2)).values('%s' % data[0],
                                       '%s' % data[1],
                                       '%s' % data[2],
                                       '%s' % data[3],
                                       '%s' % data[4],
                                       '%s' % data[5],
                                       '%s' % data[6],
                                       '时间')
        return user_time
    elif len(data) == 8:
        t1, t2 = gtime(starttime), gtime(endtime)
        user_time = Jtsb1.objects.filter(
            时间__range=(t1, t2)).values('%s' % data[0],
                                       '%s' % data[1],
                                       '%s' % data[2],
                                       '%s' % data[3],
                                       '%s' % data[4],
                                       '%s' % data[5],
                                       '%s' % data[6],
                                       '%s' % data[7],
                                       '时间')
        return user_time
    elif len(data) == 9:
        t1, t2 = gtime(starttime), gtime(endtime)
        user_time = Jtsb1.objects.filter(
            时间__range=(t1, t2)).values('%s' % data[0],
                                       '%s' % data[1],
                                       '%s' % data[2],
                                       '%s' % data[3],
                                       '%s' % data[4],
                                       '%s' % data[5],
                                       '%s' % data[6],
                                       '%s' % data[7],
                                       '%s' % data[8],
                                       '时间')
        return user_time
    # elif len(data) == 10:
    else:
        t1, t2 = gtime(starttime), gtime(endtime)
        user_time = Jtsb1.objects.filter(
            时间__range=(t1, t2)).values('%s' % data[0],
                                       '%s' % data[1],
                                       '%s' % data[2],
                                       '%s' % data[3],
                                       '%s' % data[4],
                                       '%s' % data[5],
                                       '%s' % data[6],
                                       '%s' % data[7],
                                       '%s' % data[8],
                                       '%s' % data[9],
                                       '时间')
        return user_time


def dict_2d_fun(item, data):
    '''
    输出多个Y值
    :param item:
    :param data:
    :return:
    '''
    try:

        dict_d = []
        # if data.count() > 11000:
        # print('大于11000')
        for i in item:
            data = data.values(i)
            # dict_11d = [data[j][aa] for j in range(0, len(data), 600)]
            dict_11d = screen_data(data, item=i)
            dict_d.append(dict_11d)
            # else:
            #     #print('小于11000')
            #     for i in item:
            #         aa = dicts[i]
            #         dict_1d = [j[aa] for j in data.values(aa)]
            #         # dict_3d = [data.values(aa)[j][aa] for j in range(0,len(data.values(aa)),60)]
            #         dict_d.append(dict_1d)
    except Exception as e:
        return [e]
    else:
        return dict_d


def screen_data(datas, item='时间'):
    lens = len(datas)
    set1 = time_split(lens)
    return [datas[i][item] for i in range(0, lens, set1)]


def time_split(items: int):
    items = int(items)
    if 0 < items <= 3700:
        return 1
    elif 3700 < items <= 10800:
        return 30
    elif 10800 < items <= 21600:
        return 60
    elif 21600 < items <= 43200:
        return 120
    elif 43200 < items <= 86400:
        return 240
    elif 86400 < items <= 172800:
        return 480
    elif 172800 < items <= 345600:
        return 960
    elif items > 345600:
        return 3600
    else:
        return 1
