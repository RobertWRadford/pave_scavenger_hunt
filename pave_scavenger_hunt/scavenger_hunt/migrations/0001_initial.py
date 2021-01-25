# Generated by Django 3.1.5 on 2021-01-25 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the text you want to appear with the hyperlink.', max_length=200)),
                ('link', models.URLField(help_text='Enter the target URL.')),
            ],
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hint', models.CharField(help_text='Enter the text for the hint.', max_length=200)),
                ('helpfulness', models.CharField(blank=True, choices=[('s', 'subtle'), ('a', 'average'), ('b', 'big')], default='a', help_text='Hint helpfulness', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Optional. Enter descriptive text for the image', max_length=200)),
                ('link', models.URLField(help_text='Enter the target images hosted URL. Check the live site to make sure that the image was accessible.')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(help_text='Enter the address of the location.', max_length=200)),
                ('description', models.CharField(blank=True, help_text="Enter a description of the location and it's significance.", max_length=1600)),
                ('album', models.ManyToManyField(blank=True, to='scavenger_hunt.Image')),
            ],
        ),
        migrations.CreateModel(
            name='PaveMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the members name.', max_length=75)),
                ('link', models.URLField(blank=True, help_text='Enter the target images hosted URL. Check the live site to make sure that the image was accessible.')),
                ('bio', models.CharField(blank=True, help_text='Enter a short bio of the member.', max_length=1600)),
                ('email', models.EmailField(blank=True, help_text='Enter the members email for contact.', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.CharField(blank=True, help_text='Enter the introduction text for this question/riddle.', max_length=1600)),
                ('question', models.CharField(help_text='Enter the prompt for the question/riddle.', max_length=450)),
                ('answer', models.CharField(help_text='Enter the answer to the question/riddle.', max_length=200)),
                ('album', models.ManyToManyField(blank=True, to='scavenger_hunt.Image')),
                ('hints', models.ManyToManyField(blank=True, to='scavenger_hunt.Hint')),
            ],
            options={
                'ordering': ['question', 'answer'],
            },
        ),
        migrations.CreateModel(
            name='StartingInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scavenger_hunt.location')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.IntegerField(help_text='Enter the number for the question', unique=True)),
                ('directions', models.CharField(blank=True, help_text='Enter directions from the current location to the answer location.', max_length=1600)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scavenger_hunt.location')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scavenger_hunt.question')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('questions_completed', models.ManyToManyField(blank=True, to='scavenger_hunt.QuestionInstance')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
