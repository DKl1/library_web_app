# Generated by Django 4.1 on 2023-02-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(blank=True, max_length=20)),
                ('surname', models.CharField(blank=True, max_length=20)),
                ('patronymic', models.CharField(blank=True, max_length=20)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]