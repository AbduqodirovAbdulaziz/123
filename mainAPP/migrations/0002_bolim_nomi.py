# Generated by Django 5.0.1 on 2024-02-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolim',
            name='nomi',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
