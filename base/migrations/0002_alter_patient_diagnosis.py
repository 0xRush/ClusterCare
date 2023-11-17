# Generated by Django 4.2.4 on 2023-11-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='diagnosis',
            field=models.CharField(choices=[('Type 2 Diabetes Mellitus', 'E11'), ('Hypertension', 'I10'), ('Major Depressive Disorder', 'F32'), ('Acute Bronchitis', 'J20'), ('Essential Hypertension', 'I10'), ('Osteoarthritis of Knee', 'M17'), ('Acute Myocardial Infarction', 'I21'), ('Asthma', 'J45'), ('Urinary Tract Infection', 'N39.0')], max_length=50),
        ),
    ]