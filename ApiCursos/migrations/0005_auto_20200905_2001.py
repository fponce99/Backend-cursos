# Generated by Django 2.1.5 on 2020-09-05 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiCursos', '0004_tcp'),
    ]

    operations = [
        migrations.AddField(
            model_name='tcp',
            name='cantidad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tcp',
            name='tipo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tcp',
            name='destino',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tcp',
            name='origen',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
