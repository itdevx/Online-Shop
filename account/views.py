from django.shortcuts import render
from django.views.generic import View


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)
    

class ProfileView(View):
    template_name = 'profile.html'

    def get(self, request):
        return render(request, self.template_name)