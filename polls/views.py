from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    numbers = [1, 2, 3, 4, 5]
    context = {"list": latest_question_list,
               "numbers": numbers}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def test():
    print("Hello World")
    return
