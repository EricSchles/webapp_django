from django.db import models

class Gremlin_Attributes(models.Model):

    class Meta:
        app_label = 'gremlins'

    NAME = models.CharField(max_length=75)
    HEIGHT = models.DecimalField(max_digits=7, decimal_places=2)
    POWER = models.CharField(max_length=40)
    damageDone = models.CharField(max_length=200) # all the damage a given gremlin has done to people around danny


    def __unicode__(self):
        return "Gremlin {0} has height {1}, power {2} and has done this much damage: {3}".format(self.NAME, self.HEIGHT, self.POWER, self.damageDone)


