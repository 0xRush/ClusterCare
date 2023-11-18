# Generated by Django 4.2.4 on 2023-11-18 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_patient_diagnosis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileclinic',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mobileclinics', to=settings.AUTH_USER_MODEL),
        ),
    ]