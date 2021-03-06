# Generated by Django 3.2.7 on 2021-09-20 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0043_auto_20210712_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year_categoryss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='category',
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='tags',
        ),
        migrations.AddField(
            model_name='gallery',
            name='image2',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='Heading',
            field=models.TextField(max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='GALLERYS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='')),
                ('years', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zgoruban.year_categoryss')),
            ],
        ),
    ]
