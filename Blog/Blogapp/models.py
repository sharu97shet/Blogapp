from django.db import models

#from django.contrib.auth.models import Group, User ,Permission

#from django.utils import timezone
# Create your models here.

class Bloguser(models.Model):
    #id=models.CharField(max_length=200)

    Name=models.CharField(max_length=200, null=False)

    Email=models.EmailField(max_length=200 , default='' )

    Password=models.CharField(max_length=10)

    class Meta:
        app_label = 'Blogapp'
    
   
    def __str__(self):
        return self.Name
    

class Blog(models.Model):
    class Meta:
        app_label = 'Blogapp'
    #id=models.CharField(max_length=200)

    BlogName = models.CharField(max_length=200, null=False)

    Image= models.ImageField(upload_to="media")

    Description=models.TextField()

    user=models.ForeignKey(Bloguser,default='',  on_delete=models.CASCADE)

    def __str__(self):   
        return self.BlogName   


class Blogdetails(models.Model):
    #id=models.CharField(max_length=200)

    BlogName = models.CharField(max_length=120, null=False)

    
    Description=models.TextField()    

    class Meta:
        app_label = 'Blogapp'  


# class Resume(models.Model):   
#     Name=models.CharField(max_length=32)
#     Resumedoc=models.FileField(upload_to='media')
#     Mobileno=models.CharField(max_length=32) 

#     class Meta:
#         app_label = 'Blogapp'   


# class Student(models.Model):  
#     Studentname=models.CharField(max_length=52)
#     createddate=models.DateTimeField(auto_now_add=True)
#     updatedate=models.DateTimeField(auto_now=True)

#     class Meta:
#         app_label = 'Blogapp'

# class Mark(models.Model):  
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)    
#     subject_id=models.IntegerField()
#     marks=models.IntegerField()

#     class Meta:
#         app_label = 'Blogapp'
     

# class Interest(models.Model): 
#     title=models.CharField(max_length=200) 

#     class Meta:
#         app_label = 'Blogapp'
    
#     def __str__(self):
#         return self.title
    

# class City(models.Model):
#        title=models.CharField(max_length=200)

#        class Meta:
#         app_label = 'Blogapp'

#        def __str__(self):
#         return self.title
       

# class Person(models.Model):
#     name=models.CharField(max_length=200)
#     mobile=models.CharField(max_length=20)
#     interests=models.ManyToManyField(Interest)

#     class Meta:
#         app_label = 'Blogapp'

#     def __str__(self):
#         return self.name


# class PersonAddress(models.Model):
#     person=models.OneToOneField(Person , on_delete=models.CASCADE)
#     city=models.ForeignKey(City,on_delete=models.CASCADE)
#     street_address=models.CharField(max_length=100)

#     class Meta:
#         app_label = 'Blogapp'

#     def __str__(self):
#         return self.person.name 
    




    

    