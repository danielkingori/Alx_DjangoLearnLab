# Generated by Django 5.0.7 on 2024-08-19 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0004_alter_author_name_alter_book_author_alter_book_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='library',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='relationship_app.library'),
        ),
    ]
