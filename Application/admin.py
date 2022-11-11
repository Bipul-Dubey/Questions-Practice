from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser
# Register your models here.

from .models import *
admin.site.register((McqTopic,Contact))
admin.site.register((SubjectiveTopic,SubjectiveQuestion,Question_Comment))


fields=list(UserAdmin.fieldsets)
fields[1]=('Personal Info',{'fields':('first_name','last_name','email','mobile_number','photo','date_of_birth','profession','address')})

UserAdmin.fieldsets=tuple(fields)
admin.site.register(NewUser,UserAdmin)

class OptionAdmin(admin.StackedInline):
    model=QuestionOption

class QuestionAdmin(admin.ModelAdmin):
    inlines=[OptionAdmin]

admin.site.register(McqQuestion,QuestionAdmin)
admin.site.register(QuestionOption)