# Ex02 Django ORM Web Application

## Date: 01/03/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![alt text](<Concept map.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

from django.db import models
from django.contrib import admin 
class book(models.Model):
	bookno=models.IntegerField(primary_key=True);
	bname=models.CharField(max_length=100);
	bauthor=models.CharField(max_length=100);
	yop=models.DateField();
	aemail=models.EmailField();
	bcat=models.CharField(max_length=100);
class bookAdmin(admin.ModelAdmin):
	list_display=("bookno","bname","bauthor","yop","aemail","bcat");
```

```
admin.py

from django.contrib import admin
from .models import book,bookAdmin
admin.site.register(book,bookAdmin)
```

## OUTPUT

![alt text](<django admin - books added.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully