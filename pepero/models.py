from django.db import models

# Create your models here.
class Pepero(models.Model):
    choco = models.TextField(verbose_name='초코코팅')
    syrop = models.TextField(verbose_name='시럽')
    deco = models.TextField(verbose_name='지불방식')
    content = models.TextField(verbose_name='편지 내용') 
    