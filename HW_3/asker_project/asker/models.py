from django.db import models

from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    def update_answer_count(self, question):
        answer_count = Answer.objects.filter(question=question).count()
        question.answer_count = answer_count
        question.save()

    def update_like_count(self, question):
        like_count = LikeQuestion.objects.filter(question=question).count()
        question.like_count = like_count
        question.save()

    def new(self):
        return self.all().order_by("-creation_date")

    def hot(self):
        return self.all().order_by("-like_count")
    
class Answermanager(models.Manager):
    def hot(self, question):
        return self.filter(question=question).order_by("-like_count")
    
class ProfileManager(models.Manager):
    def best_members(self):
        return Profile.objects.annotate(answer_count=models.Count('answers')).order_by("-answer_count")
    
class TagManager(models.Manager):
    def popular_tags(self):
        return Tag.objects.annotate(question_count=models.Count('questions')).order_by('-question_count')#????
    
class LikeQuestionManager(models.Manager):
    pass

class LikeAnswerManager(models.Manager):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='avatars/')

    objects = ProfileManager()

    def __str__(self):
        return f"{self.name}"

class Tag(models.Model):
    title = models.CharField(max_length=20)

    objects = TagManager()

    def __str__(self):
        return f"{self.title}"

class Question(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now=True)
    like_count = models.IntegerField(default=0)
    answer_count = models.IntegerField(default=0)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True)

    objects = QuestionManager()

    def __str__(self):
        return f"{self.title}"

class Answer(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    like_count = models.IntegerField(default=0)

    objects = Answermanager()

    def __str__(self):
        return f"{self.text}"


class LikeQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default="False")

    def __str__(self):
        return f"{self.id}"

class LikeAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default="False")

    def __str__(self):
        return f"{self.id}"