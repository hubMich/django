from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','question_text','pub_data','was_published_recently']
    search_fields = ['question_text']
admin.site.register(Question,QuestionAdmin)
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass