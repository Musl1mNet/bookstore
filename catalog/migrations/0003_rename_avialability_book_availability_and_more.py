# Generated by Django 4.1.3 on 2023-02-03 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_author_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='avialability',
            new_name='availability',
        ),
        migrations.AlterField(
            model_name='book',
            name='content',
            field=models.TextField(),
        ),
    ]
