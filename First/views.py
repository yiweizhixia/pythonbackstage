from django.shortcuts import render
from First.models import Stu
from django.http import HttpResponse,JsonResponse
import json

# Create your views here.
def showInfo(request):
    stu_list = Stu.objects.all()
    content = {'list':stu_list}
    return render(request,'index.html',content)

# 新增用户
def add_stu(request):
    if request.method == "POST":
        add_st = Stu(name="xiaoxiao")
        add_st.save()
        return HttpResponse("<p>数据添加成功！</p>")

        """
        req = json.load(request.body)
        print(req)
        #key_flag = req.get("name")
        key_flag=1
        if key_flag:
            name = req["name"]
            add_st = Stu(name=name)
            add_st.save()
            return JsonResponse({"status":"BS.200","msg":"public stu success."})
        else:
            return JsonResponse({"status":"BS.400","msg":"please check para."})
        """
    elif request.method == "GET":
        stus = {}
        query_stu = Stu.objects.all()
        for title in query_stu:
            stus[title.id] = title.name
        return JsonResponse({"status": "BS.200", "all_titles": stus, "msg": "query articles sucess."})
    else:
        return JsonResponse({"status": "BS.400", "msg": "please check method."})

def testdb(request):
    test1 = Stu(name='lili')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")