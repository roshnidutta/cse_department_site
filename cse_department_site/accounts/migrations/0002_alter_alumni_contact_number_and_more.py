# Generated by Django 4.2.1 on 2023-06-11 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='graduation_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='contact_number',
            field=models.IntegerField(),
        ),
    ]
