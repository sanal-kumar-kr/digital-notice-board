# Generated by Django 4.2.5 on 2023-11-28 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='add_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=500)),
                ('date', models.DateField(null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('status', models.CharField(default='', max_length=500)),
                ('update_status', models.CharField(default='', max_length=50)),
                ('message', models.CharField(default='', max_length=500)),
                ('files', models.FileField(default='', upload_to='')),
                ('staffid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StatusClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_status', models.CharField(default='', max_length=50)),
                ('message', models.CharField(default='', max_length=500)),
                ('files', models.FileField(default='', upload_to='')),
                ('work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staffwork.add_work')),
            ],
        ),
    ]
