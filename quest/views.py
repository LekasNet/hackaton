from django.shortcuts import render
from django.views import View
from .models import Quest, Question, Answer, UserAnswer
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


class ActiveQuestView(View):

    def get(self, request):
        active_quests = Quest.objects.filter(is_active=True)
        return render(request, 'quest/active_quests.html', {'active_quests': active_quests})


class QuestView(View):
    def get(self, request, quest_id):
        quest = get_object_or_404(Quest, pk=quest_id)
        first_question = Question().next_question(quest=quest)
        return render(request, 'quest/quest.html', {'quest': quest, 'first_question': first_question})


class QuestionView(View):

    def get(self, request, quest_id, question_id):
        quest = get_object_or_404(Quest, pk=quest_id)
        question = get_object_or_404(Question, pk=question_id, quest_id=quest)
        next_question = question.next_question()
        gamers = UserAnswer.get_gamers(quest.id)
        return render(request, 'quest/question.html',
                      {'quest': quest, 'question': question, 'next_question': next_question, 'gamers':gamers})

    def post(self, request, quest_id, question_id):
        quest = get_object_or_404(Quest, pk=quest_id)
        question = get_object_or_404(Question, pk=question_id, quest_id=quest)
        answer_id = request.POST.get('answer')
        answer = get_object_or_404(Answer, pk=answer_id, question=question)
        result, created = UserAnswer.objects.get_or_create(user=request.user,
                                                           question=question,
                                                           defaults={'answer': answer, 'is_true': answer.is_true,
                                                                                    'cost': question.cost if answer.is_true else 0})
        next_question = question.next_question()

        if next_question:
            return redirect('question_url', quest.id, next_question.id)
        else:
            return redirect('quest_end', quest.id)


class QuestEndView(View):

    def get(self, request, quest_id):
        quest = get_object_or_404(Quest, pk=quest_id)
        cost = UserAnswer.get_cost_user_result(request.user, quest.id)
        return render(request, 'quest/end.html',
                      {'quest': quest, 'cost': cost})


class MyStatView(View):
    def get(self, request):
        quests = UserAnswer.get_quests(request.user)
        return render(request, 'quest/statistic.html',
                      {'quests':quests})
