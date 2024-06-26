# Generated by Django 5.0.4 on 2024-04-14 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='clienteProduto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_cliente', models.CharField(max_length=50)),
                ('id_produto', models.CharField(max_length=200)),
            ],
        ),
    ]
