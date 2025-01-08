from django.contrib import admin
from .models import Student, Question, QuestionOption


admin.site.register([Student, Question, QuestionOption])