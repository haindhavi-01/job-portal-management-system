from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer


def home(request):
    return render(request, 'jobs/home.html')


class JobViewSet(viewsets.ModelViewSet):

    queryset = Job.objects.all().order_by('-posted_date')

    serializer_class = JobSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]

    filterset_fields = [
        'location',
        'category',
        'company'
    ]

    search_fields = [
        'title',
        'company',
        'location',
        'category',
        'description'
    ]


class ApplicationViewSet(viewsets.ModelViewSet):

    queryset = Application.objects.all().order_by('-applied_date')

    serializer_class = ApplicationSerializer