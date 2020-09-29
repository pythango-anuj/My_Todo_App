from django.db import models

status_list = (
    ('Yet To Start','Yet To Start'),
    ('In Progess','In Progress'),
    ('In Review','In Review'),
    ('Completed','Completed'),
)

priority_list = (
    ('Low','Low'),
    ('Intermediate','Intermediate'),
    ('High','High'),
)
# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=250)
    end_date = models.CharField(max_length=20)
    status = models.CharField(max_length=100,choices=status_list)
    priority = models.CharField(max_length=100,choices=priority_list)
    assignees = models.CharField(max_length=250)
    
    def __str__(self):
        return self.task_name

