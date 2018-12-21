from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.forms import UserCreationForm

from . forms import RegisterFrom,Changepswform,Weiboform
from . models import MyUser,Weibo
import datetime,time

# Create your views here.


def me(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST['delete']
            Weibo.objects.filter(author=request.user.username, id=id).delete()
        text = MyUser.objects.get(id=request.user.id)
        weibos = Weibo.objects.all().order_by('-id')  # 获得所有的博客按时间排序
        return render(request, 'me.html', {'text': text,'weibos':weibos})
    else:
        return redirect('login')


def nlogin(request):
    if request.method=='POST':
        email = request.POST['username']
        password = request.POST['password']
        if MyUser.objects.filter(username=email):
            user = MyUser.objects.get(username=email)
            if check_password(password,user.password):
                request.session['name'] = email
                login(request, user)
                return redirect('me')
            else:
                return render(request, 'login.html', {'error': 'password is invalid.'})
        elif MyUser.objects.filter(email=email):
            user = MyUser.objects.get(email=email)
            if check_password(password,user.password):
                login(request, user)
                return redirect('me')
            else:
                return render(request, 'login.html', {'error': 'password is invalid.'})
        else:
            return render(request, 'login.html', {'error': 'email/username not found.'})
    else:
        return render(request,'login.html')


def nlogout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegisterFrom(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username=form.cleaned_data['username']
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['password_confirmation']
            if MyUser.objects.filter(email=email):
                return render(request, 'register.html', {'form': form, 'invalid': 'email already taken.'})
            if username.isalpha() == False:
                return render(request, 'register.html', {'form': form, 'invalid': 'username has illegal characters.'})
            if MyUser.objects.filter(username=username):
                return render(request, 'register.html', {'form': form, 'invalid': 'username already taken.'})
            if password1.__len__()< 6:
                return render(request, 'register.html', {'form': form, 'invalid': 'password too short.'})
            if password1 and password2 and password1 != password2:
                return render(request, 'register.html', {'form': form, 'invalid': 'password mismatch.'})
            user = MyUser(email=email,username=username, password=make_password(password1,None, 'pbkdf2_sha256'),creation_date=datetime.datetime.now())
            user.save()
            login(request, user)
            return redirect('me')
        else:
             return render(request,'register.html',{'form': form})
    else:
        form = RegisterFrom()
        return render(request, 'register.html', {'form': form})


def change_psw(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Changepswform(request.POST)
            obj = MyUser.objects.get(id=request.user.id)
            if form.is_valid():
                old_password = form.cleaned_data['old_password']
                password = form.cleaned_data['password']
                password_confirmation = form.cleaned_data['password_confirmation']
                if password.__len__() < 6:
                    return render(request, 'change_psw.html', {'form': form, 'invalid': 'password too short.'})
                if password and password_confirmation and password != password_confirmation:
                    return render(request, 'change_psw.html', {'form': form, 'invalid': 'password mismatch.'})
                if check_password(old_password,obj.password):
                    MyUser.objects.filter(email=obj.email).update(password=make_password(password,None, 'pbkdf2_sha256'))
                    user=MyUser.objects.get(email=obj.email)
                    login(request, user)
                    return render(request, 'change_psw.html', {'form': form, 'invalid': 'success'})
                else:
                    return render(request, 'change_psw.html', {'form': form, 'invalid': 'invalid password.'})
            else:
                return render(request, "change_psw.html", {'form': form})
        else:
            form = Changepswform()
            return render(request, 'change_psw.html', {'form': form})
        return render(request, 'change_psw.html', {'form': form})
    else:
        return redirect('login')

def weibo_add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Weiboform(request.POST)
            if form.is_valid():
                content=form.cleaned_data['content']
                if content.__len__() > 300:
                    return render(request, 'weibo_add.html', {'invalid': 'too long.'})
                weibo = Weibo(author=request.user.username,posted_date=time.strftime("%Y/%m/%d %H:%M"), content=content,likes=0)
                weibo.save()
                return redirect('me')
            else:
                 return render(request,'weibo_add.html',{'form': form})
        else:
            form =Weiboform()
            return render(request, 'weibo_add.html', {'form': form})
    else:
        return redirect('login')


def search_info(request):
      if request.user.is_authenticated:
           search_info = request.POST.get('searchBox')
           if not search_info:
                error_msg = 'Please enter a username'
                return render(request, 'result.html', {'error_msg': error_msg})
           info = Weibo.objects.filter(author=search_info).order_by('-id')
           return render(request, 'result.html', {'info': info})
      else:
           return redirect('login')