from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=200, help_text='Optional. Enter descriptive text for the image', default='Image')
    link = models.URLField(max_length=200, help_text='Enter the target images hosted URL. Check the live site to make sure that the image was accessible.')

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title}'

class ExternalLink(models.Model):

    name = models.CharField(max_length=200, help_text='Enter the text you want to appear with the hyperlink.')
    link = models.URLField(max_length=200, help_text='Enter the target URL.')
    photo = models.URLField(max_length=200, help_text='Enter the target images hosted URL. Check the live site to make sure that the image was accessible.', blank=True)
    description = models.TextField(help_text='Enter a description of the location.', blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'

class Hint(models.Model):
    hint = models.TextField(help_text='Enter the text for the hint.')

    strengths = (('s', 'subtle'), ('a', 'average'), ('b', 'big'),)

    helpfulness = models.CharField(
        max_length=1,
        choices=strengths,
        blank=True,
        default='a',
        help_text='Hint helpfulness',
    )

    def full_helpfullness(self):
        return {'s': 'subtle', 'a': 'average', 'b': 'big'}[self.helpfulness]

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.hint}'

class OpenQuestion(models.Model):

    intro = models.TextField(help_text='Enter the introduction text for this question/riddle.', blank=True)
    album = models.ManyToManyField(Image, blank=True)
    question = models.TextField(help_text='Enter the prompt for the question/riddle.')
    hints = models.ManyToManyField(Hint, blank=True)
    answer = models.CharField(max_length=200, help_text='Enter the answer to the question/riddle.')

    class Meta:
        ordering = ['question', 'answer']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.question}'

class ChoiceQuestion(models.Model):

    intro = models.TextField(help_text='Enter the introduction text for this question/riddle.', blank=True)
    album = models.ManyToManyField(Image, blank=True)
    question = models.TextField(help_text='Enter the prompt for the question/riddle.')
    hints = models.ManyToManyField(Hint, blank=True)
    answerOne = models.CharField(max_length=200, help_text='Enter the first answer choice for the question/riddle.')
    answerTwo = models.CharField(max_length=200, help_text='Enter the second answer choice for the question/riddle.')
    answerThree = models.CharField(max_length=200, help_text='Enter the third answer choice for the question/riddle.')
    answerFour = models.CharField(max_length=200, help_text='Enter the fourth answer choice for the question/riddle.')
    correctAnswer = models.CharField(max_length=200, help_text='Enter the answer to the question/riddle.')

    class Meta:
        ordering = ['question', 'correctAnswer']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.question}'

class Location(models.Model):

    address = models.CharField(max_length=200, help_text='Enter the address of the location.')
    description = models.TextField(help_text='Enter a description of the location and it\'s significance.', blank=True)
    album = models.ManyToManyField(Image, blank=True)
    link = models.URLField(max_length=200, help_text='Enter the target URL.', blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.address}'

class AnnArborStartingInstance(models.Model):

    location = models.OneToOneField('Location', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.location.address}'

class CampusStartingInstance(models.Model):

    location = models.OneToOneField('Location', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.location.address}'

class CampusQuestionInstance(models.Model):

    question_number = models.IntegerField(help_text='Enter the number for the question', unique=True)
    openQuestion = models.ForeignKey('OpenQuestion', on_delete=models.CASCADE, blank=True)
    choiceQuestion = models.ForeignKey('ChoiceQuestion', on_delete=models.CASCADE, blank=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    directions = models.TextField(help_text='Enter directions from the current location to the answer location.', blank=True)

    def resolveType(self):
        return self.openQuestion if self.openQuestion else self.choiceQuestion
    
    def question(self):
        return self.resolveType().question
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.question_number}.) {self.question()}'

class AnnArborQuestionInstance(models.Model):

    question_number = models.IntegerField(help_text='Enter the number for the question', unique=True)
    openQuestion = models.ForeignKey('OpenQuestion', on_delete=models.CASCADE, blank=True)
    choiceQuestion = models.ForeignKey('ChoiceQuestion', on_delete=models.CASCADE, blank=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    directions = models.TextField(help_text='Enter directions from the current location to the answer location.', blank=True)

    def resolveType(self):
        return self.openQuestion if self.openQuestion else self.choiceQuestion
    
    def question(self):
        return self.resolveType().question
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.question_number}.) {self.question()}'

class PaveMember(models.Model):

    name = models.CharField(max_length=75, help_text='Enter the members name.')
    link = models.URLField(max_length=200, help_text='Enter the target images hosted URL. Check the live site to make sure that the image was accessible.', blank=True)
    bio = models.TextField(help_text='Enter a short bio of the member.', blank=True)
    email = models.EmailField(max_length=254, help_text='Enter the members email for contact.', blank=True)

    def __str__(self):
        return f'{self.name}'

class ExtraPageAbout(models.Model):

    description = models.TextField(help_text='Enter the description block for the extras page', default='No additional information')

    def __str__(self):
        return f'{self.description[:25]}...'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    aa_questions_completed = models.ManyToManyField(AnnArborQuestionInstance, blank=True)
    campus_questions_completed = models.ManyToManyField(CampusQuestionInstance, blank=True)

    def __str__(self):
        return f'{self.user.username}'

    def getEmail(self):
        return f'{self.user.email}'

    def aaQuestionsCompleted(self):
        return f'{self.aa_questions_completed.all().count()}'

    def campusQuestionsCompleted(self):
        return f'{self.campus_questions_completed.all().count()}'

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()