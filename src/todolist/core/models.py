# from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """"""


def main(g: int) -> int:
    print(g)
    return g + 2
