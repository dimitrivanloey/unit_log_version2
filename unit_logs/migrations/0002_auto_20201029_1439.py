# Generated by Django 3.1.2 on 2020-10-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arkle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('MISSING', 'Missing'), ('FAILED', 'Failed'), ('BOXED', 'boxed'), ('STICK', 'Stick')], default='STICK', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Denman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('MISSING', 'Missing'), ('FAILED', 'Failed'), ('BOXED', 'boxed'), ('STICK', 'Stick')], default='STICK', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Enable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('MISSING', 'Missing'), ('FAILED', 'Failed'), ('BOXED', 'boxed'), ('STICK', 'Stick')], default='STICK', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Frankel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('MISSING', 'Missing'), ('FAILED', 'Failed'), ('BOXED', 'boxed'), ('STICK', 'Stick')], default='STICK', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kauto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('MISSING', 'Missing'), ('FAILED', 'Failed'), ('BOXED', 'boxed'), ('STICK', 'Stick')], default='STICK', max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='winx',
            name='status',
            field=models.CharField(choices=[('MISSING', 'Missing'), ('FAILED', 'Failed'), ('BOXED', 'boxed'), ('STICK', 'Stick')], default='STICK', max_length=10),
        ),
    ]
