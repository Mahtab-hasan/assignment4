from django.db import models

class TaskCategory(models.Model):
    categoryName  = models.CharField(max_length = 110)
    def __str__(self):
        return self.categoryName