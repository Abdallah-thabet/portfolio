# Generated by Django 3.1.1 on 2020-09-26 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20200926_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='description',
            field=models.TextField(default='No Description', max_length=300),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='description',
            field=models.TextField(default='No Description', max_length=300),
        ),
    ]
