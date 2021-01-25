from django.contrib import admin
from .models import ExternalLink, Image, Hint, Question, Location, StartingInstance, QuestionInstance, PaveMember, Profile
# Register your models here.

@admin.register(ExternalLink)
class ExternalLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('link',)

@admin.register(Hint)
class HintAdmin(admin.ModelAdmin):
    list_display = ('hint',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('address',)

@admin.register(StartingInstance)
class StartingInstanceAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(QuestionInstance)
class QuestionInstanceAdmin(admin.ModelAdmin):
    list_display = ('question_number', 'question')

@admin.register(PaveMember)
class PaveMemberAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__','getEmail','questionsCompleted')