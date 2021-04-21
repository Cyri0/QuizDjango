from django.shortcuts import render
from quiz_game.models import BasicQuiz
import random

def quiz_view(request):
    quizes = BasicQuiz.objects.filter()
    quiz = quizes[random.randint(0,len(quizes)-1)]
    context = {
        "quiz":quiz
    }
    return render(request, 'quiz.html', context)

def test_view(request, id, answ):
    quiz = BasicQuiz.objects.filter(id=id)[0]
    result = False
    if quiz.good == answ:
        result = True

    context = {
        "quiz" : quiz,
        "result" : result
    }
    return render(request, 'quiz.html', context)