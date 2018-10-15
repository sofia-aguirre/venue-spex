# Generated by Django 2.1.2 on 2018-10-15 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('full_name', models.CharField(max_length=100)),
                ('contact_email', models.CharField(max_length=100)),
                ('contact_phone', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('houseSoundInstalled', models.TextField()),
                ('houseElectricInstalled', models.TextField()),
                ('houseLightsInstalled', models.TextField()),
                ('houseStageInstalled', models.TextField()),
                ('houseBackInstalled', models.TextField()),
                ('houseSoundAvail', models.TextField()),
                ('houseElectricAvail', models.TextField()),
                ('houseLightsAvail', models.TextField()),
                ('houseStageAvail', models.TextField()),
                ('houseBackAvail', models.TextField()),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venue', to='vs_app.CustomUser')),
            ],
        ),
    ]
