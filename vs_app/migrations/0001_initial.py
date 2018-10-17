# Generated by Django 2.1.2 on 2018-10-17 04:19

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
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_pic', models.ImageField(blank=True, null=True, upload_to='comment_pics')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('full_name', models.CharField(max_length=100)),
                ('contact_email', models.CharField(max_length=100)),
                ('contact_phone', models.CharField(max_length=17)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('venue_pic', models.ImageField(blank=True, null=True, upload_to='venue_pics')),
                ('parking_diagram', models.ImageField(blank=True, null=True, upload_to='parking_diagrams')),
                ('parking_details', models.TextField(blank=True)),
                ('audience_diagram', models.ImageField(blank=True, null=True, upload_to='audience_diagrams')),
                ('audience_details', models.TextField(blank=True)),
                ('sound_diagram', models.ImageField(blank=True, null=True, upload_to='sound_diagrams')),
                ('houseSoundInstalled', models.TextField(blank=True)),
                ('houseSoundAvail', models.TextField(blank=True)),
                ('electrics_diagram', models.ImageField(blank=True, null=True, upload_to='electrics_diagrams')),
                ('houseElectricInstalled', models.TextField(blank=True)),
                ('houseElectricAvail', models.TextField(blank=True)),
                ('lights_diagram', models.ImageField(blank=True, null=True, upload_to='lights_diagrams')),
                ('houseLightsInstalled', models.TextField(blank=True)),
                ('houseLightsAvail', models.TextField(blank=True)),
                ('stage_diagram', models.ImageField(blank=True, null=True, upload_to='stage_diagrams')),
                ('houseStageInstalled', models.TextField(blank=True)),
                ('houseStageAvail', models.TextField(blank=True)),
                ('backstage_diagram', models.ImageField(blank=True, null=True, upload_to='backstage_diagrams')),
                ('houseBackInstalled', models.TextField(blank=True)),
                ('houseBackAvail', models.TextField(blank=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venue', to='vs_app.CustomUser')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='vs_app.CustomUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='vs_app.Venue'),
        ),
    ]
