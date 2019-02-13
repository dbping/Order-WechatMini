# Generated by Django 2.1.5 on 2019-02-13 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0005_menutype_menus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menutype',
            name='Menus',
        ),
        migrations.AlterField(
            model_name='menu',
            name='Type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Menus', to='Data.MenuType', verbose_name='菜品分类'),
        ),
    ]
