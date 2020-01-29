from django.contrib import admin

# Register your models here.
from core.models import Game, User

admin.site.register(Game)
admin.site.register(User)