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
    superwash = models.BooleanField(default=False)
    notes = models.CharField(max_length=200, blank=True)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    wash_id = models.ForeignKey(Wash, on_delete=models.CASCADE)
    weight_id = models.ForeignKey(Weight, on_delete=models.CASCADE)
    materials = models.ManyToManyField(Material)


class Color(models.Model):
    def __str__(self):
        name = str(self.yarntype) + ' ' + str(self.color)
        return name

    yarntype = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, null=True)
    col_nr = models.IntegerField(null=True)
    own_it = models.BooleanField(default=False)
    nr_in_stash = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True)
    yarnshop = models.ForeignKey(Yarnshop, on_delete=models.CASCADE)

class Swatch(models.Model):
    name = models.CharField(max_length=50)
    n_rows = models.IntegerField(blank=True, null=True)
    n_stitches = models.IntegerField(blank=True, null=True)
    n_rows_washed = models.IntegerField(blank=True, null=True)
    n_stitches_washed = models.IntegerField(blank=True, null=True)
    needlesize = models.ForeignKey(Needlesize, on_delete=models.CASCADE)
    yarn = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    notes = models.CharField(max_length=200, blank=True)


class Projectidea(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    link = models.CharField(max_length=200, blank=True)
    notes = models.CharField(max_length=200, blank=True)
    yarn = models.ManyToManyField(Yarn, blank=True)
    color = models.ManyToManyField(Color, blank=True)
    weight = models.ManyToManyField(Weight, blank=True)


class FinishedObject(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    for_who = models.CharField(max_length=50, blank=True)
    stichnr = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True)
    yarn = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    skeins_used = models.IntegerField(blank=True, null=True)
    color = models.ManyToManyField(Color, blank=True)
    needlsize = models.ManyToManyField(Needlesize)
