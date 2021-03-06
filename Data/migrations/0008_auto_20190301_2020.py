# Generated by Django 2.1.5 on 2019-03-01 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0007_auto_20190222_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-Time'], 'verbose_name_plural': '订单'},
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderState',
            field=models.CharField(choices=[('0', '未付款'), ('1', '微信'), ('2', '支付宝'), ('3', '现金')], default='0', max_length=6, verbose_name='付款状态'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='Price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True, verbose_name='单价快照'),
        ),
    ]
