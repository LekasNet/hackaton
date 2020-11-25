from django.urls import path
from django.contrib.auth.decorators import login_required
from quest.views import ActiveQuestView, QuestView


urlpatterns = [

    path('quest/<int:quest_id>', login_required(QuestView.as_view()), name='quest_url'),
    path('', login_required(ActiveQuestView.as_view()), name='active_quests'),

]