# Generated by Django 4.2.1 on 2023-05-23 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='colors',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
