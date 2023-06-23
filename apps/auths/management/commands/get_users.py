# Python
from typing import Any

# Django
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args: Any, **kwargs: Any) -> None:
        try:
            User.objects.create_superuser(
                username='root2',
                email='root2@mail.cc',
                password='bc83cg378cg3c',
                first_name='Иван',
                last_name='Темнохолмов'
            )
            print('Админ успешно создан')
        except Exception as e:
            print(e)
            print('Админ успешно не создан')