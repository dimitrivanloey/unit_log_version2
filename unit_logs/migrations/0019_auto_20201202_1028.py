# Generated by Django 3.1.2 on 2020-12-02 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unit_logs', '0018_auto_20201202_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arkle_entry',
            name='status',
            field=models.CharField(choices=[('No Solid White', 'No Solid White'), ('No Solid Orange', 'No Solid Orange'), ('In Service', 'In Service'), ('Switch Broken', 'Switch Broken'), ('Connector Broken', 'Connector Broken'), ('Failed Battery', 'Failed Battery'), ('Damaged Case', 'Damaged Case')], default='In Service', max_length=18),
        ),
        migrations.AlterField(
            model_name='arkle_entry',
            name='venue',
            field=models.CharField(choices=[('Thirsk', 'Thirsk'), ('Catterick Bridge', 'Catterick Bridge'), ('Ayr', 'Ayr'), ('Cheltenham', 'Cheltenham'), ('Redcar', 'Redcar'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Nottingham', 'Nottingham'), ('Aintree', 'Aintree'), ('Epsom Downs', 'Epsom Downs'), ('Salisbury', 'Salisbury'), ('Leicester', 'Leicester'), ('Kempton Park', 'Kempton Park'), ('Newbury', 'Newbury'), ('Carlisle', 'Carlisle'), ('Cartmel', 'Cartmel'), ('Taunton', 'Taunton'), ('Wincanton', 'Wincanton'), ('Wetherby', 'Wetherby'), ('Chester', 'Chester'), ('Market Rasen', 'Market Rasen'), ('Newmarket', 'Newmarket'), ('Exeter', 'Exeter'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Beverly', 'Beverly'), ('Huntingdon', 'Huntingdon'), ('Goodwood', 'Goodwood'), ('Kelso', 'Kelso'), ('Perth', 'Perth'), ('Hamilton', 'Hamilton Park'), ('Ludlow', 'Ludlow'), ('York', 'York'), ('Haydock', 'Haydock Park'), ('Musselburgh', 'Musselburgh'), ('Warwick', 'Warwick')], default='Kempton Park', max_length=18),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='status',
            field=models.CharField(choices=[('No Solid White', 'No Solid White'), ('No Solid Orange', 'No Solid Orange'), ('In Service', 'In Service'), ('Switch Broken', 'Switch Broken'), ('Connector Broken', 'Connector Broken'), ('Failed Battery', 'Failed Battery'), ('Damaged Case', 'Damaged Case')], default='In Service', max_length=18),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='venue',
            field=models.CharField(choices=[('Thirsk', 'Thirsk'), ('Catterick Bridge', 'Catterick Bridge'), ('Ayr', 'Ayr'), ('Cheltenham', 'Cheltenham'), ('Redcar', 'Redcar'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Nottingham', 'Nottingham'), ('Aintree', 'Aintree'), ('Epsom Downs', 'Epsom Downs'), ('Salisbury', 'Salisbury'), ('Leicester', 'Leicester'), ('Kempton Park', 'Kempton Park'), ('Newbury', 'Newbury'), ('Carlisle', 'Carlisle'), ('Cartmel', 'Cartmel'), ('Taunton', 'Taunton'), ('Wincanton', 'Wincanton'), ('Wetherby', 'Wetherby'), ('Chester', 'Chester'), ('Market Rasen', 'Market Rasen'), ('Newmarket', 'Newmarket'), ('Exeter', 'Exeter'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Beverly', 'Beverly'), ('Huntingdon', 'Huntingdon'), ('Goodwood', 'Goodwood'), ('Kelso', 'Kelso'), ('Perth', 'Perth'), ('Hamilton', 'Hamilton Park'), ('Ludlow', 'Ludlow'), ('York', 'York'), ('Haydock', 'Haydock Park'), ('Musselburgh', 'Musselburgh'), ('Warwick', 'Warwick')], default='Kempton Park', max_length=18),
        ),
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.CharField(choices=[('No Solid White', 'No Solid White'), ('No Solid Orange', 'No Solid Orange'), ('In Service', 'In Service'), ('Switch Broken', 'Switch Broken'), ('Connector Broken', 'Connector Broken'), ('Failed Battery', 'Failed Battery'), ('Damaged Case', 'Damaged Case')], default='In Service', max_length=18),
        ),
        migrations.AlterField(
            model_name='entry',
            name='venue',
            field=models.CharField(choices=[('Thirsk', 'Thirsk'), ('Catterick Bridge', 'Catterick Bridge'), ('Ayr', 'Ayr'), ('Cheltenham', 'Cheltenham'), ('Redcar', 'Redcar'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Nottingham', 'Nottingham'), ('Aintree', 'Aintree'), ('Epsom Downs', 'Epsom Downs'), ('Salisbury', 'Salisbury'), ('Leicester', 'Leicester'), ('Kempton Park', 'Kempton Park'), ('Newbury', 'Newbury'), ('Carlisle', 'Carlisle'), ('Cartmel', 'Cartmel'), ('Taunton', 'Taunton'), ('Wincanton', 'Wincanton'), ('Wetherby', 'Wetherby'), ('Chester', 'Chester'), ('Market Rasen', 'Market Rasen'), ('Newmarket', 'Newmarket'), ('Exeter', 'Exeter'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Beverly', 'Beverly'), ('Huntingdon', 'Huntingdon'), ('Goodwood', 'Goodwood'), ('Kelso', 'Kelso'), ('Perth', 'Perth'), ('Hamilton', 'Hamilton Park'), ('Ludlow', 'Ludlow'), ('York', 'York'), ('Haydock', 'Haydock Park'), ('Musselburgh', 'Musselburgh'), ('Warwick', 'Warwick')], default='Kempton Park', max_length=18),
        ),
        migrations.CreateModel(
            name='Arkle_Denman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('No Solid White', 'No Solid White'), ('No Solid Orange', 'No Solid Orange'), ('In Service', 'In Service'), ('Switch Broken', 'Switch Broken'), ('Connector Broken', 'Connector Broken'), ('Failed Battery', 'Failed Battery'), ('Damaged Case', 'Damaged Case')], default='In Service', max_length=18)),
                ('venue', models.CharField(choices=[('Thirsk', 'Thirsk'), ('Catterick Bridge', 'Catterick Bridge'), ('Ayr', 'Ayr'), ('Cheltenham', 'Cheltenham'), ('Redcar', 'Redcar'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Nottingham', 'Nottingham'), ('Aintree', 'Aintree'), ('Epsom Downs', 'Epsom Downs'), ('Salisbury', 'Salisbury'), ('Leicester', 'Leicester'), ('Kempton Park', 'Kempton Park'), ('Newbury', 'Newbury'), ('Carlisle', 'Carlisle'), ('Cartmel', 'Cartmel'), ('Taunton', 'Taunton'), ('Wincanton', 'Wincanton'), ('Wetherby', 'Wetherby'), ('Chester', 'Chester'), ('Market Rasen', 'Market Rasen'), ('Newmarket', 'Newmarket'), ('Exeter', 'Exeter'), ('Sandown Park', 'Sandown Park'), ('Pontefract', 'Pontefract'), ('Beverly', 'Beverly'), ('Huntingdon', 'Huntingdon'), ('Goodwood', 'Goodwood'), ('Kelso', 'Kelso'), ('Perth', 'Perth'), ('Hamilton', 'Hamilton Park'), ('Ludlow', 'Ludlow'), ('York', 'York'), ('Haydock', 'Haydock Park'), ('Musselburgh', 'Musselburgh'), ('Warwick', 'Warwick')], default='Kempton Park', max_length=18)),
                ('comments', models.TextField(blank=True)),
                ('denman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit_logs.denman')),
            ],
            options={
                'verbose_name_plural': 'denman entries',
            },
        ),
    ]