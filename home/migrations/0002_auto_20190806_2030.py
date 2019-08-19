# Generated by Django 2.2.4 on 2019-08-07 01:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BathroomBreak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('type_of_bathroom', models.CharField(max_length=4)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bathroom_break', to='home.Dog')),
            ],
        ),
        migrations.DeleteModel(
            name='BathroomSession',
        ),
    ]