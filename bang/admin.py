from django.contrib import admin
from .models import Member, Board, Comment, Champion, Skill, Rune, Vote
# Register your models here.

admin.site.register(Member)
admin.site.register(Board)
admin.site.register(Comment)
admin.site.register(Champion)
admin.site.register(Vote)
admin.site.register(Skill)
admin.site.register(Rune)