import sqlite3
from django.shortcuts import render
from classroomapp.models import Cohort
from ..connection import Connection


def student_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row

            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    s.id,
                    s.first,
                    s.last,
                    s.slack
                FROM classroomapp_student s
            """)

            all_students = db_cursor.fetchall()
            students_end_in_s = []
            students_end_without_s = []

            for student in all_students:
                if student[2].endswith('s'):
                    students_end_in_s.append(student)
                else:
                    students_end_without_s.append(student)

            template = 'students/list.html'

            context = {
                'students_end_in_s': students_end_in_s,
                'students_end_without_s': students_end_without_s
            }

            return render(request, template, context)
