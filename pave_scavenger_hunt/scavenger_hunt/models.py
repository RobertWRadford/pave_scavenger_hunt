from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class ExternalLink(models.Model):

    name = models.CharField(max_length=200, help_text='Enter the text you want to appear with the hyperlink.')
    link = models.URLField(max_length=200, help_text='Enter the target URL.')
    description = models.CharField(max_length=2400, help_text='Enter a description of the location.', blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'

class Image(models.Model):
    title = models.CharField(max_length=200, help_text='Optional. Enter descriptive text for the image', default='Image')
    link = models.URLField(max_length=200, help_text='Enter the target images hosted URL. Check the live site to make sure that the image was accessible.')

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title}'

class Hint(models.Model):
    hint = models.CharField(max_length=200, help_text='Enter the text for the hint.')

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

class Question(models.Model):

    intro = models.CharField(max_length=2400, help_text='Enter the introduction text for this question/riddle.', blank=True)
    album = models.ManyToManyField(Image, blank=True)
    question = models.CharField(max_length=1200, help_text='Enter the prompt for the question/riddle.')
    hints = models.ManyToManyField(Hint, blank=True)
    answer = models.CharField(max_length=200, help_text='Enter the answer to the question/riddle.')

    class Meta:
        ordering = ['question', 'answer']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.question}'

class Location(models.Model):

    address = models.CharField(max_length=200, help_text='Enter the address of the location.')
    description = models.CharField(max_length=1600, help_text='Enter a description of the location and it\'s significance.', blank=True)
    album = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.address}'

class StartingInstance(models.Model):

    location = models.OneToOneField('Location', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.location.address}'

class QuestionInstance(models.Model):

    question_number = models.IntegerField(help_text='Enter the number for the question', unique=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    directions = models.CharField(max_length=2400, help_text='Enter directions from the current location to the answer location.', blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.question_number}.) {self.question.question}'

class PaveMember(models.Model):

    name = models.CharField(max_length=75, help_text='Enter the members name.')
    link = models.URLField(max_length=200, help_text='Enter the target images hosted URL. Check the live site to make sure that the image was accessible.', blank=True)
    bio = models.CharField(max_length=2400, help_text='Enter a short bio of the member.', blank=True)
    email = models.EmailField(max_length=254, help_text='Enter the members email for contact.', blank=True)

    def __str__(self):
        return f'{self.name}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    questions_completed = models.ManyToManyField(QuestionInstance, blank=True)

    def __str__(self):
        return f'{self.user.username}'

    def getEmail(self):
        return f'{self.user.email}'

    def questionsCompleted(self):
        return f'{self.questions_completed.all().count()}'

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()