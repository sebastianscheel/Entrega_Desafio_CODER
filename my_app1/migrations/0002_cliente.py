# Generated by Django 4.1.2 on 2022-10-31 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=40)),
                ('phone_namber', models.IntegerField()),
                ('email', models.CharField(max_length=35)),
                ('company', models.CharField(max_length=35)),
            ],
        ),
    ]
