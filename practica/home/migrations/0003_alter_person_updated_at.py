# Generated by Django 4.1.7 on 2023-03-09 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_person_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
