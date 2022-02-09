# Generated by Django 4.0.2 on 2022-02-08 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
            preserve_default=False,
        ),
    ]