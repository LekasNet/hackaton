from django.db import models
from django.db.models import Sum, Count
from django.conf import settings


class Quest(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название квеста')
    description = models.TextField(default='', verbose_name='Описание')
    is_active = models.BooleanField(default=False, verbose_name='Квест активен')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='quests', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_questions(self):
        return Question.objects.filter(quest=self).order_by('id')

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
            return Question.objects.filter(quest=quest).order_by('id').first()
        else:
            return Question.objects.filter(id__gt=self.id, quest=self.quest).order_by('id').first()

    def __str__(self):
        return self.text


class Answer(models.Model):
    anstext = models.CharField(max_length=255, verbose_name='Вариант ответа')
    is_true = models.BooleanField(default=False, verbose_name='Правильный ответ')
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return self.anstext


class UserAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    is_true = models.BooleanField(default=False, verbose_name='Правильный ответ')
    cost = models.IntegerField(verbose_name='Стоимость вопроса', default=0)

    @staticmethod
    def get_cost_user_result(user, quest_id):
        return UserAnswer.objects.filter(user=user, question__quest_id=quest_id).aggregate(Sum('cost'))

    @staticmethod
    def get_gamers(quest_id):
        return UserAnswer.objects.filter(question__quest_id=quest_id).values('user__email').order_by('user__email').annotate(
            count=Count('user'), cost=Sum('cost'))

    @staticmethod
    def get_quests(user):
        return UserAnswer.objects.filter(user=user).values('question__quest__name').order_by(
            'question__quest__name').annotate(
            count=Count('question__quest'), cost=Sum('cost'))
