from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Question, Answer, Tag, LikeQuestion, LikeAnswer
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseNotFound
from .forms import LoginForm, RegistrationForm, QuestionForm, AnswerForm, SettingsForm
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


def update_question_fields():
    questions = Question.objects.all()
    for question in questions:
        Question.objects.update_answer_count(question)
        Question.objects.update_like_count(question)

def paginate(request, objects, per_page=5):
    page = request.GET.get('page', 1)

    try:
        page = int(page)
    except:
        raise Http404()
    
    paginator = Paginator(objects, per_page)
    return paginator.get_page(page)


def index(request):
    update_question_fields()
    context = {'items' : paginate(request, Question.objects.new()),
               'tags' : Tag.objects.popular_tags(),
               'best_members' : Profile.objects.best_members(),
               'user' : request.user,
               }
    return render(request, 'index.html', context)

@csrf_protect
@login_required(login_url='login')
def ask(request):
    if(request.method == 'GET'):
        question_form = QuestionForm()
    if(request.method == 'POST'):
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(request.user)
            if question:
                # return redirect(reverse('index'))
                return redirect(reverse('question', args=[question.id]))
            else:
                question_form.add_error(None, "Some error")
    context = {'tags' : Tag.objects.popular_tags(),
            'best_members' : Profile.objects.best_members(),
            'form' : question_form,
            'user' : request.user,
            }
    return render(request, 'ask.html', context)
    


def hot(request):
    update_question_fields()
    context = {'items' : paginate(request, Question.objects.hot()),
               'tags' : Tag.objects.popular_tags(),
               'best_members' : Profile.objects.best_members(),
               'user' : request.user,
               }
    return render(request, 'hot.html', context)

@csrf_protect
def login(request):
    if(request.method == 'GET'):
        login_form = LoginForm()
    if(request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(request, **login_form.cleaned_data)
            if user:
                auth.login(request, user)
                return redirect(reverse('index'))
            else:
                login_form.add_error('username', "Passwords or login do not match")

    
    context = {'tags' : Tag.objects.popular_tags(),
               'best_members' : Profile.objects.best_members(),
               'form' : login_form,
               }
    return render(request, 'login.html', context)

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))

@csrf_protect
@login_required(login_url="login")
def question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        if request.method == 'GET':
            answer_form = AnswerForm()
        if request.method == 'POST':
            answer_form = AnswerForm(request.POST)
            if answer_form.is_valid():
                author = request.user.profile
                answer = answer_form.save(question, author)
                if answer:
                    return redirect(reverse('index')) 
                    return redirect(reverse('question', args=[question_id])) #
                    

        context = {'question' : question,
                'items' : paginate(request, Answer.objects.hot(question)),
                'tags' : Tag.objects.popular_tags(),
                'best_members' : Profile.objects.best_members(),
                'question_id' : question_id,
                'form' : answer_form,
                'user' : request.user,
                }
        return render(request, 'question.html', context)
    except Question.DoesNotExist:
        raise Http404

@csrf_protect
def register(request):
    if request.method == 'GET':
        user_form = RegistrationForm()
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            if user:
                return redirect(reverse('index'))
            else:
                user_form.add_error(field=None, error="User saving error!")
    context = {'tags' : Tag.objects.popular_tags(),
               'best_members' : Profile.objects.best_members(),
               'form' : user_form,
               'user' : request.user,
               }
    return render(request, 'register.html', context)

@csrf_protect
@login_required(login_url="login")
def settings(request):
    if request.method == 'GET':
        settings_form = SettingsForm(instance=request.user)
    if request.method == 'POST':
        settings_form = SettingsForm(request.POST, request.FILES, instance=request.user)
        if settings_form.is_valid():
            settings_form.save()
            return redirect(reverse('settings'))
        else:
            print(settings_form.errors)

    context = {'tags' : Tag.objects.popular_tags(),
               'best_members' : Profile.objects.best_members(),
               'form' : settings_form,
               'user' : request.user,
               }
    return render(request, 'settings.html', context)

@login_required(login_url="login")
def tag(request, tag_name):
    context = {'items' : paginate(request, Question.objects.filter(tags__title=tag_name)),
            'tags' : Tag.objects.popular_tags(),
            'best_members' : Profile.objects.best_members(),
            'tag_name' : tag_name,
            'likes' : LikeQuestion.objects.all(),
            'user' : request.user,
            }
    return render(request, 'tag.html', context)