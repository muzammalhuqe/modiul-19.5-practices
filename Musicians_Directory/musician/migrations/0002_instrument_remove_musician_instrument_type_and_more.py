# Generated by Django 4.2.7 on 2023-12-20 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='musician',
            name='instrument_type',
        ),
        migrations.AddField(
            model_name='musician',
            name='instrument_type',
            field=models.ManyToManyField(to='musician.instrument'),
        ),
    ]
