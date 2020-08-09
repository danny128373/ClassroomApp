import sqlite3
from django.shortcuts import render
from ..connection import Connection


def instructor_list(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                i.id,
                i.first,
                i.last,
                i.slack,
                i.specialty
            FROM classroomapp_instructor i
        """)

        all_instructors = db_cursor.fetchall()

        template = 'instructors/list.html'

        context = {
            'all_instructors': all_instructors
        }

        return render(request, template, context)
