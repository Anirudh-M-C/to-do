# Generated by Django 3.2.25 on 2024-04-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('priority', models.IntegerField()),
                ('project', models.CharField(max_length=200)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]