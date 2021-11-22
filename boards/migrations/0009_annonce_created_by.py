# Generated by Django 3.1.7 on 2021-03-17 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0008_remove_annonce_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='created_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='annonce', to='auth.user'),
            preserve_default=False,
        ),
    ]