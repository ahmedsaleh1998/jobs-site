# Generated by Django 4.0.1 on 2022-02-09 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_apply_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='email',
            field=models.EmailField(max_length=60),
        ),
        migrations.AlterField(
            model_name='apply',
            name='linkedin',
            field=models.URLField(max_length=100),
        ),
    ]
