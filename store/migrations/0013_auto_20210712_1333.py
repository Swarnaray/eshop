# Generated by Django 3.0.5 on 2021-07-12 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210711_0159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='address1',
        ),
        migrations.AddField(
            model_name='order',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='pincode',
            field=models.CharField(blank=True, default='', max_length=7),
        ),
    ]
