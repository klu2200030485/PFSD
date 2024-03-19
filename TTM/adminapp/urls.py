from django.urls import path
from . import views
from django.urls import path
urlpatterns = [
    path("ttmhome",views.ttmhome,name="ttmhome"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("checkregistration", views.checkregistration, name="checkregistration"),
    path("checkpackage", views.checkpackage, name="checkpackage"),
    path("viewplaces", views.viewplaces, name="viewplaces"),
    path("changepassword", views.checkchangepassword, name="changepassword"),
    path("mail", views.mail, name="mail"),
    path("sendmail", views.sendmail, name="sendmail"),
    path("logout",views.logout,name="logout"),
]