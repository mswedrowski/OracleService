# Generated by Django 2.2.5 on 2019-10-30 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20191030_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodayOrderDistribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=100)),
                ('distribution', models.FloatField(max_length=20)),
            ],
        ),
    ]
