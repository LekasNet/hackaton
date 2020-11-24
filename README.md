# Документация #
### Разворачивание проекта: ###
```shell script
git clone https://github.com/LekasNet/hackaton.git
pip install -r requiremens.txt
python3 manage.py migrate
python3 manage.py runserver
```
БИНГО!!!

### Команда для создания суперпользователя ###
```
./manage.py createsuperuser 
```
### Для подключения связи с моделью пользователя используем ###
```
from django.conf import settings

class Course(models.Model):
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```