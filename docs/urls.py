from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippets/', SnippetList.as_view(), name = "snippet_list"),
    path('snippets/<int:pk>/', SnippetDetail.as_view(), name = "snippet_list_by_id"),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
#  api-auth/login
#  api-auth/register

urlpatterns = format_suffix_patterns(urlpatterns)