# Generated by Django 2.2.13 on 2021-07-09 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]