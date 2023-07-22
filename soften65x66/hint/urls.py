from django.urls import path
from . import views

urlpatterns = [
    path('<int:student_id>', views.hint_page, name='hint_page')
]