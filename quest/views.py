from django.shortcuts import render
from django.views import View
from .models import Quest, Question
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


class ActiveQuestView(View):

    def get(self, request):
        active_quests = Quest.objects.filter(is_active=True)
        return render(request, 'quest/active_quests.html', {'active_quests': active_quests})


class QuestView(View):
    def get(self, request, quiz_id):
        quest = get_object_or_404(Quest, pk=quiz_id)
        first_question = Question().next_question(quest=quest)
        return render(request, 'quiz/quiz.html', {'quiz': quest, 'first_question': first_question})
