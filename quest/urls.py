from django.urls import path
from django.contrib.auth.decorators import login_required
from quest.views import ActiveQuestView, QuestView, QuestionView, QuestEndView, MyStatView


urlpatterns = [

    path('quest/<int:quest_id>/quest_end', login_required(QuestEndView.as_view()), name='quest_end'),
    path('quest/<int:quest_id>/<int:question_id>', login_required(QuestionView.as_view()), name='question_url'),
    path('quest/<int:quest_id>', login_required(QuestView.as_view()), name='quest_url'),
    path('', login_required(ActiveQuestView.as_view()), name='active_quests'),
    path('stat', login_required(MyStatView.as_view()), name='my_static')

]
