from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrateur'),
        ('TEACHER', 'Enseignant'),
        ('STUDENT', 'Étudiant'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='STUDENT')

class ClassRoom(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la classe")
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la matière")
    coefficient = models.IntegerField(default=1)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'TEACHER'}, related_name='subjects')
    
    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'STUDENT'}, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Note")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.subject.name}: {self.value}"