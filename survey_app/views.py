from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Survey, Question, Answer, UserAnswerChoice


class IndexView(ListView):
    template_name = 'survey/index.html'
    context_object_name = 'latest_surveys_list'

    def get_queryset(self):
        """ 2 последних опроса"""
        return Survey.objects.order_by('-start_date')[:2]
