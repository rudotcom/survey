from django.contrib import admin
from .models import Survey, Question, Answer, UserAnswerChoice


class UserAnswerInline(admin.StackedInline):
    model = UserAnswerChoice
    extra = 1


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class SurveyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['survey_title']}
         ),
        ('Подробности',
         {'fields': ['description', 'finish_date'],
          'classes': ['collapse']}
         ),
    ]
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    fields = ['survey', 'question_text', 'question_type']
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    fields = ['AnswerText', 'AnswerText']
    inlines = [UserAnswerInline]


admin.site.register(Survey, SurveyAdmin)

admin.site.register(Question, QuestionAdmin)
