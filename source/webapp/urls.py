
from django.urls import path
from webapp.views import welcome, cat_info

urlpatterns = [
    path('', welcome, name='welcome'),
    path('cat/<int:cat_id>/', cat_info, name='cat_info'),
]
