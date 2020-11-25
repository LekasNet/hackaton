# Generated by Django 3.1.1 on 2020-11-25 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название викторины')),
                ('is_active', models.BooleanField(default=False, verbose_name='Викторина активна')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('cost', models.IntegerField(default=0, verbose_name='Стоимость вопроса')),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quest.quest')),
            ],
        ),
    ]
