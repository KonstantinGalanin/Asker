from django.db import models

QUESTIONS = [
    {
        'id': i,
        'author' : 'Luke Skywalker',
        'img_address' : "../static/img/avatars/Luke.jpg",
        'title' : f'Question {i}',
        'text' : f'I am question {i}',
        'answers_count' : f'{i * i}',
        'like_count' : f'{i * 2}',
        'tags' : ['force', 'Death Star']
    } for i in range(1,23)
]

ANSWERS = [{
    'id' : i,
    'author' : 'Darth Vader',
    'img_address' : "../static/img/avatars/Darth-Vader.png",
    'text' : f'I am answer {i}',
    'like_count' : f'{i * 2}',
    } for i in range(1,4)
] 


tag_names = ['force', 'sith', 'Lightsaber', 'Tatooine', 'Death Star', 'Jedi', 'blaster', 'beep']
POPULAR_TAGS = [
    {
        'name' : tag_name
    } for tag_name in tag_names
]


BEST_MEMBERS = [
    {
        'name' : 'Luke SkyWalker',
        'img_address' : "../static/img/avatars/Luke.jpg",
    },
    {
        'name' : 'Darth Vader',
        'img_address' : "../static/img/avatars/Darth-Vader.png",
    },
    {
        'name' : 'Han Solo',
        'img_address' : "../static/img/avatars/Han-Solo.png",
    },
    {
        'name' : 'Proncess Leya',
        'img_address' : "../static/img/avatars/Leya.png",
    },
    {
        'name' : 'Obi Wan Kenobi',
        'img_address' : "../static/img/avatars/Obi-Wan.png",
    },
    {
        'name' : 'R2-D2',
        'img_address' : "../static/img/avatars/R2-D2.png",
    }
]

# Create your models here.
