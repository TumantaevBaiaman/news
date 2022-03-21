from django.contrib import admin
from .models import (
    Post,
    We,
    Option,
    Grade,
)

admin.site.register(Post)
admin.site.register(Option)
admin.site.register(Grade)
admin.site.register(We)

