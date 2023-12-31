# Generated by Django 4.1.7 on 2023-04-29 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopee', '0004_alter_contact_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
            ],
        ),
    ]
