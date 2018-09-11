from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True)


class Wash(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True)

class Material(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True)
    notes = models.CharField(max_length=200, blank=True)

class Yarnshop(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True)
    notes = models.CharField(max_length=200, blank=True)

class Weight(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True, primary_key=True)

class Needlesize(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True, primary_key=True)




class Yarn(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=50, null=True)
    col_nr = models.IntegerField(null=True)
    superwash = models.BooleanField
    own_it = models.BooleanField
    nr_in_stash = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    wash_id = models.ForeignKey(Wash, on_delete=models.CASCADE)
    weight_id = models.ForeignKey(Weight, on_delete=models.CASCADE)
    materials = models.ManyToManyField(Material)
    yarnshops = models.ManyToManyField(Yarnshop, blank=True)

class Swatch(models.Model):
    name = models.CharField(max_length=50)
    n_rows = models.IntegerField
    n_stitches = models.IntegerField
    n_rows_washed = models.IntegerField
    n_stitches_washed = models.IntegerField
    needlesize_id = models.ForeignKey(Needlesize, on_delete=models.CASCADE)
    yarn_id = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    notes = models.CharField(max_length=200, blank=True)


class Projectideas(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    link = models.CharField(max_length=200, blank=True)
    notes = models.CharField(max_length=200, blank=True)
    yarn_id = models.ManyToManyField(Yarn, blank=True)
    weight_id = models.ManyToManyField(Weight, blank=True)


class FinishedObject(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    for_who = models.CharField(max_length=50, blank=True)
    stichnr = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True)
    yarn_id = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    needlsize_id = models.ManyToManyField(Needlesize)













