from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseNotFound
import math
# Create your views here.

def paginate(objects, page, per_page):
    paginator = Paginator(objects, per_page)
    return paginator.page(page)

def index(request):
    page = request.GET.get('page', 1)
    per_page = 5
    pages_count = math.ceil(len(models.QUESTIONS) / per_page) + 1
    pages_range = range(1, pages_count)
    if(int(page) > pages_count):
        return HttpResponseNotFound()
        # raise Http404

    context = {'questions' : paginate(models.QUESTIONS, page, per_page),
               'pages_range' : pages_range,
               'tags' : models.POPULAR_TAGS,
               'best_members' : models.BEST_MEMBERS,
               }
    return render(request, 'index.html', context)


def ask(request):
    context = {'tags' : models.POPULAR_TAGS,
               'best_members' : models.BEST_MEMBERS,
               }
    return render(request, 'ask.html', context)

def hot(request):
    page = request.GET.get('page', 1)
    per_page = 5
    pages_count = math.ceil(len(models.QUESTIONS) / per_page) + 1
    pages_range = range(1, pages_count)
    if(int(page) > pages_count):
        return HttpResponseNotFound()

    context = {'questions' : paginate(models.QUESTIONS, page, per_page),
               'pages_range' : pages_range,
               'tags' : models.POPULAR_TAGS,
               'best_members' : models.BEST_MEMBERS,
               }
    return render(request, 'hot.html', context) #

def login(request):
    context = {'tags' : models.POPULAR_TAGS,
               'best_members' : models.BEST_MEMBERS,
               }
    return render(request, 'login.html', context)

def question(request, question_id):
    question = {}
    for question_item in models.QUESTIONS:
        if(question_item['id'] == question_id):
            question = question_item


    context = {'question' : question,
               'answers' : models.ANSWERS,
               'tags' : models.POPULAR_TAGS,
               'question_id' : question_id,
               'questions' : models.QUESTIONS,
               'best_members' : models.BEST_MEMBERS,
               }
    return render(request, 'question.html', context)

# def question(request):
#     context = {'tags' : models.TAGS,
#                'pages' : models.PAGES,
#                'questions' : models.QUESTIONS,
#                'answers' : models.ANSWERS,
#                }
#     return render(request, 'question.html', context)

def register(request):
    context = {'tags' : models.POPULAR_TAGS,
               'best_members' : models.BEST_MEMBERS,
               }
    return render(request, 'register.html', context)

def settings(request):
    context = {'tags' : models.POPULAR_TAGS,
               'best_members' : models.BEST_MEMBERS,
               }
    return render(request, 'settings.html', context)

def tag(request, tag_name):
    page = request.GET.get('page', 1)
    per_page = 5
    pages_count = math.ceil(len(models.QUESTIONS) / per_page) + 1
    pages_range = range(1, pages_count)
    if(int(page) > pages_count):
        return HttpResponseNotFound()

    questions_tag = []
    for question in models.QUESTIONS:
        if(tag_name in question['tags']):
            questions_tag.append(question)

    pages_range = range(1, math.ceil(len(questions_tag) / per_page) + 1)

    context = {'questions' : paginate(questions_tag, page, per_page),
               'pages_range' : pages_range,
               'tags' : models.POPULAR_TAGS,
               'tag_name' : tag_name,
               'best_members' : models.BEST_MEMBERS,
               }
    return render(request, 'tag.html', context)
