from django.contrib import admin
from .models import Lecture

class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'lecturer_name', 'level', 'date')
    search_fields = ('title',)

admin.site.register(Lecture, LectureAdmin)