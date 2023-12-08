from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from account.forms import RegisterForm
from account.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from account.forms import LoginForm

# email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.utils.encoding import force_bytes, force_str
from account.token import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse



class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('product:index')

        return render(request, self.template_name, {'form': form})
        

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعالسازی اکانت '
        message = render_to_string('registration/account_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('Please confirm your email address to complete the registration')


def verify(request, uidb64, token):
    user = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('product:index')
    else :
        return HttpResponse('Activation link is invalid!')  





class ProfileView(View):
    template_name = 'profile.html'

    def get(self, request):
        return render(request, self.template_name)
    

class ForgotView(View):
    template_name = 'forgot.html'

    def get(self, request):
        return render(request, self.template_name)