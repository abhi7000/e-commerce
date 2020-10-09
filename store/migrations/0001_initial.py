# Generated by Django 3.1 on 2020-08-23 02:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=300)),
                ('pub_date', models.DateField(default=datetime.date.today)),
                ('sub_cat', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(default=' ', upload_to='store/images')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
