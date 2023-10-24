# Generated by Django 4.2.4 on 2023-10-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='crisis_type',
            field=models.CharField(choices=[('Earthquakes', 'Earthquakes'), ('Tornadoes', 'Tornadoes'), ('Floods', 'Floods'), ('Wildfires', 'Wildfires'), ('Droughts', 'Droughts'), ('Tsunamis', 'Tsunamis'), ('Volcanic Eruptions', 'Volcanic Eruptions'), ('Pandemics', 'Pandemics'), ('Food and Water Contamination', 'Food and Water Contamination'), ('Financial Crises', 'Financial Crises'), ('Refugee and Displacement Crises', 'Refugee and Displacement Crises'), ('Food and Water Scarcity', 'Food and Water Scarcity'), ('Healthcare Crises', 'Healthcare Crises')], max_length=100),
        ),
        migrations.AlterField(
            model_name='activity',
            name='weather_status',
            field=models.CharField(choices=[('Clear Sky', 'Clear Sky'), ('Cloudy', 'Cloudy'), ('Partly Cloudy', 'Partly Cloudy'), ('Fog', 'Fog'), ('Rain', 'Rain'), ('Snow', 'Snow'), ('Sleet', 'Sleet'), ('Thunderstorm', 'Thunderstorm'), ('Tornado', 'Tornado'), ('Blizzard', 'Blizzard'), ('Heatwave', 'Heatwave'), ('Dust Storm', 'Dust Storm')], max_length=100),
        ),
        migrations.AlterField(
            model_name='mobileclinic',
            name='clinic_services',
            field=models.CharField(choices=[('Emergency Medical Care', 'Emergency Medical Care'), ('Wound Care', 'Wound Care'), ('Infectious Disease Control', 'Infectious Disease Control'), ('Mental Health Support', 'Mental Health Support'), ('Rescue and Evacuation Support', 'Rescue and Evacuation Support'), ('Health Education', 'Health Education')], max_length=100),
        ),
        migrations.AlterField(
            model_name='resources',
            name='type',
            field=models.CharField(blank=True, choices=[('Medical Equipment', 'Medical Equipment'), ('Medical Supplies', 'Medical Supplies'), ('Vaccines and Immunization', 'Vaccines and Immunization'), ('Diagnostic and Laboratory Equipment', 'Diagnostic and Laboratory Equipment'), ('Pharmaceutical Supplies', 'Pharmaceutical Supplies'), ('Emergency Response and Rescue Equipment', 'Emergency Response and Rescue Equipment')], max_length=100, null=True),
        ),
    ]
