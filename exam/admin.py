from django.contrib import admin

from models import Group,Subject,Student,StudentExam,Question,Isoption,Exam


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    last_display = ('name')



@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    last_display = ('name','group')




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    last_display = ('first_name','last_name','email','group')




@admin.register(StudentExam)
class StudentExamAdmin(admin.ModelAdmin):
    last_display = ('exam','student')



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    last_display = ('name','exam')




@admin.register(Isoption)
class IsoptionAdmin(admin.ModelAdmin):
    last_display = ('name','question')

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    last_display = ('name')
