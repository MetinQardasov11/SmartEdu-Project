# Generated by Django 5.1.1 on 2024-10-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Course Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(default='courses/default_course_img.png', upload_to='courses/%Y/%m/%d', verbose_name='Image')),
                ('date', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
    ]