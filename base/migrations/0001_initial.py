# Generated by Django 4.2.4 on 2023-11-14 10:21

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=200, null=True)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('Manager', 'Manager'), ('None', 'None')], max_length=20, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('population_density', models.IntegerField()),
                ('crisis_type', models.CharField(choices=[('Earthquakes', 'Earthquakes'), ('Tornadoes', 'Tornadoes'), ('Floods', 'Floods'), ('Wildfires', 'Wildfires'), ('Droughts', 'Droughts'), ('Tsunamis', 'Tsunamis'), ('Volcanic Eruptions', 'Volcanic Eruptions'), ('Pandemics', 'Pandemics'), ('Food and Water Contamination', 'Food and Water Contamination'), ('Financial Crises', 'Financial Crises'), ('Refugee and Displacement Crises', 'Refugee and Displacement Crises'), ('Food and Water Scarcity', 'Food and Water Scarcity'), ('Healthcare Crises', 'Healthcare Crises')], max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('inActive', 'inActive')], max_length=20)),
                ('num_of_patients', models.IntegerField()),
                ('weather_status', models.CharField(choices=[('Clear Sky', 'Clear Sky'), ('Cloudy', 'Cloudy'), ('Partly Cloudy', 'Partly Cloudy'), ('Fog', 'Fog'), ('Rain', 'Rain'), ('Snow', 'Snow'), ('Sleet', 'Sleet'), ('Thunderstorm', 'Thunderstorm'), ('Tornado', 'Tornado'), ('Blizzard', 'Blizzard'), ('Heatwave', 'Heatwave'), ('Dust Storm', 'Dust Storm')], max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mobileclinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('num_of_staff', models.IntegerField()),
                ('clinic_services', models.CharField(choices=[('Emergency Medical Care', 'Emergency Medical Care'), ('Wound Care', 'Wound Care'), ('Infectious Disease Control', 'Infectious Disease Control'), ('Mental Health Support', 'Mental Health Support'), ('Rescue and Evacuation Support', 'Rescue and Evacuation Support'), ('Health Education', 'Health Education')], max_length=100)),
                ('clinic_capacity', models.IntegerField()),
                ('total_annual_budget', models.IntegerField()),
                ('pharmaceutical_expenditure', models.IntegerField()),
                ('pharmaceutical_waste', models.IntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('Medical Equipment', 'Medical Equipment'), ('Medical Supplies', 'Medical Supplies'), ('Vaccines and Immunization', 'Vaccines and Immunization'), ('Diagnostic and Laboratory Equipment', 'Diagnostic and Laboratory Equipment'), ('Pharmaceutical Supplies', 'Pharmaceutical Supplies'), ('Emergency Response and Rescue Equipment', 'Emergency Response and Rescue Equipment')], max_length=100)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('mobile_clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.mobileclinic')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('diagnosis', models.TextField()),
                ('medication_date', models.DateField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.activity')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='mobile_clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.mobileclinic'),
        ),
    ]
