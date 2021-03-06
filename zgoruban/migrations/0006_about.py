# Generated by Django 3.1.7 on 2021-04-06 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0005_auto_20210406_0234'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30, null=True)),
                ('paragraph', models.IntegerField(null=True)),
                ('image1', models.FileField(null=True, upload_to='')),
                ('image2', models.FileField(null=True, upload_to='')),
                ('image3', models.FileField(null=True, upload_to='')),
                ('image4', models.FileField(blank=True, null=True, upload_to='')),
                ('image5', models.FileField(blank=True, null=True, upload_to='')),
                ('image6', models.FileField(blank=True, null=True, upload_to='')),
                ('image7', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
