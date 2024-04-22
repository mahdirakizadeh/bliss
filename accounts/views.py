import datetime
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserSignupForm, VerifyCodeForm, UserLoginForms, ForgotForm, VerifyForgotPasswordForm, NewPasswordForm
import random
from django.contrib import messages
from .models import OtpCode, User, OtpCodeForgot
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
# from utils import send_otp_code
from django.core.mail import send_mail


class UserSignupView(View):
    form_class = UserSignupForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            random_code = random.randint(1000, 9999)
            print(random_code)
            send_otp_code(cd['phone'], random_code)
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
        expire_minute = expire_local_time.minute + 4
        form = self.form_class(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                if minute > expire_minute:
                    code_instance.delete()
                    messages.error(request, "your code expired! try again", 'danger')
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


class UserForgotPasswordView(View):
    form_class = ForgotForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/forgot.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        user = User.objects.all()
        if form.is_valid():
            cd = form.cleaned_data
            request.session[' forgot_pass_session'] = {
                'email': cd['email']
            }
            email_session = request.session['forgot_pass_session']
            check_email = email_session['email']
            if check_email == user.email:
                random_code = random.randint(10000, 99999)
                rc = f"your code is {random_code} Do not share it!"
                print(rc)
                send_mail(
                    "Verify Code For Forgot Password",
                    rc,
                    'mahdirr80@gmail.com',
                    [check_email]
                )
                messages.success(request, "code sent!", 'success')

                OtpCodeForgot.objects.create(email=cd['email_session'], code=random_code)
                if cd['code'] == random_code:
                    return redirect('account:newpass')
                messages.error(request, 'your code is not correct', 'error')
                return redirect('account:forgot_password')

            messages.error(request, "your email dose not exist!", 'error')
            return redirect('account:forgot_password')

        messages.error(request, 'please enter email', 'error')
        return redirect('account:forgot_password')


class VerifyForgotPasswordView(View):
    form_class = VerifyForgotPasswordForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/verifyforgot.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email_session = request.session['forgot_pass_session']
            code_instance = OtpCodeForgot.objects.get(email=email_session['email'])
            if cd['code'] == code_instance:
                return redirect('account:newpass')
            messages.error(request, 'your code is not correct', 'error')
            return redirect('account:verifyforgotpass')
        messages.error(request, 'enter number!', 'error')
        return redirect('account:verifyforgotpass')


class NewPasswordView(View):
    form_class = NewPasswordForm

    def get(self, request):
        form = self.form_class(request.POST)
        return render(request, 'accounts/new_password.html', {'form': form})

    def post(self, request):
        form = self.form_class()
        user = User.objects.get(id=request.id)
        if form.is_valid():
            user.set_password("new password")
            user.save()
            messages.success(request, 'your password just change' 'success')
            return redirect('home:home')

        messages.error(request, 'your password just change' 'error')
        return redirect('account:newpass')
