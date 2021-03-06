# Generated by Django 3.2.8 on 2021-10-06 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('canchas', '0002_cancha_telefono'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuando', models.DateTimeField()),
                ('mensaje', models.CharField(max_length=255)),
                ('cupos', models.IntegerField()),
                ('cancha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidas', to='canchas.cancha')),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
