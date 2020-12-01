# Generated by Django 3.1.2 on 2020-11-25 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unit_logs', '0007_auto_20201125_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('IN SERVICE', 'In Service'), ('NO SOLID ORANGE', 'No Solid Orange'), ('FAILED BATTERY', 'Failed Battery'), ('SWITCH BROKEN', 'Switch Broken'), ('CONNECTOR BROKEN', 'Connector Broken'), ('NO SOLID WHITE', 'No Solid White'), ('DAMAGED CASE', 'Damaged Case')], default='IN SERVICE', max_length=18)),
                ('comments', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.AlterField(
            model_name='arkle',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('MISSING', 'Missing'), ('STICK', 'Stick'), ('BOXED', 'Boxed')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='denman',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('MISSING', 'Missing'), ('STICK', 'Stick'), ('BOXED', 'Boxed')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='enable',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('MISSING', 'Missing'), ('STICK', 'Stick'), ('BOXED', 'Boxed')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='frankel',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('MISSING', 'Missing'), ('STICK', 'Stick'), ('BOXED', 'Boxed')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='kauto',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('MISSING', 'Missing'), ('STICK', 'Stick'), ('BOXED', 'Boxed')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='winx',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('MISSING', 'Missing'), ('STICK', 'Stick'), ('BOXED', 'Boxed')], default='STICK', max_length=10),
        ),
        migrations.DeleteModel(
            name='Entry_Winx',
        ),
        migrations.AddField(
            model_name='entry',
            name='winx',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_logs.winx'),
        ),
    ]