# Generated by Django 2.0.6 on 2018-07-25 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('def_first', models.CharField(max_length=300)),
                ('def_second', models.CharField(max_length=1500)),
                ('image_logo', models.FileField(blank=True, null=True, upload_to='')),
                ('image_first', models.FileField(blank=True, null=True, upload_to='')),
                ('image_second', models.FileField(blank=True, null=True, upload_to='')),
                ('gif', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
