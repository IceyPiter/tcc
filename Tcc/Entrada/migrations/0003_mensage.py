# Generated by Django 4.2.5 on 2023-09-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrada', '0002_alter_user_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mensage', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
