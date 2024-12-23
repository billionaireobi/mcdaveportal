from django.db import models

# Create your models here.
# class Event(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     start = models.DateTimeField()
#     end = models.DateTimeField()
#     all_day = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
 
    class Meta:  
        db_table = "tblevents"