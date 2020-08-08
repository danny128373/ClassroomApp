import sqlite3
from django.shortcuts import render
from ..connection import Connection


def exercise_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row

            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT 
                    e.id,
                    e.name,
                    e.language
                FROM classroomapp_exercise e
            """)

            all_exercises = db_cursor.fetchall()

            template = 'exercises/list.html'

            context = {
                'all_exercises': all_exercises
            }

            return render(request, template, context)
