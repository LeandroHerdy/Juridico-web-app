# Generated by Django 4.0.2 on 2022-02-03 22:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroHora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_registro_hora', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionario.funcionario')),
            ],
        ),
    ]
