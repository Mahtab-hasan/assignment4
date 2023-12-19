from django.db import models

class TaskCategory(models.Model):
    name  = models.CharField(max_length = 110)
    def __str__(self):
        return self.name
    
class Task(models.Model):
    taskTitle =models.CharField(max_length = 200)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default = False)
    taskAssignDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.taskTitle