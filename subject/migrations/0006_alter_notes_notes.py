# Generated by Django 4.2.5 on 2023-11-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0005_notes_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='notes',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
