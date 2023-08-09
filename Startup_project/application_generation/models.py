from django.db import models
from admin_app.models import User
# Create your models here.

class Application(models.Model):

    EMPLOYMENT_CHOICE = [
            ("Salaried", "Salaried"),("Self-Employed","Self-Employed")
    ]

    BUSINESS_TYPE = [
            ("Service","Service"), ("Manufacturing", "Manufacturing"), ("Treders","Trederd"), ("Other","Other")
    ]

    APPLICATION_STATUS = [
            ("Pending","Pending"), ("Apporve","Apporve"), ("Rejected","Rejected"), ("Disbursed","Disbursed")
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Applications")
    aaddar_no = models.CharField(max_length=12, default=0, blank=True)
    pan_no = models.CharField(max_length=10, default=0, blank=True)
    type_of_employment = models.CharField(max_length=250, choices=EMPLOYMENT_CHOICE, default=0, blank=True)
    business_title = models.CharField(max_length=250, default=0, blank=True)
    business_type = models.CharField(max_length=250, choices=BUSINESS_TYPE, default=0, blank=True)
    business_address = models.TextField(default=0, blank=True)
    gst_registration_no = models.CharField(max_length=50, default=0, blank=True)
    business_license_no = models.CharField(max_length=50, default=0, blank=True)
    expected_average_annual_turnover = models.CharField(max_length=250, default=0, blank=True)
    years_in_current_business = models.IntegerField(default=0, blank=True)
    collateral = models.CharField(max_length=250, default=0, blank=True)
    status = models.CharField(max_length=250, default='', choices=APPLICATION_STATUS)
    application_timestamp = models.DateTimeField(blank=True)
    remark = models.CharField(max_length=250, default=0, blank=True)

    def __str__(self):
        	return f"{self.id}"



class Guarantor(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T','Transgender')
    )

    STATE_CHOICES = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),
                     ("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),
                     ("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),
                     ("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),
                     ("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),
                     ("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),
                     ("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),
                     ("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),
                     ("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),
                     ("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),
                     ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),
                     ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),
                     ("Lakshadweep","Lakshadweep"),
                     ("National Capital Territory of Delhi","National Capital Territory of Delhi"),
                     ("Puducherry","Puducherry"))

    application=models.ForeignKey(Application,on_delete=models.CASCADE,related_name='Gaurantors')
    relation_with_customer=models.CharField(max_length=250,default=0,blank=True)
    name=models.CharField(max_length=150,default=0,blank=True)
    dob=models.DateField(default='2000-12-12',blank=True)
    gender=models.CharField(max_length=50,default=0,blank=True,choices=GENDER_CHOICES)
    email=models.EmailField(default=0,blank=True)
    address=models.TextField(max_length=250,default=0,blank=True)
    city=models.CharField(max_length=50,default=0,blank=True)
    state=models.CharField(max_length=100,default=0,blank=True,choices=STATE_CHOICES)
    country=models.CharField(max_length=100,default=0,blank=True)
    pin_code=models.IntegerField(default=0,blank=True)
    mobile=models.CharField(max_length=10,default=0,blank=True)
    photo=models.ImageField(upload_to='media/customer/guarantor/',default=0,blank=True)
    profession=models.CharField(max_length=250,default=0,blank=True)
    income_certificate=models.FileField(upload_to='media/customer/guarantor/',default=0,blank=True)
    bank_name=models.CharField(max_length=250,default=0,blank=True)
    current_account_no=models.CharField(max_length=20,default=0,blank=True)
    passbook_copy=models.FileField(upload_to='media/customer/guarantor/',default=0,blank=True)
    ifsc_code=models.CharField(max_length=20,default=0,blank=True)


    def __str__(self):
        return f'{self.id}'
    

class Document(models.Model):
    DOCUMENT_STATUS_CHOICE = [
        ('','',),
        ('pending','pending'),
        ('done','done'),
        ('rejected','rejected'),
    
    ]
    application = models.OneToOneField(Application, on_delete=models.CASCADE, realated_name='documents')
    aadhar_card = models.FileField(upload_to='customer/document',default=0,blank=True)
    pan_card = models.FileField(upload_to='customer/document',default=0,blank=True)
    business_address_proff_or_copy_of_rent_agreement = models.FileField(upload_to='customer/document',default=0,blank=True)
    electricity_bill = models.FileField(upload_to='customer/document',default=0,blank=True)
    msme_certificate = models.FileField(upload_to='customer/document',default=0,blank=True)
    gst_cerificate = models.FileField(upload_to='customer/document',default=0,blank=True)
    udhyog_adhar_registration =models.FileField(upload_to='customer/document',default=0,blank=True)
    business_lincense = models.FileField(upload_to='customer/document',default=0,blank=True)
    business_plan_or_proposal =models.FileField(upload_to='customer/document',default=0,blank=True)
    three_year_itr_with_balance_sheet = models.FileField(upload_to='customer/document',default=0,blank=True)
    collateral_document = models.FileField(upload_to='customer/document',default=0,blank=True)
    stamp_duty = models.FileField(upload_to='customer/document',default=0,blank=True)
    status = models.CharField(max_length=250,choices=DOCUMENT_STATUS_CHOICE,default=0,blank=True)
    response_timestamp = models.DateTimeField(auto_now=True,blank=True)
    remark = models.CharField(max_length=250,choices=DOCUMENT_STATUS_CHOICE,default=0,blank=True)

    def __str__(self):
        return f'{self.id}'