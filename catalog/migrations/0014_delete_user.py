# Generated by Django 4.1.6 on 2023-05-08 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_book_available'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
