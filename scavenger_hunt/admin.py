from django.contrib import admin
from .models import Image, HomePageContent, CampusExternalLink, AnnArborExternalLink, Hint, OpenQuestion, ChoiceQuestion, Location, AnnArborStartingInstance, CampusStartingInstance, CampusQuestionInstance, AnnArborQuestionInstance, PaveMember, Profile, ExtraPageAbout, AnnArborConclusion, CampusConclusion
# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(CampusExternalLink)
class CampusExternalLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link',)

@admin.register(AnnArborExternalLink)
class AnnArborExternalLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link',)

@admin.register(Hint)
class HintAdmin(admin.ModelAdmin):
    list_display = ('hint',)

@admin.register(OpenQuestion)
class OpenQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer',)

@admin.register(ChoiceQuestion)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('address',)

@admin.register(AnnArborStartingInstance)
class AnnArborStartingInstanceAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(CampusStartingInstance)
class CampusStartingInstanceAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(CampusQuestionInstance)
class CampusQuestionInstanceAdmin(admin.ModelAdmin):
    list_display = ('question_number', 'question')

@admin.register(AnnArborQuestionInstance)
class AnnArborQuestionInstanceAdmin(admin.ModelAdmin):
    list_display = ('question_number', 'question')

@admin.register(CampusConclusion)
class CampusConclusionAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(AnnArborConclusion)
class AnnArborConclusionAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(PaveMember)
class PaveMemberAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__','getEmail','aaQuestionsCompleted','campusQuestionsCompleted')

@admin.register(ExtraPageAbout)
class ExtraPageAboutAdmin(admin.ModelAdmin):
	list_display = ('__str__',)


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('__str__',)