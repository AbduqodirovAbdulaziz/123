# Generated by Django 5.0.1 on 2024-02-29 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPP', '0002_bolim_nomi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitob',
            name='file',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
