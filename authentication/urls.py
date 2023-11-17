from django.urls import path

from . import views
import authentication.views


app_name = "authentification"
urlpatterns = [
    path('', authentication.views.login_page, name='login'),
]