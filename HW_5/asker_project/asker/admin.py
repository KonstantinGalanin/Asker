from django.contrib import admin
from .models import Profile, Question, Answer, Tag, LikeQuestion, LikeAnswer
# Register your models here.

admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(LikeQuestion)
admin.site.register(LikeAnswer)