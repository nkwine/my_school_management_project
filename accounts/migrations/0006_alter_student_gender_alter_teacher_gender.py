# Generated by Django 4.2.7 on 2023-12-16 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_teacher_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('F', 'female'), ('M', 'male')], max_length=10),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.CharField(choices=[('F', 'female'), ('M', 'male')], max_length=10),
        ),
    ]
