from django.urls import path
from . import views
from .views import RegistrationView,LogoutView,LoginView,UsernameValidationView,EmailValidationView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home),

    path('pharmaceutical/', views.pharmaceutical),
    path('cosmetics/', views.cosmetics),
    path('trainers', views.trainers),
    path('trainings/', views.trainings, name="training programs"),
    path('trainers/<int:id>/', views.trainer_details, name='trainer_details'),
    path('whoweare', views.whoweare, name='whoweare'),
    path('register', RegistrationView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()),name="validate-username"),
    path('validate-email', csrf_exempt(EmailValidationView.as_view()),name='validate_email'),

    # training urls
    path('instrument_validation/', views.validation, name="Instrument validation"),
    path('instrument_calibration/', views.calibration, name="Instrument calibration"),
    path('instrument_operation/', views.operation, name="Instrument operation   "),
    path('instrument_data_analusis/', views.data_analysis, name="Instrument data analysis   "),

         

]