from django.contrib import admin
from django.urls import path
from app import views  # <-- add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # <-- add this
]
