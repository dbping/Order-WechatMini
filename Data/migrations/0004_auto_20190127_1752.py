# Generated by Django 2.1.5 on 2019-01-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0003_auto_20190127_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='Price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True, verbose_name='价格'),
        ),
    ]
