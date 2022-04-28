from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.users.forms import LoginForm


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "register.html")

    def post(self, request, *args, **kwargs):
        return render(request, "register.html")


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class LoginView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        # 登陆表单
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # user_name = request.POST.get("username", "")
            # password = request.POST.get("password", "")
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # 验证用户名密码, 成功之后会返回一个user对象，否则为None
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                # 处理登录之后的首页链接问题
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"login_form": login_form})
