from django.db import models

# Create your models here.
class SummerCamp(models.Model):
    student_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    game_name = models.CharField(max_length=100)
    marks = models.IntegerField(blank=True, default=0)

    class Meta:
        db_table = 'summer_camp'
        verbose_name_plural = 'Summer Camp'

    def __str__(self):
        return self.student_name
