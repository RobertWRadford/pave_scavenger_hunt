from django.contrib import admin
from .models import Image, ExternalLink, Hint, OpenQuestion, ChoiceQuestion, Location, StartingInstance, CampusQuestionInstance, AnnArborQuestionInstance, PaveMember, Profile, ExtraPageAbout
# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ExternalLink)
class ExternalLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link',)

@admin.register(Hint)
class HintAdmin(admin.ModelAdmin):
    list_display = ('hint',)

@admin.register(OpenQuestion)
class OpenQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer',)

@admin.register(ChoiceQuestion)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'correctAnswer',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('address',)

@admin.register(StartingInstance)
class StartingInstanceAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(CampusQuestionInstance)
class QuestionInstanceAdmin(admin.ModelAdmin):
    list_display = ('question_number', 'question')

@admin.register(AnnArborQuestionInstance)
class QuestionInstanceAdmin(admin.ModelAdmin):
    list_display = ('question_number', 'question')

@admin.register(PaveMember)
class PaveMemberAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__','getEmail','aaQuestionsCompleted','campusQuestionsCompleted')

@admin.register(ExtraPageAbout)
class ExtraPageAboutAdmin(admin.ModelAdmin):
	list_display = ('__str__',)