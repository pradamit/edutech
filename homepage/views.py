from django.shortcuts import render, redirect
from .models import *

# Create your views here.
from django.http import HttpResponse

def homepage(request):
    if request.method == 'POST':
        l = language.objects.get(name=request.POST['langName'])
        q = questionBank(email=request.POST['EneteredEmail'], language=l, question=request.POST['question'])
        q.save()
        searchedQ = None
        return redirect("/")
    elif request.method == 'GET':
        searchedQ = questionBank.objects.filter(question__contains=request.GET.get("searchQuestion", False))
    book = books.objects.all()
    lang = language.objects.all()
    disciplines = discipline.objects.all()
    exams = exam.objects.all()
    courses = course.objects.all()
    context = {
        'books': book,
        'language': lang,
        'discipline': disciplines,
        'exam': exams,
        'course': courses,
        'searchedQ': searchedQ,
    }
    return render(request, 'homepage/index.html', context)