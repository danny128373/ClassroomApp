import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from classroomapp.views import Connection
from classroomapp.models import Cohort


# def cohort_list(request):
#     if request.method == 'GET':
#         with sqlite3.connect(Connection.db_path) as conn:
