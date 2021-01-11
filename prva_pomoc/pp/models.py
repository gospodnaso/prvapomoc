from django.db import models

class User(models.Model):
    ime = models.CharField(max_length=100)
    vod = models.CharField(max_length=100)
    hashh = models.CharField(max_length=100, unique=True, default="") 
    oddal_kt1 = models.BooleanField(default=False)
    oddal_kt2 = models.BooleanField(default=False)
    oddal_kt3 = models.BooleanField(default=False)
    oddal_kt4 = models.BooleanField(default=False)
    oddal_kt5 = models.BooleanField(default=False)
    oddal_kt6 = models.BooleanField(default=False)
    oddal_kt7 = models.BooleanField(default=False)
    oddal_kt8 = models.BooleanField(default=False)
    oddal_kt9 = models.BooleanField(default=False)
    tocke_kt1 = models.IntegerField(default=0)
    tocke_kt2 = models.IntegerField(default=0)
    tocke_kt3 = models.IntegerField(default=0)
    tocke_kt4 = models.IntegerField(default=0)
    tocke_kt5 = models.IntegerField(default=0)
    tocke_kt6 = models.IntegerField(default=0)
    tocke_kt7 = models.IntegerField(default=0)
    tocke_kt8 = models.IntegerField(default=0)
    tocke_kt9 = models.IntegerField(default=0)
    beseda_kt7 = models.CharField(max_length=100, default="")
    sum_tocke = models.IntegerField(default=0)
    def __str__(self):
        return (self.ime + ';'+self.vod)
    def cal_sum(self):
        out = 0
        out += self.tocke_kt1
        out += self.tocke_kt2
        out += self.tocke_kt3
        out += self.tocke_kt4
        out += self.tocke_kt5
        out += self.tocke_kt6
        out += self.tocke_kt7
        out += self.tocke_kt8
        out += self.tocke_kt9
        return out

