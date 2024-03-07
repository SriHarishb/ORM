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