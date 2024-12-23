from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.db.models.signals import post_save 

# Create your models here.
# creating user profile model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modiefied=models.DateTimeField(user, auto_now=True)
    phone=models.CharField(max_length=20, blank=True, null=True)
    department=models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
# create a user by default
def create_profile(sender, instance, created, **kwargs):
    if created:
        User_Profile=UserProfile(user=instance)
        User_Profile.save()
        #automate the creation of user profile 
post_save.connect(create_profile, sender=User)
        
        
    # crqs model
class CRQSData(models.Model):
    date= models.DateTimeField(default=timezone.now)
    week = models.CharField(max_length=100)
    batch_number = models.CharField(max_length=50)
    assessor = models.CharField(max_length=100, help_text="Person responsible for assessment")
    variant = models.CharField(max_length=50)
    sku = models.CharField(max_length=50, verbose_name="SKU", help_text="Stock Keeping Unit")
    issue_description = models.TextField(blank=True, null=True)
    number_of_samples = models.IntegerField()
    count_of_issues = models.IntegerField()
    score = models.CharField(max_length=100, help_text="Quality assessment score")
    temperature = models.CharField(max_length=50)
    speed = models.CharField(max_length=50)
    parameter = models.CharField(max_length=255, blank=True, null=True)
    property = models.CharField(max_length=50, help_text="Production property")
    issue = models.CharField(max_length=100, help_text="Specific issue identified")
    comment = models.TextField(blank=True, null=True, help_text="Additional comments")

    def __str__(self):
        return f"{self.date} - Batch {self.batch_number} - Assessor: {self.assessor}"
    
    
    # packing model
class PackingData(models.Model):
    date=models.DateTimeField(default=timezone.now)
    week = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, verbose_name="SKU", help_text="Stock Keeping Unit")
    target=models.CharField(max_length=50)                           
    achieved=models.CharField(max_length=50)                            
    batch_number = models.CharField(max_length=50)                            
    variant = models.CharField(max_length=50)                            
    comment = models.TextField(blank=True, null=True, help_text="Additional comments")                            
    assessor = models.CharField(max_length=100, help_text="Person responsible for assessment") 
    
    def __str__(self):
        return f"{self.date} - Batch: {self.batch_number} - Assessor: {self.assessor}" 
    # production processing models
#    vimlemonke model
class VimLemonKe(models.Model):
    date = models.DateField(default=timezone.now, null=True)
    hash =models.FloatField(null=True)
    batch_number = models.CharField(null=True, max_length=20)
    start_time = models.CharField(null=True,max_length=20)
    stop_time = models.CharField(null=True,max_length=20)
    batch_time = models.CharField(null=True,max_length=20)
    whiting_quantity = models.FloatField(null=True)
    whiting_batch_number = models.CharField(null=True,max_length=20)
    magadi_quantity = models.FloatField(null=True)
    magadi_batch_number =models.CharField(null=True,max_length=20)
    tcca_quantity = models.FloatField(null=True)  # Trichloroisocyanuric Acid
    tcca_batch_number = models.CharField(max_length=20, null=True)
    lime_perf_quantity = models.FloatField(null=True)
    lime_perf_batch_number = models.CharField(max_length=20, null=True)
    sulphonic_acid_quantity = models.FloatField(null=True)
    sulphonic_acid_batch_number = models.CharField(max_length=20, null=True)
    batch_size = models.FloatField(null=True)
    pressure = models.FloatField(null=True)
    done_by =models.CharField(max_length=20, null=True)
    checked_by =models.CharField(max_length=20, null=True)
    verified_by =models.CharField(max_length=20, null=True)
    def __str__(self):
        return f"{self.date} - Batch: {self.batch_number} - Assessor: {self.done_by}" 
   
   
    # vimlavender model
class VimLavenderKe(models.Model):
    date = models.DateField(default=timezone.now, null=True)
    hash =models.FloatField(null=True)
    batch_number = models.CharField(null=True, max_length=20)
    start_time = models.CharField(null=True,max_length=20)
    stop_time = models.CharField(null=True,max_length=20)
    batch_time = models.CharField(null=True,max_length=20)
    whiting_quantity = models.FloatField(null=True)
    whiting_batch_number = models.CharField(null=True,max_length=20)
    magadi_quantity = models.FloatField(null=True)
    magadi_batch_number =models.CharField(null=True,max_length=20)
    tcca_quantity = models.FloatField(null=True)  # Trichloroisocyanuric Acid
    tcca_batch_number = models.CharField(max_length=20, null=True)
    sulphonic_acid_quantity = models.FloatField(null=True)
    sulphonic_acid_batch_number = models.CharField(max_length=20, null=True)
    katio_quantity = models.FloatField(null=True)
    katio_batch_number = models.CharField(max_length=20, null=True)
    batch_size = models.FloatField(null=True)
    pressure = models.FloatField(null=True)
    done_by =models.CharField(max_length=20, null=True)
    checked_by =models.CharField(max_length=20, null=True)
    verified_by =models.CharField(max_length=20, null=True)
    def __str__(self):
        return f"{self.date} - Batch: {self.batch_number} - Assessor: {self.done_by}" 
                                
                
