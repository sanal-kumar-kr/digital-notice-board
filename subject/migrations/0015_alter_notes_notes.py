# Generated by Django 4.2.7 on 2023-12-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0014_alter_notes_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='notes',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
