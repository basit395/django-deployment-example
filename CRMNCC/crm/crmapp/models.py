
from django.db import models
import datetime
from datetime import timedelta
from datetime import date
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import  get_object_or_404
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

def defaultstatus():
    return operationstatus.objects.get(id=1)

def defaultstatusorder():
    return operationstatus.objects.get(id=4)

def defaulemployeetstatus():
    return employeestatus.objects.get(id=1)


def defaultdealcategory():
    return dealcategory.objects.get(id=1)

class customer(models.Model):
    creator = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='user_customers',verbose_name ='Creator')
    customername = models.CharField("Customer Name",max_length=100,null=True)
    cr = models.IntegerField(null = True,blank = True, unique=True)
    activity  = models.CharField(max_length=100,blank=True)
    no_of_employees = models.IntegerField(null = True,blank = True)
    branches = models.IntegerField(null = True,blank = True)
    district  = models.CharField(max_length = 100,blank = True)
    street  = models.CharField(max_length=100,blank=True)
    phone = models.IntegerField(null = True,blank = True)
    email = models.EmailField(null = True,blank = True)
    current_services = models.CharField(max_length=1000,blank=True)
    notes = models.CharField(max_length=1000,blank=True)
    creationdate = models.DateTimeField("Creation Date",auto_now_add=True)
    updatedate = models.DateTimeField("Update Date",auto_now=True)

    def __str__(self):
        return self.customername

    def get_absolute_url(self):
        return reverse('customerdetail',kwargs={'pk':self.pk})

class suggestion(models.Model):
    requestor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_requests')
    requesttext = models.CharField("Request",max_length=100,null=True,unique=True)
    completion = models.BooleanField(default=False)
    creationdate = models.DateTimeField("Creation Date",auto_now_add=True)
    updatedate = models.DateTimeField("Update Date",auto_now=True)

    class Meta:
        verbose_name ='Suggesion'
        verbose_name_plural ='Suggestions'

    def __str__(self):
        return self.requesttext

    def get_absolute_url(self):
        return reverse('suggestiondetail',kwargs={'pk':self.pk})



class servicecategory(models.Model):
    servicecategoryname = models.CharField("Service Category",max_length=100,null=True)

    class Meta:
        verbose_name ='Service Category'
        verbose_name_plural ='Service Categorys'

    def __str__(self):
        return self.servicecategoryname

class dealcategory(models.Model):
    dealcategoryname = models.CharField("Deal Category Name",max_length=100,null=True)

    class Meta:
        verbose_name ='Deal Category'
        verbose_name_plural ='Deal Categorys'

    def __str__(self):
        return self.dealcategoryname

