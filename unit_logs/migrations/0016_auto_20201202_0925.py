# Generated by Django 3.1.2 on 2020-12-02 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unit_logs', '0015_auto_20201202_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arkle',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('MISSING', 'Missing'), ('BOXED', 'Boxed'), ('STICK', 'Stick')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='denman',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('MISSING', 'Missing'), ('BOXED', 'Boxed'), ('STICK', 'Stick')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='enable',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('MISSING', 'Missing'), ('BOXED', 'Boxed'), ('STICK', 'Stick')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.CharField(choices=[('Connector Broken', 'Connector Broken'), ('No Solid Orange', 'No Solid Orange'), ('Damaged Case', 'Damaged Case'), ('Failed Battery', 'Failed Battery'), ('In Service', 'In Service'), ('Switch Broken', 'Switch Broken'), ('No Solid White', 'No Solid White')], default='In Service', max_length=18),
        ),
        migrations.AlterField(
            model_name='entry',
            name='venue',
            field=models.CharField(choices=[('Newbury', 'Newbury'), ('Hamilton', 'Hamilton Park'), ('York', 'York'), ('Thirsk', 'Thirsk'), ('Wincanton', 'Wincanton'), ('Redcar', 'Redcar'), ('Leicester', 'Leicester'), ('Ayr', 'Ayr'), ('Exeter', 'Exeter'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Market Rasen', 'Market Rasen'), ('Newmarket', 'Newmarket'), ('Kempton Park', 'Kempton Park'), ('Taunton', 'Taunton'), ('Aintree', 'Aintree'), ('Sandown Park', 'Sandown Park'), ('Epsom Downs', 'Epsom Downs'), ('Wetherby', 'Wetherby'), ('Carlisle', 'Carlisle'), ('Catterick Bridge', 'Catterick Bridge'), ('Cartmel', 'Cartmel'), ('Ludlow', 'Ludlow'), ('Kelso', 'Kelso'), ('Cheltenham', 'Cheltenham'), ('Goodwood', 'Goodwood'), ('Salisbury', 'Salisbury'), ('Haydock', 'Haydock Park'), ('Nottingham', 'Nottingham'), ('Musselburgh', 'Musselburgh'), ('Perth', 'Perth'), ('Beverly', 'Beverly'), ('Chester', 'Chester'), ('Huntingdon', 'Huntingdon'), ('Pontefract', 'Pontefract'), ('Warwick', 'Warwick')], default='Kempton', max_length=18),
        ),
        migrations.AlterField(
            model_name='frankel',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('MISSING', 'Missing'), ('BOXED', 'Boxed'), ('STICK', 'Stick')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='kauto',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('MISSING', 'Missing'), ('BOXED', 'Boxed'), ('STICK', 'Stick')], default='STICK', max_length=10),
        ),
        migrations.AlterField(
            model_name='winx',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('MISSING', 'Missing'), ('BOXED', 'Boxed'), ('STICK', 'Stick')], default='STICK', max_length=10),
        ),
        migrations.CreateModel(
            name='Enable_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Connector Broken', 'Connector Broken'), ('No Solid Orange', 'No Solid Orange'), ('Damaged Case', 'Damaged Case'), ('Failed Battery', 'Failed Battery'), ('In Service', 'In Service'), ('Switch Broken', 'Switch Broken'), ('No Solid White', 'No Solid White')], default='In Service', max_length=18)),
                ('venue', models.CharField(choices=[('Newbury', 'Newbury'), ('Hamilton', 'Hamilton Park'), ('York', 'York'), ('Thirsk', 'Thirsk'), ('Wincanton', 'Wincanton'), ('Redcar', 'Redcar'), ('Leicester', 'Leicester'), ('Ayr', 'Ayr'), ('Exeter', 'Exeter'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Market Rasen', 'Market Rasen'), ('Newmarket', 'Newmarket'), ('Kempton Park', 'Kempton Park'), ('Taunton', 'Taunton'), ('Aintree', 'Aintree'), ('Sandown Park', 'Sandown Park'), ('Epsom Downs', 'Epsom Downs'), ('Wetherby', 'Wetherby'), ('Carlisle', 'Carlisle'), ('Catterick Bridge', 'Catterick Bridge'), ('Cartmel', 'Cartmel'), ('Ludlow', 'Ludlow'), ('Kelso', 'Kelso'), ('Cheltenham', 'Cheltenham'), ('Goodwood', 'Goodwood'), ('Salisbury', 'Salisbury'), ('Haydock', 'Haydock Park'), ('Nottingham', 'Nottingham'), ('Musselburgh', 'Musselburgh'), ('Perth', 'Perth'), ('Beverly', 'Beverly'), ('Chester', 'Chester'), ('Huntingdon', 'Huntingdon'), ('Pontefract', 'Pontefract'), ('Warwick', 'Warwick')], default='Kempton', max_length=18)),
                ('comments', models.TextField(blank=True)),
                ('enable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_logs.enable')),
            ],
            options={
                'verbose_name_plural': 'enable entries',
            },
        ),
    ]
