from django.db import models
from django.db.models import Sum, Count
from django.conf import settings


class Quest(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название викторины')
    description = models.TextField(default='', verbose_name='Описание')
    is_active = models.BooleanField(default=False, verbose_name='Викторина активна')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='quizzes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_questions(self):
        return Question.objects.filter(quiz=self).order_by('id')

    def get_questions_count(self):
        return self.questions.all().count()

    def get_questions_cost(self):
        return self.questions.aggregate(Sum('cost'))


class Question(models.Model):
    text = models.TextField(verbose_name='Текст вопроса')
    quest = models.ForeignKey(Quest, related_name='questions', on_delete=models.CASCADE)
    cost = models.IntegerField(verbose_name='Стоимость вопроса', default=0)

    def next_question(self, quest=None):
        if quest:
            return Question.objects.filter(quiz=quest).order_by('id').first()
        else:
            return Question.objects.filter(id__gt=self.id, quiz=self.quest).order_by('id').first()

    def __str__(self):
        return self.text
