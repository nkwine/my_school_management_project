# Generated by Django 4.2.7 on 2023-12-16 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_image_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='date_birth',
            field=models.DateField(),
        ),
    ]
