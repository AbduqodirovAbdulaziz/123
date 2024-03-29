# Generated by Django 5.0.1 on 2024-02-29 11:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bolim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haqida', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('familiya', models.CharField(max_length=30)),
                ('tirik', models.CharField(choices=[('tirik', 'tirik'), ("o'lgan", "o'lgan")], max_length=10)),
                ('mamlakat', models.CharField(blank=True, max_length=35, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=30)),
                ('yili', models.DateField()),
                ('file', models.FileField(null=True, upload_to='')),
                ('bolim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainAPP.bolim')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainAPP.muallif')),
            ],
        ),
    ]
