from django.db import models

class Winx(models.Model):

    STATUS_CHOICES = {
        ('MISSING', 'Missing'),
        ('FAILED', 'Failed'),
        ('STICK', 'Stick'),
        ('BOXED', 'Boxed'),
    }

    number = models.PositiveSmallIntegerField()
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='STICK')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"W{self.number}"
        return name


class Enable(models.Model):

    STATUS_CHOICES = {
        ('MISSING', 'Missing'),
        ('FAILED', 'Failed'),
        ('STICK', 'Stick'),
        ('BOXED', 'Boxed'),
    }

    number = models.PositiveSmallIntegerField()
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='STICK')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"E{self.number}"
        return name


class Arkle(models.Model):

    STATUS_CHOICES = {
        ('MISSING', 'Missing'),
        ('FAILED', 'Failed'),
        ('STICK', 'Stick'),
        ('BOXED', 'Boxed'),
    }

    number = models.PositiveSmallIntegerField()
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='STICK')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"A{self.number}"
        return name


class Denman(models.Model):

    STATUS_CHOICES = {
        ('MISSING', 'Missing'),
        ('FAILED', 'Failed'),
        ('STICK', 'Stick'),
        ('BOXED', 'Boxed'),
    }

    number = models.PositiveSmallIntegerField()
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='STICK')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"D{self.number}"
        return name



class Kauto(models.Model):

    STATUS_CHOICES = {
        ('MISSING', 'Missing'),
        ('FAILED', 'Failed'),
        ('STICK', 'Stick'),
        ('BOXED', 'Boxed'),
    }

    number = models.PositiveSmallIntegerField()
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='STICK')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"K{self.number}"
        return name


class Frankel(models.Model):

    STATUS_CHOICES = {
        ('MISSING', 'Missing'),
        ('FAILED', 'Failed'),
        ('STICK', 'Stick'),
        ('BOXED', 'Boxed'),
    }

    number = models.PositiveSmallIntegerField()
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='STICK')

    def __str__(self):
        """Returning a sring representation of the model"""
        name = f"F{self.number}"
        return name


class Entry(models.Model):

    STATUS_CHOICES = {
        ('In Service', 'In Service'),
        ('Failed Battery', 'Failed Battery'),
        ('Damaged Case', 'Damaged Case'),
        ('No Solid White', 'No Solid White'),
        ('No Solid Orange', 'No Solid Orange'),
        ('Connector Broken', 'Connector Broken'),
        ('Switch Broken', 'Switch Broken'),
    }

    VENUES = {
        ('Aintree', 'Aintree'),
        ('Ayr', 'Ayr'),
        ('Beverly', 'Beverly'),
        ('Carlisle', 'Carlisle'),
        ('Cartmel', 'Cartmel'),
        ('Catterick Bridge', 'Catterick Bridge'),
        ('Cheltenham', 'Cheltenham'),
        ('Chester', 'Chester'),
        ('Epsom Downs', 'Epsom Downs'),
        ('Exeter', 'Exeter'),
        ('Goodwood', 'Goodwood'),
        ('Hamilton', 'Hamilton Park'),
        ('Haydock', 'Haydock Park'),
        ('Huntingdon', 'Huntingdon'),
        ('Kelso', 'Kelso'),
        ('Kempton Park', 'Kempton Park'),
        ('Leicester', 'Leicester'),
        ('Ludlow', 'Ludlow'),
        ('Market Rasen', 'Market Rasen'),
        ('Musselburgh', 'Musselburgh'),
        ('Newbury', 'Newbury'),
        ('Newmarket', 'Newmarket'),
        ('Nottingham', 'Nottingham'),
        ('Perth', 'Perth'),
        ('Pontefract', 'Pontefract'),
        ('Salisbury', 'Salisbury'),
        ('Redcar', 'Redcar'),
        ('Sandown Park', 'Sandown Park'),
        ('Stratford-On-Avon', 'Stratford-On-Avon'),
        ('Taunton', 'Taunton'),
        ('Thirsk', 'Thirsk'),
        ('Warwick', 'Warwick'),
        ('Wetherby', 'Wetherby'),
        ('Wincanton', 'Wincanton'),
        ('York', 'York'),
    }

    winx = models.ForeignKey(Winx, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=18, choices=STATUS_CHOICES, default='In Service')
    venue = models.CharField(max_length=18, choices=VENUES, default='Kempton')
    comments = models.TextField()

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"Entry: {self.date_added}"
