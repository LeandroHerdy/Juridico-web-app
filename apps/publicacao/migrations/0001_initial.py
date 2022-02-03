# Generated by Django 4.0.2 on 2022-02-03 22:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('processo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_publicacao', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('numero', models.IntegerField(max_length=50)),
                ('processo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='processo.processo')),
            ],
        ),
    ]