class service(models.Model):
    servicename = models.CharField("Service",max_length=100,null=True)
    servicecategory = models.ForeignKey(servicecategory,blank=True,on_delete=models.CASCADE,related_name='category_services',verbose_name ='Service Category')
    ncc_id = models.IntegerField(unique=True)
    catalogue_id = models.IntegerField(unique=True)
    nrc = models.IntegerField()
    mrc = models.IntegerField()
    commission = models.IntegerField()

    def get_absolute_url(self):
        return reverse('servicedetail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.servicename

class stcstatus(models.Model):
    stcstatusname = models.CharField("STC Status",max_length=100,null=True)

    class Meta:
        verbose_name ='STC Status'
        verbose_name_plural ='STC Status'


    def __str__(self):
        return self.stcstatusname

class leadsource(models.Model):
    leadsourcename = models.CharField("Lead Source",max_length=100,null=True)

    class Meta:
        verbose_name ='Lead Source'
        verbose_name_plural ='Lead Source'

    def __str__(self):
        return self.leadsourcename

class operationstatus(models.Model):
    operationstatusname = models.CharField("Operation_Status",max_length=100,null=True)

    class Meta:
        verbose_name ='Operation Status'
        verbose_name_plural ='Operation Status'

    def __str__(self):
        return self.operationstatusname

class employeestatus(models.Model):
    employeestatusname = models.CharField("Employee Status",max_length=100,null=True)

    class Meta:
        verbose_name ='Employee  Status'
        verbose_name_plural ='Employee Status'

    def __str__(self):
        return self.employeestatusname

class jobtitle(models.Model):
    jobtitlename = models.CharField("Job Title",max_length=100,null=True)

    class Meta:
        verbose_name ='Job Title'
        verbose_name_plural ='Job Titles'

    def __str__(self):
        return self.jobtitlename

class customercontactnumber(models.Model):
    customercontactnumbername = models.CharField("Customer Contact No",max_length=100,null=True)
    mobile1 = models.IntegerField(null = True,blank = True)
    mobile2 = models.IntegerField(null = True,blank = True)
    email = models.EmailField(null = True,blank = True)

    class Meta:
        verbose_name ='Customer Contact Number'
        verbose_name_plural ='Customer Contact Numbers'

    def __str__(self):
        return self.customercontactnumbername

class staff(models.Model):
    staffname = models.CharField("Name Of Staff",max_length=100,null=True,unique=True)
    staff_id = models.IntegerField("Staff_ID",unique=True)
    joindate = models.DateField("Join Date",null=True,blank=True)
    employeestatus = models.ForeignKey(employeestatus,blank=True,on_delete=models.CASCADE,related_name='employeestatus_staff',verbose_name ='Employee Status',default=defaulemployeetstatus)
    employeejobtitle = models.ForeignKey(jobtitle,blank=True,on_delete=models.CASCADE,related_name='jobtitle_staff',verbose_name ='Job Title')
    updatedate = models.DateTimeField("Update Date",auto_now=True)

    class Meta:
        verbose_name ='Staff'
        verbose_name_plural ='Staff'

    def __str__(self):
        return self.staffname

    def get_absolute_url(self):
        return reverse('staffdetail',kwargs={'pk':self.pk})

class opportunity(models.Model):
    lms = models.IntegerField("LMS No",unique=True)
    opportunityno = models.IntegerField("Opportunity No",unique=True)
    creationdate = models.DateTimeField("Creation Date",auto_now_add=True)
    salesman = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='salesman_opportunities',verbose_name ='Sales Man')
    employeejobtitle = models.CharField("Job Title",max_length=100,null=True) #def
    customer = models.ForeignKey(customer,blank=True,on_delete=models.CASCADE,related_name='customer_opportunities',verbose_name ='Customer')
    service = models.ForeignKey(service,blank=True,on_delete=models.CASCADE,related_name='service_opportunities',verbose_name ='Service')
    servicecategory = models.CharField("Service Category",max_length=100,null=True) #def
    status = models.ForeignKey(operationstatus,blank=True,on_delete=models.CASCADE,related_name='status_opportunities',verbose_name ='Status',null=True,default=defaultstatus)
    noofservices = models.IntegerField("No Of Services",default=1)
    updatedate = models.DateTimeField("Update Date",auto_now=True)
    authorized = models.CharField("Authorized Person",max_length=100,null=True,blank=True)
    totalnrc = models.IntegerField("Total NRC")
    totalmrc = models.IntegerField("Total MRC")
    coordinates = models.CharField("Coordinates",max_length=100,null=True,blank=True)

    class Meta:
        verbose_name ='Opportunity'
        verbose_name_plural ='Opportunitys'

    def __str__(self):
        return str(self.opportunityno)

    def save(self, *args, **kwargs):


         obj1 =  get_object_or_404(service,servicename = self.service)
         self.servicecategory = str(obj1.servicecategory)

         self.totalnrc = obj1.nrc * self.noofservices
         self.totalmrc = obj1.mrc * self.noofservices

         super(opportunity, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('opportunitydetail',kwargs={'pk':self.pk})
# Orders

class order(models.Model):
    dealcategory = (
            ('n', 'New'),
            ('u', 'Upgrade'),
            ('d', 'Downgrade'),
        )
    dealcategory = models.CharField("Deal Category",max_length=1, choices=dealcategory)
    opportunity = models.ForeignKey(opportunity,on_delete=models.CASCADE,related_name='opportunity_orders',verbose_name ='Opportunity')
    orderno= models.IntegerField("Order No",unique=True)
    creationdate = models.DateTimeField("Creation Date",auto_now_add=True)
    accountno = models.IntegerField("Account No")
    service = models.ForeignKey(service,blank=True,on_delete=models.CASCADE,related_name='service_orders',verbose_name ='Service')
    servicecategory = models.CharField("Service Category",max_length=100,null=True) #def
    status = models.ForeignKey(operationstatus,blank=True,on_delete=models.CASCADE,related_name='status_orders',verbose_name ='Status',null=True,default=defaultstatusorder)
    operationexecutive = models.ForeignKey(User,on_delete=models.CASCADE,related_name='executive_orders',verbose_name ='Operation Executive')
    nrc = models.IntegerField("NRC")
    mrc = models.IntegerField("MRC")
    updatedate = models.DateTimeField("Update Date",auto_now=True)
    activationdate = models.DateField("Activation Date",blank=True,null=True)
    cabinetno = models.CharField("Cabinet No",max_length=100,null=True)
    circuitno = models.CharField("Circuit No",max_length=100,null=True)


    class Meta:
        verbose_name ='Order'
        verbose_name_plural ='Orders'

    def save(self, *args, **kwargs):
         obj1 =  get_object_or_404(service,servicename = self.service)
         self.servicecategory = str(obj1.servicecategory)
         self.nrc = obj1.nrc
         self.mrc = obj1.mrc

         super(order, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('orderdetail',kwargs={'pk':self.pk})

# class deal(models.Model):
#     editor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_nazeel')
#     nazeelname = models.CharField("اسم النزيل",null = True,max_length=100)
#     nazeelnationalid = models.IntegerField("رقم الهوية",null = True)
#     nazeelid = models.IntegerField("رقم النزيل",null = True,unique=True)
#     nationality = models.ForeignKey(nationality,blank=True,on_delete=models.CASCADE,related_name='nationality_nazeel')
#     nationalitycat = models.CharField("نوع الجنسية",blank=True,null=True,max_length=20)
#     dateofbirth = models.DateField("تاريخ الميلاد")
#     age = models.IntegerField("العمر",null = True,blank=True)
#     status = models.ForeignKey(status,blank=True,null = True,on_delete=models.CASCADE,related_name='status_nazeel')
#     arrivalfrom = models.ForeignKey(arrivalfrom,blank=True,null = True,on_delete=models.CASCADE)
#     jail = models.ForeignKey(jail,blank=True,null=True,on_delete=models.CASCADE,related_name='jail_nazeel')
#     region = models.CharField(region,blank=True,null=True,max_length=100)
#     wing = models.ForeignKey(wing,blank=True,null = True,on_delete=models.CASCADE)
#     case = models.ForeignKey(case,blank=True,null=True,on_delete=models.CASCADE,related_name='case_nazeel')
#     casecatn = models.CharField("نوع القضية",blank=True,null=True,max_length=100)
#     entrydate = models.DateTimeField("تاريخ الدخول",auto_now_add=True)
#     exitdate = models.DateTimeField("تاريخ الخروج",null=True,blank=True)
#     sex = models.ForeignKey(sex,blank=True,null=True,on_delete=models.CASCADE)
#     statusnow= models.CharField("موقع النزيل",null = True,max_length=100,default='داخل السجن')
#     def save(self, *args, **kwargs):
#         obj =  get_object_or_404(jail,jailname = self.jail)
#         self.region = str(obj.region)
#
#         if str(self.nationality) == "سعودي":
#             self.nationalitycat = "سعودي"
#         else:
#             self.nationalitycat = "اجنبي"
#
#         self.age = int(datetime.datetime.today().strftime('%Y')) - int(self.dateofbirth.strftime('%Y'))
#
#         obj1 =  get_object_or_404(case,casename = self.case)
#         self.casecatn = str(obj1.casecat)
#
#         super(nazeel, self).save(*args, **kwargs)
#
#
#
#     def get_absolute_url(self):
#         return reverse('detail',kwargs={'pk':self.pk})
#
#
#
#
#     class Meta:
#         verbose_name ='اسم النزيل'
#         verbose_name_plural ='اسماء النزلاء'
#
#     def __str__(self):
#          return self.nazeelname
