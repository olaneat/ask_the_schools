# Generated by Django 2.0.5 on 2018-09-11 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0016_auto_20180911_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schools',
            name='info',
        ),
        migrations.AddField(
            model_name='schools',
            name='advantage',
            field=models.TextField(help_text='what do parents tend to benefit  by entrusting their children in your school not more than 1000 characters', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='schools',
            name='level',
            field=models.CharField(choices=[('Pri', 'Primary'), ('Sec', 'Secondary'), ('Pri and Sec', 'Primary and Secondary')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='schools',
            name='motto',
            field=models.CharField(help_text='enter the school motto above ', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='schools',
            name='school_Num',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='schools',
            name='state',
            field=models.CharField(choices=[('ABI', 'ABIA'), ('ADA', 'ADAMAWA'), ('AKW', 'AKWA IBOM'), ('ANA', 'ANAMBRA'), ('BAU', 'BAUCHI'), ('BAY', 'BAYELSA'), ('BEN', 'BENUE'), ('BOR', 'BORNO'), ('CRO', 'CROSS RIVER'), ('DEL', 'DELTA'), ('EBO', 'EBONYI'), ('EDO', 'EDO'), ('EKI', 'EKITI'), ('ENU', 'ENUGU'), ('GOM', 'GOMBE'), ('IMO', 'IMO'), ('JIG', 'JIGAWA'), ('KAD', 'KADUNA'), ('KAN', 'KANO'), ('KAT', 'KATSINA'), ('KEB', 'KEBBI'), ('KOG', 'KOGI'), ('KWA', 'KWARA'), ('LAG', 'LAGOS'), ('NAS', 'NASARAWA'), ('NIG', 'NIGER'), ('OGU', 'OGUN'), ('OND', 'ONDO'), ('OSU', 'OSUN'), ('OYO', 'OYO'), ('PLA', 'PLATEAU'), ('RIV', 'RIVERS'), ('SOK', 'SOKOTO'), ('TAR', 'TARABA'), ('YOB', 'YOBE'), ('ZAM', 'ZAMFARA'), ('FCT', 'FEDERAL CAPITAL TERRITORY')], max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='schools',
            name='town',
            field=models.CharField(help_text='enter the Local Government Area', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='schools',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
