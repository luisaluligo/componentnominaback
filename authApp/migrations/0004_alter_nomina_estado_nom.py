# Generated by Django 3.2.8 on 2021-10-27 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_empleado_estado_emp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomina',
            name='estado_nom',
            field=models.CharField(choices=[('liquidada', 'liquidada'), ('pre-liquidada', 'pre-liquidada')], max_length=230),
        ),
    ]
