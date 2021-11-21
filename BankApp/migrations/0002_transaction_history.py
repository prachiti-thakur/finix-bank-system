# Generated by Django 3.2.8 on 2021-11-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.IntegerField()),
                ('receiver', models.IntegerField()),
                ('amount', models.FloatField(default=0)),
                ('dnt', models.DateTimeField(editable=False)),
            ],
        ),
    ]
