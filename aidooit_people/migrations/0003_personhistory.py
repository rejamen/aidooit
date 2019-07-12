# Generated by Django 2.2.3 on 2019-07-11 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aidooit_people', '0002_person_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aidooit_people.Person')),
            ],
        ),
    ]