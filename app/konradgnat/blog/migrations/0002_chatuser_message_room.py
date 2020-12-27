# Generated by Django 3.1.4 on 2020-12-23 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=250, unique=True)),
                ('pub_date', models.DateField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.chatuser')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=200, unique=True)),
                ('messages', models.ManyToManyField(to='blog.Message')),
                ('users', models.ManyToManyField(to='blog.ChatUser')),
            ],
        ),
    ]
