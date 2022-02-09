# Generated by Django 4.0.2 on 2022-02-08 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
        ('funcionario', '0002_alter_funcionario_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empresa.empresa'),
        ),
    ]