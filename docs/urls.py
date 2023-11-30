from django.contrib import admin
from django.urls import path
from snippets.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom',checkUtils,name="cutomm")
]
