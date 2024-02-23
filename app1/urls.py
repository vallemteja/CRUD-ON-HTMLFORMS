
from django.contrib import admin
from django.urls import path
from demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('devil/',views.com,name="com"),
    path('add/',views.add,name="add"),
    path('addrec/',views.addrec,name="addrec")
]
