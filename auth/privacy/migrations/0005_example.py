# Generated by Django 4.1.3 on 2022-12-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('privacy', '0004_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('example', models.CharField(max_length=4)),
            ],
        ),
    ]