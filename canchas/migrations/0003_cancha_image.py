# Generated by Django 3.2.8 on 2021-10-19 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0002_cancha_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancha',
            name='image',
            field=models.CharField(choices=[('images/cancha1.jpeg', 'Cancha 1'), ('images/cancha2.jpeg', 'Cancha 2'), ('images/cancha3.jpeg', 'Cancha 3'), ('images/cancha4.jpeg', 'Cancha 4'), ('images/cancha5.jpeg', 'Cancha 5'), ('images/cancha6.jpeg', 'Cancha 6'), ('images/cancha7.jpeg', 'Cancha 7')], default='images/cancha1.jpeg', max_length=20),
        ),
    ]
