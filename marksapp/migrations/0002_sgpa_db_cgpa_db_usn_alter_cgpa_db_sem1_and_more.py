# Generated by Django 4.1.2 on 2022-11-08 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marksapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sgpa_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='cgpa_db',
            name='usn',
            field=models.TextField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cgpa_db',
            name='sem1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cgpa_db',
            name='sem2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cgpa_db',
            name='sem3',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cgpa_db',
            name='sem4',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cgpa_db',
            name='sem5',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cgpa_db',
            name='sem6',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cgpa_db',
            name='sem7',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cgpa_db',
            name='sem8',
            field=models.FloatField(null=True),
        ),
    ]
