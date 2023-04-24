from django.db import models

# Create your models here.
class Operator(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)


    def full_name(self):
        return f'{self.l_name}, {self.f_name}'


    def __str__(self) -> str:
        return self.full_name()


class Todo(models.Model):
    title = models.CharField(max_length=30)
    created_by = models.ForeignKey(Operator, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    description = models.TextField(max_length=255)
    is_urgent = models.BooleanField()
    slug = models.SlugField()


    class Meta:
        verbose_name_plural = 'Todo List Items'

    def __str__(self) -> str:
        return self.title