# Generated by Django 4.1.1 on 2022-11-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0008_alter_receta_preparación'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='preparación',
            field=models.TextField(max_length=5000),
        ),
    ]
