# Generated by Django 3.1.2 on 2020-10-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_logs', '0002_auto_20201029_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arkle',
            name='status',
            field=models.CharField(choices=[('STICK', 'Stick'), ('MISSING', 'Missing'), ('FAILED', 'Failed'), ('BOXED', 'boxed')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='denman',
            name='status',
            field=models.CharField(choices=[('STICK', 'Stick'), ('MISSING', 'Missing'), ('FAILED', 'Failed'), ('BOXED', 'boxed')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='enable',
            name='status',
            field=models.CharField(choices=[('STICK', 'Stick'), ('MISSING', 'Missing'), ('FAILED', 'Failed'), ('BOXED', 'boxed')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='frankel',
            name='status',
            field=models.CharField(choices=[('STICK', 'Stick'), ('MISSING', 'Missing'), ('FAILED', 'Failed'), ('BOXED', 'Boxed')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='kauto',
            name='status',
            field=models.CharField(choices=[('STICK', 'Stick'), ('MISSING', 'Missing'), ('FAILED', 'Failed'), ('BOXED', 'boxed')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='winx',
            name='status',
            field=models.CharField(choices=[('STICK', 'Stick'), ('MISSING', 'Missing'), ('FAILED', 'Failed'), ('BOXED', 'boxed')], default='STICK', max_length=10),
        ),
    ]