# Generated by Django 4.2.7 on 2023-12-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0015_alter_notes_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='notes',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
