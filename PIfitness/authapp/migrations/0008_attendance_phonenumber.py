# Generated by Django 5.0 on 2024-02-23 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='phonenumber',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
