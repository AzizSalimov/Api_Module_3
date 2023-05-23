from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Userlist, UserDetail

urlpatterns = [
    path('', Userlist.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
