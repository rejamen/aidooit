# Generated by Django 2.2.3 on 2019-07-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidooit_people', '0003_personhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='personhistory',
            name='description',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
