# Generated by Django 3.1.5 on 2021-01-27 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scavenger_hunt', '0003_auto_20210126_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraPageAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='No additional information', help_text='Enter the description block for the extras page')),
            ],
        ),
    ]
