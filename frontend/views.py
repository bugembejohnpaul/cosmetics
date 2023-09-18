from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
# from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from panel.models import Trainer
from django.shortcuts import render, get_object_or_404


# @login_required(login_url='/login')
def home(request):
    return render(request, "frontend/home.html")

# pharmaceuticals
def pharmaceutical(request):
    return render(request, "frontend/pharmaceuticals.html")

# cosmetics
def cosmetics(request):
    return render(request, "frontend/cosmetics.html")


def whoweare(request):
    trainers = Trainer.objects.all()
    return render(request, "frontend/whoweare.html", {'trainers': trainers})


def trainers(request):
    trainers = Trainer.objects.all()
    return render(request, "frontend/trainers.html", {'trainers': trainers})
# single Trainer
def trainer_details(request, id):
    trainer = get_object_or_404(Trainer, pk=id)
    return render(request, 'frontend/trainer_details.html', {'trainer': trainer})


class RegistrationView(View):
    def get(self, request):
        return render(request, 'frontend/register.html')

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'frontend/register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, 'Account successfully created')
                return render(request, 'frontend/register.html')

        return render(request, 'frontend/register.html')


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'sorry email in use,choose another one '}, status=409)
        return JsonResponse({'email_valid': True})


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'sorry username in use,choose another one '}, status=409)
        return JsonResponse({'username_valid': True})


class LoginView(View):
    def get(self, request):
        return render(request, 'frontend/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' +
                                     user.username+' you are now logged in')
                    return redirect('/')
                messages.error(
                    request, 'Account is not active,please check your email')
                return render(request, 'frontend/login.html')
            messages.error(
                request, 'Invalid credentials,try again')
            return render(request, 'frontend/login.html')

        messages.error(
            request, 'Please fill all fields')
        return render(request, 'frontend/login.html')
    

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')

def trainings(request):
    return render(request, 'frontend/trainings.html')

# training views
def validation(request):
    return render(request, 'frontend/trainings/instrument_validation.html')
def calibration(request):
    return render(request, 'frontend/trainings/instrument_calibration.html')
def operation(request):
    return render(request, 'frontend/trainings/instrument_operation.html')
def data_analysis(request):
    return render(request, 'frontend/trainings/instrument_data_analysis.html')