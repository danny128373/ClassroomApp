from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'classroomapp'

urlpatterns = [
    path('cohorts/', cohort_list, name='cohorts'),
    path('exercises/', exercise_list, name='cohorts'),
    path('students/', student_list, name='students'),
    path('instructors/', instructor_list, name='instructors'),
]
