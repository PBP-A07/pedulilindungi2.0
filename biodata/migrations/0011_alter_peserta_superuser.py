# Generated by Django 3.2.7 on 2021-10-27 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biodata', '0010_alter_peserta_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peserta',
            name='superUser',
            field=models.ForeignKey(db_column='User.username', default=-1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
