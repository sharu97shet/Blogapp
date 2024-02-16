from django.contrib import admin

# Register your models here.

from .models import*
# Register your models here.

admin.site.register(Bloguser)
    
admin.site.register(Blog)
admin.site.register(Blogdetails)

# admin.site.register(Resume)

# admin.site.register(Student)

# admin.site.register(Mark)

# admin.site.register([Person,PersonAddress,City,Interest])