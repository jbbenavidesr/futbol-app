# Generated by Django 3.2.8 on 2021-10-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancha',
            name='telefono',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]