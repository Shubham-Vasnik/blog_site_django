# Generated by Django 3.0.3 on 2020-04-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200408_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/default_profile_pic.jpg', upload_to='profile_pics'),
        ),
    ]
