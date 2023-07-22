from django.db import models

class Hint(models.Model):
    student_id = models.CharField(max_length=12)
    text = models.TextField()
    no = models.IntegerField()

    def __str__(self):
        return f'{self.no}_{self.student_id}'
