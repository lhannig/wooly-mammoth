# Generated by Django 2.1.2 on 2018-10-19 14:59

from django.db import migrations

def create_weights(apps, schema_editor):
    """create yarnweights"""

    Weight = apps.get_model('Backend', 'Weight')
    lace = Weight(name='Lace')
    lace.save()
    lightfingering = Weight(name='Light Fingering')
    lightfingering.save()
    fingering = Weight(name='Fingering')
    fingering.save()
    sport = Weight(name='Sport')
    sport.save()
    dk = Weight(name='DK')
    dk.save()
    worsted = Weight(name='Worsted')
    worsted.save()
    aran = Weight(name='Aran')
    aran.save()
    bulky = Weight(name='Bulky')
    bulky.save()
    superbulky = Weight(name='Super Bulky')
    superbulky.save()

def create_wash(apps, schema_editor):
    """create washing types"""

    Wash = apps.get_model('Backend', 'Wash')
    hw = Wash(name='Handwash')
    mwc = Wash(name='Machine wash gentle 30 deg')
    mww = Wash(name='Machine wash gentle 40 deg')
    mwh = Wash(name='Machine wash 60 deg')
    hw.save()
    mwc.save()
    mww.save()
    mwh.save()


def create_needlesizes(apps, shema_editor):
    """create needlesizes"""

    Needlesize = apps.get_model('Backend', 'Needlesize')
    n1 = Needlesize(name='1 mm')
    n1.save()
    n125 = Needlesize(name='1,25 mm')
    n125.save()
    n15 = Needlesize(name='1,5 mm')
    n15.save()
    n175 = Needlesize(name='1,75 mm')
    n175.save()
    n2 = Needlesize(name='2 mm')
    n2.save()
    n225 = Needlesize(name='2,25 mm')
    n225.save()
    n25 = Needlesize(name='2,5 mm')
    n25.save()
    n275 = Needlesize(name='2,75 mm')
    n275.save()
    n3 = Needlesize(name='3 mm')
    n3.save()
    n325 = Needlesize(name='3,25 mm')
    n325.save()
    n35 = Needlesize(name='3,5 mm')
    n35.save()
    n375 = Needlesize(name='3,75 mm')
    n375.save()
    n4 = Needlesize(name='4 mm')
    n4.save()
    n425 = Needlesize(name='4,25 mm')
    n425.save()
    n45 = Needlesize(name='4,5 mm')
    n45.save()
    n475 = Needlesize(name='4,75 mm')
    n475.save()
    n5 = Needlesize(name='5 mm')
    n5.save()
    n525 = Needlesize(name='5,25 mm')
    n525.save()
    n55 = Needlesize(name='5,5 mm')
    n55.save()
    n575 = Needlesize(name='5,75 mm')
    n575.save()
    n6 = Needlesize(name='6 mm')
    n6.save()
    n625 = Needlesize(name='6,25 mm')
    n625.save()
    n65 = Needlesize(name='6,5 mm')
    n65.save()
    n675 = Needlesize(name='6,75 mm')
    n675.save()
    n7 = Needlesize(name='7 mm')
    n7.save()
    n75 = Needlesize(name='7,5 mm')
    n75.save()
    n725 = Needlesize(name='7,25 mm')
    n725.save()
    n775 = Needlesize(name='7,75 mm')
    n775.save()
    n8 = Needlesize(name='8 mm')
    n8.save()
    n825 = Needlesize(name='8,25 mm')
    n825.save()
    n85 = Needlesize(name='8,5 mm')
    n85.save()
    n875 = Needlesize(name='8,75 mm')
    n875.save()
    n9 = Needlesize(name='9 mm')
    n9.save()
    n925 = Needlesize(name='9,25 mm')
    n925.save()
    n95 = Needlesize(name='9,5 mm')
    n95.save()
    n975 = Needlesize(name='9,75 mm')
    n975.save()
    n10 = Needlesize(name='10 mm')
    n10.save()




class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0004_auto_20181015_1347'),
    ]

    operations = [migrations.RunPython(create_weights),
                  migrations.RunPython(create_wash),
                  migrations.RunPython(create_needlesizes)
    ]
