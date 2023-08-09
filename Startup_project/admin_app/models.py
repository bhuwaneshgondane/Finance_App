from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
    GENDER_CHOICES = [
        ('male','male'),
        ('female','female'),
        ('transgender','transgender')
    ]
    
    ROLE_CHOICES = [
        ('cs', 'customer'),
        ('lr', 'loan_representative'),
        ('oh', 'operational_head'),
        ('lo', 'loan_sanctioning_officer'),
        ('ad', 'admin'),
        ('ah', 'account_head')
    ]
    
    dob = models.DateField(blank=True, default='2000-12-12')
    gender = models.CharField(max_length=11, choices=GENDER_CHOICES)
    email = models.EmailField(db_index=True, max_length=50, unique=True)
    permanent_address = models.TextField()
    current_address = models.TextField()
    mobile = PhoneNumberField(region='IN')
    photo = models.ImageField(blank=True, upload_to='photo/')
    signature = models.ImageField(blank=True, upload_to='signature/')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active=models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name','last_name','mobile')
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        

class Family(models.Model):

    MARTIAL_STATUS_CHOICES = [('married','married'),('unmarried','unmarried'),('divorced','divorced')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='family')
    father_name = models.CharField(max_length=30, blank=True,default='')
    father_profeesion = models.CharField(max_length=30, blank=True, default='')
    father_income = models.FloatField(blank=True, default=0.0)
    father_contact = PhoneNumberField(region='IN', blank=True , null=True)
    mother_name = models.CharField(max_length=30, blank=True, default='')
    mother_profeesion = models.CharField(max_length=30, blank=True, default='')
    mother_income = models.FloatField(blank=True, default=0.0)
    mother_contact = PhoneNumberField(region='IN', blank=True , null=True)
    martial_status = models.CharField(max_length=20, default='unmarried', choices=MARTIAL_STATUS_CHOICES)
    spouse_name = models.CharField(max_length=30,default=0.0, blank=True)
    spouse_income = models.FloatField(blank=True, default=0.0)
    spouse_profeesion = models.CharField(max_length=30, blank=True, default='')
    spouce_contact = PhoneNumberField(region='IN', blank=True , null=True)

class Bank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='banks')
    bank_name = models.CharField(max_length=30, default='', blank=True, null=True)
    account_number = models.CharField(max_length=20, default='', blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, default='')
    passbook_copy = models.ImageField(upload_to='customer/bank/', blank=True, null=True)
    bank_address = models.TextField(blank=True, null=True)