from django.urls import path

from . import views
import authentication.views


app_name = "authentication"
urlpatterns = [
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_def, name='logout'),
]