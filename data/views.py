import ast
import json

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from data.models import ShoesInfo, ClothesInfo, ToolsInfo, UploadRecord


def cors(request, response):
    if request.POST["from"] == "8080":
        response["Access-Control-Allow-Origin"] = "http://localhost:8080"
    if request.POST["from"] == "8081":
        response["Access-Control-Allow-Origin"] = "http://localhost:8081"
    response["Access-Control-Allow-Credentials"] = "true"
    response["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS,DELETE"
    response["Access-Control-Allow-Headers"] = "origin, content-type, accept"
    return response


def back_index(request):
    if request.method == "POST":
        # json_ = request.body.decode('utf-8')
        # json_ = ast.literal_eval(json_)
        json_ = request.POST
        print(json_)
        user = authenticate(username=json_["username"], password=json_["password"])
        if user is not None:
            if user.is_active:
                login(request, user)
                print(request.user.is_authenticated())
                response = HttpResponse(json.dumps({"status": "200", "error": ""}))
                return cors(request, response)
            else:
                response = HttpResponse(json.dumps({"status": "201", "error": "用户未激活"}))
                return cors(request, response)
        else:
            response = HttpResponse(json.dumps({"status": "202", "error": "用户名或密码错误"}))
            return cors(request, response)
    else:
        if request.user.is_authenticated():
            response = HttpResponse(json.dumps({"status": "200", "error": ""}))
            return cors(request, response)
        else:
            response = HttpResponse(json.dumps({"status": "202", "error": "用户名或密码错误"}))
            return cors(request, response)


def shoes_info(request):
    print(request.FILES.getlist("image1"))
    if request.method == "POST":
        # json_ = request.body.decode('utf-8')
        # json_ = ast.literal_eval(json_)
        try:
            ShoesInfo.objects.filter(user=request.POST['user']).get(shoesinfo=request.POST['shoesinfo'])
            response = HttpResponse(json.dumps({"status": "202", "info": "后台已录入过此信息"}))
            return cors(request, response)
        except:
            if len(request.FILES) == 1:
                shoesinfo_new = ShoesInfo(shoesinfo=request.POST['shoesinfo'],
                                          shoesdetail=request.POST['shoesdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                shoesinfo_new.save()
            elif len(request.FILES) == 2:
                shoesinfo_new = ShoesInfo(shoesinfo=request.POST['shoesinfo'],
                                          shoesdetail=request.POST['shoesdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          image2=request.FILES['image2'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                shoesinfo_new.save()
            else:
                shoesinfo_new = ShoesInfo(shoesinfo=request.POST['shoesinfo'],
                                          shoesdetail=request.POST['shoesdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          image2=request.FILES['image2'],
                                          image3=request.FILES['image3'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                shoesinfo_new.save()
            response = HttpResponse(json.dumps({"status": "200", "info": "后台录入数据成功"}))
            return cors(request, response)

    else:
        response = HttpResponse(json.dumps({"status": "203", "info": "请使用post请求"}))
        return cors(request, response)


def clothes_info(request):
    print(request.FILES.getlist("image1"))
    if request.method == "POST":
        # json_ = request.body.decode('utf-8')
        # json_ = ast.literal_eval(json_)
        try:
            ClothesInfo.objects.filter(user=request.POST['user']).get(clothesinfo=request.POST['clothesinfo'])
            response = HttpResponse(json.dumps({"status": "202", "info": "后台已录入过此信息"}))
            return cors(request, response)
        except:
            if len(request.FILES) == 1:
                clothesinfo_new = ClothesInfo(clothesinfo=request.POST['clothesinfo'],
                                            clothesdetail=request.POST['clothesdetail'],
                                            price=request.POST['price'],
                                            image1=request.FILES['image1'],
                                            category=request.POST['category'],
                                            user=request.POST['user'])
                clothesinfo_new.save()
            elif len(request.FILES) == 2:
                clothesinfo_new = ClothesInfo(clothesinfo=request.POST['clothesinfo'],
                                            clothesdetail=request.POST['clothesdetail'],
                                            price=request.POST['price'],
                                            image1=request.FILES['image1'],
                                            image2=request.FILES['image2'],
                                            category=request.POST['category'],
                                            user=request.POST['user'])
                clothesinfo_new.save()

            else:
                clothesinfo_new = ClothesInfo(clothesinfo=request.POST['clothesinfo'],
                                            clothesdetail=request.POST['clothesdetail'],
                                            price=request.POST['price'],
                                            image1=request.FILES['image1'],
                                            image2=request.FILES['image2'],
                                              image3=request.FILES['image3'],
                                            category=request.POST['category'],
                                            user=request.POST['user'])
                clothesinfo_new.save()

            response = HttpResponse(json.dumps({"status": "200", "info": "后台录入数据成功"}))
            return cors(request, response)

    else:
        response = HttpResponse(json.dumps({"status": "203", "info": "请使用post请求"}))
        return cors(request, response)


def tools_info(request):
    print(request.FILES.getlist("image1"))
    if request.method == "POST":
        # json_ = request.body.decode('utf-8')
        # json_ = ast.literal_eval(json_)
        try:
            ToolsInfo.objects.filter(user=request.POST['user']).get(toolsinfo=request.POST['toolsinfo'])
            response = HttpResponse(json.dumps({"status": "202", "info": "后台已录入过此信息"}))
            return cors(request, response)
        except:
            if len(request.FILES) == 1:
                toolsinfo_new = ToolsInfo(toolsinfo=request.POST['toolsinfo'],
                                          toolsdetail=request.POST['toolsdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                toolsinfo_new.save()
            elif len(request.FILES) == 2:
                toolsinfo_new = ToolsInfo(toolsinfo=request.POST['toolsinfo'],
                                          toolsdetail=request.POST['toolsdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          image2=request.FILES['image2'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                toolsinfo_new.save()
            else:
                toolsinfo_new = ToolsInfo(toolsinfo=request.POST['toolsinfo'],
                                          toolsdetail=request.POST['toolsdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          image2=request.FILES['image2'],
                                          image3=request.FILES['image3'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                toolsinfo_new.save()
            response = HttpResponse(json.dumps({"status": "200", "info": "后台录入数据成功"}))
            return cors(request, response)

    else:
        response = HttpResponse(json.dumps({"status": "203", "info": "请使用post请求"}))
        return cors(request, response)


def back_register_do(request):
    if request.method == "OPTIONS":
        response = HttpResponse(json.dumps({"status": "210", "error": ""}))
        return cors(request, response)
    if request.method == "POST":
        # json_ = request.body.decode('utf-8')
        # json_ = ast.literal_eval(json_)
        json_ = request.POST
        print(json_)
        if json_["username"] == "" or json_["password"] == "":
            response = HttpResponse(json.dumps({"status": "204", "error": "用户名及密码不能为空"}))
            return cors(request, response)
        elif int(len(json_["username"])) <= 20 and int(len(json_["password"])) <= 20:
            try:
                User.objects.get(username=json_["username"])
                response = HttpResponse(json.dumps({"status": "205", "error": "此账户已经注册"}))
                return cors(request, response)
            except:
                user = User.objects.create_user(username=json_["username"], password=json_["password"])
                user.save()
                response = HttpResponse(json.dumps({"status": "200", "info": "您已注册成功"}))
                return cors(request, response)
        else:
            response = HttpResponse(json.dumps({"status": "203", "error": "您输入的用户名及密码超过20位"}))
            return cors(request, response)
    else:
        response = HttpResponse(json.dumps({"status": "202", "error": "请输入需要注册的用户名及密码"}))
        return cors(request, response)


def loginout(request):
    try:
        logout(request)
        response = HttpResponse(json.dumps({"status": "200", "info": "登出成功"}))
        return cors(request, response)
    except:
        response = HttpResponse(json.dumps({"status": "202", "info": "登出失败"}))
        return cors(request, response)


def login_re(request):
    if request.method == "OPTIONS":
        response = HttpResponse(json.dumps({"status": "210", "info": ""}))
        return cors(request, response)
    if request.method == "POST":
        if request.user.is_authenticated:
            response = HttpResponse(json.dumps({"status": "200", "info": "处于登入状态", "username": request.user.username}))
            return cors(request, response)
        else:
            response = HttpResponse(json.dumps({"status": "202", "info": "请登入"}))
            return cors(request, response)


def get_backend_info(request):
    if request.method == "OPTIONS":
        response = HttpResponse(json.dumps({"status": "210", "shoesinfo": "none"}))
        return cors(request, response)
    if request.method == "POST":
        shoeinfo_ = ShoesInfo.objects.all()
        print(i.shoesinfo for i in shoeinfo_.values("shoesinfo"))
        response = HttpResponse(json.dumps({"status": "200", "shoesinfo": "asdasd"}))
        return cors(request, response)
    else:
        response = HttpResponse(json.dumps({"status": "202", "shoesinfo": "none"}))
        return cors(request, response)


def save_uploadrecord(request):
    if request.method == "POST":
        try:
            UploadRecord.objects.filter(user=User.objects.get(username=request.POST["user"])).get(shoesinfo=request.POST['info'])
            response = HttpResponse(json.dumps({"status": "202", "info": ""}))
            return cors(request, response)
        except:
            if len(request.FILES) == 1:
                record_new = UploadRecord(category=request.POST["category"],
                                          categorys=request.POST["categorys"],
                                          info=request.POST["info"],
                                          detail=request.POST["detail"],
                                          price=request.POST["price"],
                                          image1=request.FILES["image1"],
                                          user=User.objects.get(username=request.POST["user"]))
                record_new.save()
            elif len(request.FILES) == 2:
                record_new = UploadRecord(category=request.POST["category"],
                                          categorys=request.POST["categorys"],
                                          info=request.POST["info"],
                                          detail=request.POST["detail"],
                                          price=request.POST["price"],
                                          image1=request.FILES["image1"],
                                          image2=request.FILES["image2"],
                                          user=User.objects.get(username=request.POST["user"]))
                record_new.save()
            else:
                record_new = UploadRecord(category=request.POST["category"],
                                          categorys=request.POST["categorys"],
                                          info=request.POST["info"],
                                          detail=request.POST["detail"],
                                          price=request.POST["price"],
                                          image1=request.FILES["image1"],
                                          image2=request.FILES["image2"],
                                          image3=request.FILES["image3"],
                                          user=User.objects.get(username=request.POST["user"]))
                record_new.save()
            response = HttpResponse(json.dumps({"status": "200", "info": "记录成功"}))
            return cors(request, response)

    else:
        response = HttpResponse(json.dumps({"status": "203", "info": "请使用post请求"}))
        return cors(request, response)


def get_uploadrecord(request):
    if request.method == "POST":
        records = UploadRecord.objects.filter(user=User.objects.get(username=request.POST["user"]))
        record_list = []
        for i in range(len(records)):
            print(records[i].image1)
            record = {"data": records[i].data.strftime("%Y-%m-%d %H:%M:%S"),
                      "categorys": records[i].categorys,
                      "category": records[i].category,
                      "info": records[i].info,
                      "detail": records[i].detail,
                      "image1": records[i].image1,
                      "image2": records[i].image2,
                      "image3": records[i].image3,
                      "price": records[i].price,}
            record_list.append(record)
        response = HttpResponse(json.dumps({"status": "200", "info": str(record_list)}))
        return cors(request, response)
    else:
        response = HttpResponse(json.dumps({"status": "202", "info": "请使用post请求"}))
        return cors(request, response)
