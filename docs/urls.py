from django.contrib import admin
from django.urls import path
from snippets.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom', checkUtils , name = "cutomm"),
    path('snippets', snippet_list, name = "snippet_list"),
    path('snippets/<int:pk>', snippet_detail, name = "snippet_list_by_id"),
]
