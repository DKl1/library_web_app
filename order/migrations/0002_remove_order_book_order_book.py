# Generated by Django 4.1.7 on 2023-04-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_image'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='book',
        ),
        migrations.AddField(
            model_name='order',
            name='book',
            field=models.ManyToManyField(related_name='orders', to='book.book'),
        ),
    ]
