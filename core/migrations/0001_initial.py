# Generated by Django 2.2.4 on 2019-08-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('from_user', models.CharField(max_length=70)),
                ('to_user', models.CharField(max_length=70)),
                ('block_number', models.IntegerField()),
                ('hash', models.CharField(max_length=100)),
            ],
        ),
    ]
