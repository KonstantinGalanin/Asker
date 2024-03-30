from django.shortcuts import render
from .models import Profile, Question, Answer, Tag, LikeQuestion, LikeAnswer
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseNotFound
import math
# Create your views here.

def paginate(request, objects, per_page=5):
    page = request.GET.get('page', 1)
    paginator = Paginator(objects, per_page)
    return paginator.get_page(page)

def index(request):
    questions = Question.objects.all()
    for question in questions:
        Question.objects.update_answer_count(question)
        Question.objects.update_like_count(question)
    context = {'questions' : paginate(request, Question.objects.new()),
               'tags' : Tag.objects.popular_tags(),
               'best_members' : Profile.objects.best_members(),
               }
    return render(request, 'index.html', context)


def ask(request):
    context = {'tags' : Tag.objects.popular_tags(),
               'best_members' : Profile.objects.best_members(),
               }
    return render(request, 'ask.html', context)

def hot(request):
    questions = Question.objects.all()
    for question in questions:
        Question.objects.update_answer_count(question)
        Question.objects.update_like_count(question)
    context = {'questions' : paginate(request, Question.objects.hot()),
               'tags' : Tag.objects.popular_tags(),
               'best_members' : Profile.objects.best_members(),
               }
    return render(request, 'hot.html', context) #

def login(request):
    context = {'tags' : Tag.objects.popular_tags(),
               'best_members' : Profile.objects.best_members(),
               }
    return render(request, 'login.html', context)

def question(request, question_id):
    question = Question.objects.get(pk=question_id)

    context = {'question' : question,
               'answers' : paginate(request, Answer.objects.hot(question)),
               'tags' : Tag.objects.popular_tags(),
               'best_members' : Profile.objects.best_members(),
               'question_id' : question_id,
               }
    return render(request, 'question.html', context)


def register(request):
    context = {'tags' : Tag.objects.popular_tags(),
               'best_members' : Profile.objects.best_members(),
               }
    return render(request, 'register.html', context)

def settings(request):
    context = {'tags' : Tag.objects.popular_tags(),
               'best_members' : Profile.objects.best_members(),
               }
    return render(request, 'settings.html', context)

def tag(request, tag_name):

    target_tag = Tag.objects.get(title=tag_name)
    questions_tag = Question.objects.filter(tags__title=tag_name) # How it works ??

    context = {'questions' : paginate(request, questions_tag),
               'tags' : Tag.objects.popular_tags(),
               'best_members' : Profile.objects.best_members(),
               'tag_name' : tag_name,
               'likes' : LikeQuestion.objects.all(),
               }
    return render(request, 'tag.html', context)