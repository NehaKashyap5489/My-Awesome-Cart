# Generated by Django 4.1.7 on 2023-04-30 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopee', '0006_order_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=50000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
