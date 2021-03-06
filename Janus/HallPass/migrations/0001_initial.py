# Generated by Django 2.1.4 on 2018-12-28 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassroomLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_ID', models.IntegerField()),
                ('Leave_Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ClassroomReturn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_ID', models.IntegerField()),
                ('Return_Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_ID', models.IntegerField()),
                ('Student_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_ID', models.IntegerField()),
                ('Leave_Time', models.DateTimeField()),
                ('Return_Time', models.DateTimeField()),
            ],
        ),
    ]
