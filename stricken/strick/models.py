from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    """manufacturer of a yarn"""

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Wash(models.Model):
    """Washing instrucion"""

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Material(models.Model):
    """material/s that a yarn consists of"""

    name = models.CharField(max_length=50, unique=True)
    notes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Yarnshop(models.Model):
    """vendor where the yarn was bought"""

    name = models.CharField(max_length=50, unique=True)
    notes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Weight(models.Model):
    """Weightclass, name is pk"""

    name = models.CharField(max_length=50, unique=True, primary_key=True)

    def __str__(self):
        return self.name

class Needlesize(models.Model):
    """neeldesize in mm, name is pk"""

    name = models.CharField(max_length=50, unique=True, primary_key=True)

    def __str__(self):
        return self.name

class Yarn(models.Model):
    """type of yarn"""

    name = models.CharField(max_length=50, unique=True)
    superwash = models.BooleanField(default=False)
    yardage = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    wash = models.ForeignKey(Wash, on_delete=models.CASCADE)
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE)
    materials = models.ManyToManyField(Material)

    def __str__(self):
        return self.name

class Color(models.Model):
    """colorway of a yarn"""

    yarntype = models.ForeignKey(Yarn, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    col_nr = models.IntegerField(null=True)
    own_it = models.BooleanField(default=False)
    quantity = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True)
    yarnshop = models.ForeignKey(Yarnshop, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        name = str(self.yarntype) + ' ' + str(self.color)
        return name


class Swatch(models.Model):
    """swatch made with a yarn"""
    name = models.CharField(max_length=50, unique=True)
    n_rows = models.IntegerField(blank=True, null=True)
    n_stitches = models.IntegerField(blank=True, null=True)
    n_rows_washed = models.IntegerField(blank=True, null=True)
    n_stitches_washed = models.IntegerField(blank=True, null=True)
    needlesize = models.ForeignKey(Needlesize, on_delete=models.CASCADE)
    yarn = models.ForeignKey(Yarn, null=True, on_delete=models.SET_NULL)
    notes = models.CharField(max_length=200, blank=True)


class Projectidea(models.Model):
    """idea for a project and yarn/color to use"""

    name = models.CharField(max_length=50, unique=True)
    link = models.CharField(max_length=200, blank=True)
    notes = models.CharField(max_length=200, blank=True)
    yardage_needed = models.IntegerField(blank=True, null=True)
    skeins_needed = models.IntegerField(blank=True, null=True)
    yarn = models.ForeignKey(Yarn, on_delete=models.CASCADE,  blank=True, null=True)
    color = models.ManyToManyField(Color, blank=True)
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class FinishedObject(models.Model):
    """finished item"""

    name = models.CharField(max_length=50, unique=True)
    for_who = models.CharField(max_length=50, blank=True)
    stichnr = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=200, blank=True)
    yarn = models.ForeignKey(Yarn, null=True, on_delete=models.SET_NULL)
    skeins_used = models.IntegerField(blank=True, null=True)
    color = models.ManyToManyField(Color, blank=True)
    needlsize = models.ManyToManyField(Needlesize)

    def __str__(self):
        return self.name