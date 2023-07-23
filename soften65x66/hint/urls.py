from django.urls import path
from . import views

urlpatterns = [
    path('', views.hint_page, name='hint_page'),
    path('get/<int:student_id>', views.get_hint, name='get_hint')
]