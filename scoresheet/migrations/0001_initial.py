# Generated by Django 5.1.4 on 2025-01-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startup_idea', models.CharField(max_length=10)),
                ('target_market', models.CharField(max_length=10)),
                ('growth_potential', models.CharField(max_length=10)),
                ('revenue_model', models.CharField(max_length=10)),
                ('stage_of_startup', models.CharField(max_length=10)),
                ('team_members', models.CharField(max_length=10)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
