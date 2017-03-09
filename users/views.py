from django.shortcuts import render, redirect
from django import forms
from django.core.mail import send_mail
from .models import User, UserActive
from datetime import datetime, timedelta
import uuid
# Create your views here.


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'nickname', 'stevens_id']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email += '@stevens.edu'
            user.posts = ''
            user.is_Admin = False
            user.is_Verified = False
            user.save()

            user = User.objects.get(email=user.email)
            activate_code(user, request)

            return redirect('/')
        else:
            return render(request, 'register.html', {"form": form})


def activate_code(user, request):
    code = str(uuid.uuid4()).replace("-", "")
    # link = "%s/activate/%s" % (request.get_host(), code)
    user_active = UserActive(user=user, active_code=code, expire_date=datetime.today()+timedelta(hours=24))
    activate_email = 'Your code: ' + code  # <%s>.' % code
    send_mail(
        subject='StevensHelper Activation',
        message=activate_email, # link to activate your account: %s' % link,
        # html_message=activate_email,
        from_email='stevenshelper@163.com',
        recipient_list=[user.email],
        fail_silently=False
    )
    # may need update
    user_active.save()
    return None


def activate(request):
    pass


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = request.POST['email']
            password = request.POST['password']
            user.email += "@stevens.edu"
            # email = user.email
            try:
                user = User.objects.get(email=user.email, password=user.password)
            except user.DoesNotExist:
                error = 'Incorrect email or password, please input again.'
                return render(request, 'login.html', {"error": error})
            if user:
                request.session['email'] = user.email
                request.session['nickname'] = user.nickname
                return redirect('/')
            else:
                error = 'Incorrect email or password, please input again.'
                return render(request, 'login.html', {"form": form})
        else:
            return render(request, 'login.html', {"form": form})


def logout(request):
    del request.session['email']
    del request.session['nickname']
    return redirect('/')