# Generated by Django 3.1.4 on 2020-12-22 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_logs', '0023_auto_20201222_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arkle',
            name='status',
            field=models.CharField(choices=[('BOXED', 'Boxed'), ('FAILED', 'Failed'), ('IN SERVICE', 'In Service'), ('STICK', 'Stick'), ('NOT IN SERVICE', 'Not In Service'), ('MISSING', 'Missing')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='arkle_entry',
            name='status',
            field=models.CharField(choices=[('Connector Broken', 'Connector Broken'), ('No Solid Orange', 'No Solid Orange'), ('Failed Battery', 'Failed Battery'), ('Stick', 'Stick'), ('Failed', 'Failed'), ('In Repair', 'In Repair'), ('Never Worked', 'Refurb'), ('Damaged Case', 'Damaged Case'), ('Switch Broken', 'Switch Broken'), ('No Solid White', 'No Solid White'), ('In Service', 'In Service'), ('Missing', 'Missing'), ('Refurb', 'Refurb')], default='In Service', max_length=18),
        ),
        migrations.AlterField(
            model_name='arkle_entry',
            name='venue',
            field=models.CharField(choices=[('Newmarket', 'Newmarket'), ('Warwick', 'Warwick'), ('Kempton Park', 'Kempton Park'), ('Beverly', 'Beverly'), ('Salisbury', 'Salisbury'), ('Leicester', 'Leicester'), ('Hamilton', 'Hamilton Park'), ('Ludlow', 'Ludlow'), ('Pontefract', 'Pontefract'), ('Newbury', 'Newbury'), ('Goodwood', 'Goodwood'), ('York', 'York'), ('Huntingdon', 'Huntingdon'), ('Wincanton', 'Wincanton'), ('Market Rasen', 'Market Rasen'), ('Redcar', 'Redcar'), ('Kelso', 'Kelso'), ('Chester', 'Chester'), ('Taunton', 'Taunton'), ('Sandown Park', 'Sandown Park'), ('Nottingham', 'Nottingham'), ('Exeter', 'Exeter'), ('Thirsk', 'Thirsk'), ('Cartmel', 'Cartmel'), ('Wetherby', 'Wetherby'), ('Aintree', 'Aintree'), ('Cheltenham', 'Cheltenham'), ('Perth', 'Perth'), ('Catterick Bridge', 'Catterick Bridge'), ('Ayr', 'Ayr'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Musselburgh', 'Musselburgh'), ('Haydock', 'Haydock Park'), ('Epsom Downs', 'Epsom Downs'), ('Carlisle', 'Carlisle')], default='Kempton Park', max_length=18),
        ),
        migrations.AlterField(
            model_name='denman',
            name='status',
            field=models.CharField(choices=[('BOXED', 'Boxed'), ('FAILED', 'Failed'), ('IN SERVICE', 'In Service'), ('STICK', 'Stick'), ('NOT IN SERVICE', 'Not In Service'), ('MISSING', 'Missing')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='denman_entry',
            name='status',
            field=models.CharField(choices=[('Connector Broken', 'Connector Broken'), ('No Solid Orange', 'No Solid Orange'), ('Failed Battery', 'Failed Battery'), ('Stick', 'Stick'), ('Failed', 'Failed'), ('In Repair', 'In Repair'), ('Never Worked', 'Refurb'), ('Damaged Case', 'Damaged Case'), ('Switch Broken', 'Switch Broken'), ('No Solid White', 'No Solid White'), ('In Service', 'In Service'), ('Missing', 'Missing'), ('Refurb', 'Refurb')], default='In Service', max_length=18),
        ),
        migrations.AlterField(
            model_name='denman_entry',
            name='venue',
            field=models.CharField(choices=[('Newmarket', 'Newmarket'), ('Warwick', 'Warwick'), ('Kempton Park', 'Kempton Park'), ('Beverly', 'Beverly'), ('Salisbury', 'Salisbury'), ('Leicester', 'Leicester'), ('Hamilton', 'Hamilton Park'), ('Ludlow', 'Ludlow'), ('Pontefract', 'Pontefract'), ('Newbury', 'Newbury'), ('Goodwood', 'Goodwood'), ('York', 'York'), ('Huntingdon', 'Huntingdon'), ('Wincanton', 'Wincanton'), ('Market Rasen', 'Market Rasen'), ('Redcar', 'Redcar'), ('Kelso', 'Kelso'), ('Chester', 'Chester'), ('Taunton', 'Taunton'), ('Sandown Park', 'Sandown Park'), ('Nottingham', 'Nottingham'), ('Exeter', 'Exeter'), ('Thirsk', 'Thirsk'), ('Cartmel', 'Cartmel'), ('Wetherby', 'Wetherby'), ('Aintree', 'Aintree'), ('Cheltenham', 'Cheltenham'), ('Perth', 'Perth'), ('Catterick Bridge', 'Catterick Bridge'), ('Ayr', 'Ayr'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Musselburgh', 'Musselburgh'), ('Haydock', 'Haydock Park'), ('Epsom Downs', 'Epsom Downs'), ('Carlisle', 'Carlisle')], default='Kempton Park', max_length=18),
        ),
        migrations.AlterField(
            model_name='enable',
            name='status',
            field=models.CharField(choices=[('BOXED', 'Boxed'), ('FAILED', 'Failed'), ('IN SERVICE', 'In Service'), ('STICK', 'Stick'), ('NOT IN SERVICE', 'Not In Service'), ('MISSING', 'Missing')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='status',
            field=models.CharField(choices=[('Connector Broken', 'Connector Broken'), ('No Solid Orange', 'No Solid Orange'), ('Failed Battery', 'Failed Battery'), ('Stick', 'Stick'), ('Failed', 'Failed'), ('In Repair', 'In Repair'), ('Never Worked', 'Refurb'), ('Damaged Case', 'Damaged Case'), ('Switch Broken', 'Switch Broken'), ('No Solid White', 'No Solid White'), ('In Service', 'In Service'), ('Missing', 'Missing'), ('Refurb', 'Refurb')], default='In Service', max_length=18),
        ),
        migrations.AlterField(
            model_name='enable_entry',
            name='venue',
            field=models.CharField(choices=[('Newmarket', 'Newmarket'), ('Warwick', 'Warwick'), ('Kempton Park', 'Kempton Park'), ('Beverly', 'Beverly'), ('Salisbury', 'Salisbury'), ('Leicester', 'Leicester'), ('Hamilton', 'Hamilton Park'), ('Ludlow', 'Ludlow'), ('Pontefract', 'Pontefract'), ('Newbury', 'Newbury'), ('Goodwood', 'Goodwood'), ('York', 'York'), ('Huntingdon', 'Huntingdon'), ('Wincanton', 'Wincanton'), ('Market Rasen', 'Market Rasen'), ('Redcar', 'Redcar'), ('Kelso', 'Kelso'), ('Chester', 'Chester'), ('Taunton', 'Taunton'), ('Sandown Park', 'Sandown Park'), ('Nottingham', 'Nottingham'), ('Exeter', 'Exeter'), ('Thirsk', 'Thirsk'), ('Cartmel', 'Cartmel'), ('Wetherby', 'Wetherby'), ('Aintree', 'Aintree'), ('Cheltenham', 'Cheltenham'), ('Perth', 'Perth'), ('Catterick Bridge', 'Catterick Bridge'), ('Ayr', 'Ayr'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Musselburgh', 'Musselburgh'), ('Haydock', 'Haydock Park'), ('Epsom Downs', 'Epsom Downs'), ('Carlisle', 'Carlisle')], default='Kempton Park', max_length=18),
        ),
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.CharField(choices=[('Connector Broken', 'Connector Broken'), ('No Solid Orange', 'No Solid Orange'), ('Failed Battery', 'Failed Battery'), ('Stick', 'Stick'), ('Failed', 'Failed'), ('In Repair', 'In Repair'), ('Never Worked', 'Refurb'), ('Damaged Case', 'Damaged Case'), ('Switch Broken', 'Switch Broken'), ('No Solid White', 'No Solid White'), ('In Service', 'In Service'), ('Missing', 'Missing'), ('Refurb', 'Refurb')], default='In Service', max_length=18),
        ),
        migrations.AlterField(
            model_name='entry',
            name='venue',
            field=models.CharField(choices=[('Newmarket', 'Newmarket'), ('Warwick', 'Warwick'), ('Kempton Park', 'Kempton Park'), ('Beverly', 'Beverly'), ('Salisbury', 'Salisbury'), ('Leicester', 'Leicester'), ('Hamilton', 'Hamilton Park'), ('Ludlow', 'Ludlow'), ('Pontefract', 'Pontefract'), ('Newbury', 'Newbury'), ('Goodwood', 'Goodwood'), ('York', 'York'), ('Huntingdon', 'Huntingdon'), ('Wincanton', 'Wincanton'), ('Market Rasen', 'Market Rasen'), ('Redcar', 'Redcar'), ('Kelso', 'Kelso'), ('Chester', 'Chester'), ('Taunton', 'Taunton'), ('Sandown Park', 'Sandown Park'), ('Nottingham', 'Nottingham'), ('Exeter', 'Exeter'), ('Thirsk', 'Thirsk'), ('Cartmel', 'Cartmel'), ('Wetherby', 'Wetherby'), ('Aintree', 'Aintree'), ('Cheltenham', 'Cheltenham'), ('Perth', 'Perth'), ('Catterick Bridge', 'Catterick Bridge'), ('Ayr', 'Ayr'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Musselburgh', 'Musselburgh'), ('Haydock', 'Haydock Park'), ('Epsom Downs', 'Epsom Downs'), ('Carlisle', 'Carlisle')], default='Kempton Park', max_length=18),
        ),
        migrations.AlterField(
            model_name='frankel',
            name='status',
            field=models.CharField(choices=[('BOXED', 'Boxed'), ('FAILED', 'Failed'), ('IN SERVICE', 'In Service'), ('STICK', 'Stick'), ('NOT IN SERVICE', 'Not In Service'), ('MISSING', 'Missing')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='frankel_entry',
            name='status',
            field=models.CharField(choices=[('Connector Broken', 'Connector Broken'), ('No Solid Orange', 'No Solid Orange'), ('Failed Battery', 'Failed Battery'), ('Stick', 'Stick'), ('Failed', 'Failed'), ('In Repair', 'In Repair'), ('Never Worked', 'Refurb'), ('Damaged Case', 'Damaged Case'), ('Switch Broken', 'Switch Broken'), ('No Solid White', 'No Solid White'), ('In Service', 'In Service'), ('Missing', 'Missing'), ('Refurb', 'Refurb')], default='In Service', max_length=18),
        ),
        migrations.AlterField(
            model_name='frankel_entry',
            name='venue',
            field=models.CharField(choices=[('Newmarket', 'Newmarket'), ('Warwick', 'Warwick'), ('Kempton Park', 'Kempton Park'), ('Beverly', 'Beverly'), ('Salisbury', 'Salisbury'), ('Leicester', 'Leicester'), ('Hamilton', 'Hamilton Park'), ('Ludlow', 'Ludlow'), ('Pontefract', 'Pontefract'), ('Newbury', 'Newbury'), ('Goodwood', 'Goodwood'), ('York', 'York'), ('Huntingdon', 'Huntingdon'), ('Wincanton', 'Wincanton'), ('Market Rasen', 'Market Rasen'), ('Redcar', 'Redcar'), ('Kelso', 'Kelso'), ('Chester', 'Chester'), ('Taunton', 'Taunton'), ('Sandown Park', 'Sandown Park'), ('Nottingham', 'Nottingham'), ('Exeter', 'Exeter'), ('Thirsk', 'Thirsk'), ('Cartmel', 'Cartmel'), ('Wetherby', 'Wetherby'), ('Aintree', 'Aintree'), ('Cheltenham', 'Cheltenham'), ('Perth', 'Perth'), ('Catterick Bridge', 'Catterick Bridge'), ('Ayr', 'Ayr'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Musselburgh', 'Musselburgh'), ('Haydock', 'Haydock Park'), ('Epsom Downs', 'Epsom Downs'), ('Carlisle', 'Carlisle')], default='Kempton Park', max_length=18),
        ),
        migrations.AlterField(
            model_name='kauto',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('BOXED', 'Boxed'), ('MISSING', 'Missing'), ('STICK', 'Stick')], default='IN SERVICE', max_length=15),
        ),
        migrations.AlterField(
            model_name='kauto_entry',
            name='status',
            field=models.CharField(choices=[('Connector Broken', 'Connector Broken'), ('No Solid Orange', 'No Solid Orange'), ('Failed Battery', 'Failed Battery'), ('Stick', 'Stick'), ('Failed', 'Failed'), ('In Repair', 'In Repair'), ('Never Worked', 'Refurb'), ('Damaged Case', 'Damaged Case'), ('Switch Broken', 'Switch Broken'), ('No Solid White', 'No Solid White'), ('In Service', 'In Service'), ('Missing', 'Missing'), ('Refurb', 'Refurb')], default='In Service', max_length=18),
        ),
        migrations.AlterField(
            model_name='kauto_entry',
            name='venue',
            field=models.CharField(choices=[('Newmarket', 'Newmarket'), ('Warwick', 'Warwick'), ('Kempton Park', 'Kempton Park'), ('Beverly', 'Beverly'), ('Salisbury', 'Salisbury'), ('Leicester', 'Leicester'), ('Hamilton', 'Hamilton Park'), ('Ludlow', 'Ludlow'), ('Pontefract', 'Pontefract'), ('Newbury', 'Newbury'), ('Goodwood', 'Goodwood'), ('York', 'York'), ('Huntingdon', 'Huntingdon'), ('Wincanton', 'Wincanton'), ('Market Rasen', 'Market Rasen'), ('Redcar', 'Redcar'), ('Kelso', 'Kelso'), ('Chester', 'Chester'), ('Taunton', 'Taunton'), ('Sandown Park', 'Sandown Park'), ('Nottingham', 'Nottingham'), ('Exeter', 'Exeter'), ('Thirsk', 'Thirsk'), ('Cartmel', 'Cartmel'), ('Wetherby', 'Wetherby'), ('Aintree', 'Aintree'), ('Cheltenham', 'Cheltenham'), ('Perth', 'Perth'), ('Catterick Bridge', 'Catterick Bridge'), ('Ayr', 'Ayr'), ('Stratford-On-Avon', 'Stratford-On-Avon'), ('Musselburgh', 'Musselburgh'), ('Haydock', 'Haydock Park'), ('Epsom Downs', 'Epsom Downs'), ('Carlisle', 'Carlisle')], default='Kempton Park', max_length=18),
        ),
        migrations.AlterField(
            model_name='winx',
            name='status',
            field=models.CharField(choices=[('BOXED', 'Boxed'), ('FAILED', 'Failed'), ('IN SERVICE', 'In Service'), ('STICK', 'Stick'), ('NOT IN SERVICE', 'Not In Service'), ('MISSING', 'Missing')], default='IN SERVICE', max_length=15),
        ),
    ]