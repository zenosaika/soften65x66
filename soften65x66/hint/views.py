from django.shortcuts import render
from django.http import HttpResponse
from .models import Hint
from django.core import serializers

def hint_page(request):
    return render(request, 'hint/hint.html')

def get_hint(request, student_id):
    hints = Hint.objects.filter(student_id=student_id)
    serialized_obj = serializers.serialize('json', hints)
    return HttpResponse(serialized_obj)