from django.db import models

# Create your models here.

class language(models.Model):
    name = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class questionBank(models.Model):
    email = models.EmailField(null=True, default="guest@edutech.com")
    language = models.ForeignKey(language, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.email

class discipline(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class books(models.Model):
    name = models.CharField(max_length=300, null=True)
    author_name = models.CharField(max_length=100, null=True)
    discipline = models.ForeignKey(discipline, on_delete=models.CASCADE)
    link = models.URLField(null=True)

    def __str__(self):
        return self.name

class exam(models.Model):
    name = models.CharField(max_length=300, null=True)
    discipline = models.ForeignKey(discipline, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class course(models.Model):
    name = models.CharField(max_length=200, null=True)
    exam = models.ForeignKey(exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name