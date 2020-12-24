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
    fields = ['survey_title', 'description', 'finish_date']
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    fields = ['survey', 'question_text', 'question_type']
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    fields = ['AnswerText']
    inlines = [UserAnswerInline]


class UserAnswerAdmin(admin.ModelAdmin):
    fields = ['AnswerText']


admin.site.register(Survey, SurveyAdmin)

admin.site.register(Question, QuestionAdmin)
