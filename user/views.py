from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .models import CustomUser
from .tokens import account_activation_token


# Create your views here.
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home:index')
    else:
        return HttpResponse('Activation link is invalid!')


class SignIn(View):
    template_name = "user/signin.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_authent = CustomUser.objects.filter(
            username=username, 
            password=password, 
            is_active=True
        ).first()

        if user_authent:
            login(request, user_authent)
            return redirect("home:index")
        context = {
            "errors": "Username or password does not correct or the account is not activated"
        }
        return render(request, self.template_name, context)
        


class SignUp(View):
    template_name = "user/signup.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        context = {}
        
        checkbox_required = request.POST.get("checkboxterm")

        if not checkbox_required:
            context.update({
                "errors": "Please check to the checkbox"
            })
            return render(request, self.template_name, context)
        password = request.POST.get("pass1")
        confirmation = request.POST.get("pass2")

        if password != confirmation:
            context.update({
                "errors": "Passwords must match."
            })
            return render(request, self.template_name, context)

        username = request.POST.get("username")
        email = request.POST.get("email")
        exist_user = CustomUser.objects.filter(username=username).first()
        if exist_user:
            context.update({
                "errors": "Username exists"
            })
            return render(request, self.template_name, context)

        create_user = CustomUser.objects.create(
            username=username, 
            password=password,
            email=email
        )

        current_site = get_current_site(self.request)
        mail_subject = 'Activate your account.'

        message = render_to_string('user/acc_active_email.html', {
            'user': create_user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(create_user.pk)),
            'token': account_activation_token.make_token(create_user),
        })

        send_email = EmailMessage(
            mail_subject, message, to=[email]
        )

        send_email.send()
        

        # login(request, create_user)
        return HttpResponse('Please confirm your email address to complete the registration')

        # return redirect("home:index")


class SignOut(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("home:index")
