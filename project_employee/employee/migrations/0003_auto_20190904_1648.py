# Generated by Django 2.2.4 on 2019-09-04 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20190904_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(blank=True, max_length=20, verbose_name='部活名'),
        ),
    ]
