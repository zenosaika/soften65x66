from django.shortcuts import render
from django.http import HttpResponse
from .models import Hint

def hint_page(request, student_id):
    hints = Hint.objects.filter(student_id=student_id)
    res = '<br>'.join([f'{hint.no}. {hint.text}' for hint in hints])
    return HttpResponse(res)