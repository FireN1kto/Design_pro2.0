# Generated by Django 3.2.25 on 2024-12-13 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppDesign', '0002_category_interiordesignrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interiordesignrequest',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AppDesign.category'),
        ),
    ]
