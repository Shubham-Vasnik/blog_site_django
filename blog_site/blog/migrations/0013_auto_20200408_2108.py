# Generated by Django 3.0.3 on 2020-04-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200408_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/default_profile_pic.jpg', null=True, upload_to='profile_pics'),
        ),
    ]
