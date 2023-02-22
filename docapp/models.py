from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings


# Create your models here.


class CustomUser(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    generated_code = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.generated_code


class Tutorials(models.Model):
    tutorial_name = models.CharField(max_length=200)
    generated_code = models.CharField(max_length=50, null=False, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.tutorial_name


class Subjects(models.Model):
    subject_name = models.CharField(max_length=200)
    generated_code = models.CharField(max_length=50, unique=True, null=False)
    tutorial = models.ForeignKey(Tutorials, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name


class Contents(models.Model):
    content = RichTextField()
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
