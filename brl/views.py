from django.shortcuts import render,HttpResponse
from brl.models import Page_list
from django.http import JsonResponse
from brl.myfunc import DateEncoder,get_time_data,dict_2d_fun,screen_data
import json
# Create your views here.
def get_data(requests):
    '''
    进入页面
    :param request:
    :return:
    '''
    tables_list = Page_list.objects.filter(pk__gt=0)
    if requests.method == 'GET':
        return render(request=requests, template_name='t/1.1.html', context={'tables_list': tables_list})
    else:
        return HttpResponse('出错了')

def logging(requests):
    data = {'data': '输入指令异常'}
    lists = None
    '''
    获取表的字段
    :param requests:
    :return:
    '''
    try:
        # print('开始访问')
        if requests.method == "POST":
            starttime = requests.POST.get('开始时间')
            endtime = requests.POST.get('结束时间')
            a_ac = requests.POST.get('A相电流')
            b_ac = requests.POST.get('B相电流')
            c_ac = requests.POST.get('C相电流')
            a_uv = requests.POST.get('A相电压')
            b_uv = requests.POST.get('B相电压')
            c_uv = requests.POST.get('C相电压')
            m_s = requests.POST.get('总有功电度')
            r_s = requests.POST.get('总无功电度')
            m_m = requests.POST.get('当月有功电度')
            m_r = requests.POST.get('当月无功电度')
            e_t1 = requests.POST.get('环境温度1')
            e_t2 = requests.POST.get('环境温度2')
            e_t3 = requests.POST.get('环境温度3')
            e_t4 = requests.POST.get('环境温度4')
            e_t5 = requests.POST.get('环境温度5')
            e_t6 = requests.POST.get('环境温度6')
            e_t7 = requests.POST.get('环境温度7')
            e_t8 = requests.POST.get('环境温度8')
            e_t9 = requests.POST.get('环境温度9')
            e_t10 = requests.POST.get('环境温度10')
            e_t11 = requests.POST.get('环境温度11')
            e_t12 = requests.POST.get('环境温度12')
            h_t1 = requests.POST.get('环境湿度1')
            h_t2 = requests.POST.get('环境湿度2')
            lists = [a_ac, b_ac, c_ac, a_uv, b_uv, c_uv, m_s, r_s, m_m, m_r, e_t1, e_t2, e_t3, e_t4, e_t5, e_t6, e_t7,
                     e_t8,
                     e_t9, e_t10, e_t11, e_t12, h_t1, h_t2]
            # print(lists)
            while None in lists:
                lists.remove(None)  # 删除没选中的元素
            # print(starttime, '开始时间', endtime, '结束时间')
            if starttime == '' or endtime == '':
                data = {'data': {'data': '请输入时间选项'}}
                return JsonResponse(data=data)
            else:
                if lists:
                    try:
                        data = get_time_data(data=lists, starttime=starttime, endtime=endtime)
                    except Exception as e_sql:
                        data = {'data': {'data': '数据库查询输错:%s' % e_sql}}
                        print(e_sql)
                        return JsonResponse(data=data)
                        # 获取数据库数据
                    if data.count():
                        data_time = data.values('时间')  # 单独获取时间数据
                        dict_time = screen_data(data_time)  # 筛选
                        dict_2d = dict_2d_fun(item=lists, data=data)
                    else:
                        data = {'data': {'data': '当前时间段%s-%s数据不存在' % (starttime, endtime)}}
                        return JsonResponse(data=data)
                else:
                    data = {'data': {'data': '请输入数据选项'}}
                    return JsonResponse(data=data)
    except Exception as e_all:
        print('出错为', e_all)
        data = {'data': {'data': '输入出错'}}
        return JsonResponse(data=data)
    else:
        try:
            if isinstance(data, dict):
                json_data = data
                return JsonResponse(data=json_data, safe=False, json_dumps_params={'ensure_ascii': False})

            else:
                if dict_2d and dict_time and lists:
                    # print(2222)
                    json_dict_time = json.dumps(dict_time, cls=DateEncoder, ensure_ascii=False)
                    json_dict_2d = json.dumps(dict_2d, cls=DateEncoder, ensure_ascii=False)
                    json_lists = json.dumps(lists, cls=DateEncoder, ensure_ascii=False)
                    data_a = {'json_dict_time': json_dict_time, 'json_dict_2d': json_dict_2d, 'json_lists': json_lists}
                    return JsonResponse(data=data_a, safe=False, json_dumps_params={'ensure_ascii': False})
                else:
                    data = {'data': {'data': '当前时间段%s-%s数据不存在' % (starttime, endtime)}}
                    return JsonResponse(data=data)
        except Exception as e:
            data = {'data': {'data': '操作异常%s' % e}}
            return JsonResponse(data=data)