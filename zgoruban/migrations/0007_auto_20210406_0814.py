# Generated by Django 3.1.7 on 2021-04-06 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0006_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='paragraph',
            field=models.TextField(null=True),
        ),
    ]
