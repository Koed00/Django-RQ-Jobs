# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin

from .models import Job, task_list

class JobForm(forms.ModelForm):
    task = forms.ChoiceField(choices=task_list())

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Job
        fields = '__all__'

class ScheduleAdmin(admin.ModelAdmin):
    form = JobForm
    list_display = (
        u'id',
        'task',
        'schedule_type',
        'repeats',
        'last_run',
        'next_run',
        'rq_link',
        'rq_status'
    )
    list_filter = ('last_run', 'next_run', 'schedule_type')
    list_display_links = ('id', 'task')
admin.site.register(Job, ScheduleAdmin)
