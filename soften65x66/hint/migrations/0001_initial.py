# Generated by Django 4.2.3 on 2023-07-22 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=12)),
                ('text', models.TextField()),
                ('no', models.IntegerField()),
            ],
        ),
    ]
