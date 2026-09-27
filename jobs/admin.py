from django.contrib import admin
from .models import Job, Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'company',
        'location',
        'category',
        'salary',
        'posted_date'
    )

    search_fields = (
        'title',
        'company',
        'location'
    )

    list_filter = (
        'category',
        'location'
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'job',
        'applicant',
        'status',
        'applied_date'
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'applicant__username',
        'job__title'
    )