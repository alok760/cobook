# Generated by Django 3.1.1 on 2020-12-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cowork',
            name='zipcode',
            field=models.PositiveIntegerField(default=None, help_text='Enter the number of room the Coworking space have'),
            preserve_default=False,
        ),
    ]
