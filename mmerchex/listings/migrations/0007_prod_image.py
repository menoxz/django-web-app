# Generated by Django 5.0.1 on 2024-01-31 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_prod_band'),
    ]

    operations = [
        migrations.AddField(
            model_name='prod',
            name='image',
            field=models.ImageField(default='', upload_to='image'),
            preserve_default=False,
        ),
    ]