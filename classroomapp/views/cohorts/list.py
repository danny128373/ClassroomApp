import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from classroomapp.views import Connection
from classroomapp.models import Cohort


def cohort_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row

            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT 
                    c.id,
                    c.name
                FROM classroomapp_cohort c 
            """)

            all_cohorts = db_cursor.fetchall()

            template = 'cohorts/list.html'

            context = {
                'all_cohorts': all_cohorts
            }

            return render(request, template, context)
