from django.contrib import admin
from .models import(
    Inout,
    Student,
    Studententry
)

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['name','classs','division','rollno','mobile','macaddress','parentmobile','email']

@admin.register(Inout)
class InoutModelAdmin(admin.ModelAdmin):
    list_display=['classs','intime','outtime']

@admin.register(Studententry)
class StudententryModelAdmin(admin.ModelAdmin):
    list_display=['date','time','macadd']