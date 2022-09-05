from turtle import title
from catigory.models import Catigory
import django_filters
from job.models import Job

class JobFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['category','title','location','job_type','description']