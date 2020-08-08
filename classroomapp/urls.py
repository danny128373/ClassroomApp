from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'classroomapp'

urlpatterns = [
    path('', home),
    path('cohorts/', cohort_list, name='cohorts'),
]
