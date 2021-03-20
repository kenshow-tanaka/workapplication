# Generated by Django 3.1.7 on 2021-02-25 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pdc',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('plan', models.CharField(max_length=400)),
                ('do', models.CharField(blank=True, max_length=400, null=True)),
                ('check', models.CharField(blank=True, max_length=400, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('userPdc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userPdc', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('action_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_user', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdca.category')),
                ('pdca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdcs', to='pdca.pdc')),
            ],
        ),
    ]