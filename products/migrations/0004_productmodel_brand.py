# Generated by Django 4.0.3 on 2022-03-04 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='brand',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='products.brandmodel'),
            preserve_default=False,
        ),
    ]