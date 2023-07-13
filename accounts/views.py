import datetime
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserSignupForm, VerifyCodeForm, UserLoginForms
import random
from django.contrib import messages
from .models import OtpCode, User
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


class UserSignupView(View):
    form_class = UserSignupForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            print(random_code)
            cd = form.cleaned_data
            OtpCode.objects.create(phone_number=cd['phone'], code=random_code)
            request.session['user_signup_info'] = {
                'phone_number': cd['phone'],
                'email': cd['email'],
                'full_name': cd['full_name'],
                'password': cd['password2'],
            }
            messages.success(request, "we sent you a code", 'success')
            return redirect('account:verify_code')
        return redirect('account:user_sign_up')


class UserSignupVerifyView(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_signup_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        now = datetime.datetime.now()
        minute = now.minute
        expire_local_time = timezone.localtime(code_instance.created)
        expire_minute = expire_local_time.minute + 1
        form = self.form_class(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                if minute > expire_minute:
                    code_instance.delete()
                    messages.error(request, "your code expired try again", 'danger')
                    return redirect('account:user_sign_up')
                else:
                    User.objects.create_user(user_session['email'], user_session['phone_number'], user_session[
                        'full_name'], user_session['password'])
                    code_instance.delete()
                    messages.success(request, "you sign up successfully", 'success')
                    return redirect('home:home')
            else:
                messages.error(request, 'this code is wrong try again', 'danger')
                return redirect('account:verify_code')
        return redirect('home:home')


class UserLoginView(View):
    class_form = UserLoginForms

    def get(self, request):
        form = self.class_form
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you login successfully', 'success')
                return redirect('home:home')
            messages.error(request, 'your entered information is wrong ', 'danger')
        return render(request, 'accounts/login.html', {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logout successfully', 'success')
        return redirect('home:home')
