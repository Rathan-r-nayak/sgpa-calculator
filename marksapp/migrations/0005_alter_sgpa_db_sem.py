# Generated by Django 4.1.2 on 2022-11-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marksapp', '0004_rename_credit_sgpa_db_sem_remove_sgpa_db_mark_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sgpa_db',
            name='sem',
            field=models.TextField(null=True),
        ),
    ]
