# Generated by Django 2.2.2 on 2019-07-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidooit_people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
