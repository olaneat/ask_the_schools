# Generated by Django 2.1.1 on 2018-10-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0021_auto_20180921_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school_data',
            old_name='curriculum',
            new_name='CURRICULUM',
        ),
        migrations.RenameField(
            model_name='school_data',
            old_name='Direction',
            new_name='DIRECTION',
        ),
        migrations.RenameField(
            model_name='school_data',
            old_name='extra_curriculum',
            new_name='EXTRA_CURRICULUM',
        ),
        migrations.RenameField(
            model_name='schools',
            old_name='address',
            new_name='ADDRESS',
        ),
        migrations.RenameField(
            model_name='schools',
            old_name='advantage',
            new_name='ADVANTAGE',
        ),
        migrations.RenameField(
            model_name='schools',
            old_name='badge',
            new_name='BADGE',
        ),
        migrations.RenameField(
            model_name='schools',
            old_name='level',
            new_name='LEVEL',
        ),
        migrations.RenameField(
            model_name='schools',
            old_name='school_Phone_Num',
            new_name='PHONE',
        ),
        migrations.RenameField(
            model_name='schools',
            old_name='state',
            new_name='STATE',
        ),
        migrations.RenameField(
            model_name='schools',
            old_name='town',
            new_name='TOWN',
        ),
        migrations.RenameField(
            model_name='schools',
            old_name='video',
            new_name='VIDEO',
        ),
        migrations.RemoveField(
            model_name='school_data',
            name='awards',
        ),
        migrations.RemoveField(
            model_name='school_data',
            name='date_established',
        ),
        migrations.RemoveField(
            model_name='school_data',
            name='facilites',
        ),
        migrations.RemoveField(
            model_name='school_data',
            name='website',
        ),
        migrations.RemoveField(
            model_name='schools',
            name='fees_range',
        ),
        migrations.RemoveField(
            model_name='schools',
            name='motto',
        ),
        migrations.RemoveField(
            model_name='schools',
            name='name',
        ),
        migrations.RemoveField(
            model_name='schools',
            name='school_email',
        ),
        migrations.RemoveField(
            model_name='schools',
            name='status',
        ),
        migrations.AddField(
            model_name='school_data',
            name='AWARDS',
            field=models.CharField(blank=True, help_text='kindly list the schools Awards', max_length=150),
        ),
        migrations.AddField(
            model_name='school_data',
            name='SPORT_ACTIVITIES',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='school_data',
            name='WEBSITE',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='schools',
            name='EMAIL',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='schools',
            name='FEES_RANGE',
            field=models.CharField(choices=[('#51,000.00 - #100,000.00', '#51,000.00 - #100,000.00'), ('#101,000.00 - 200,000.00', '#101,000.00 - 200,000.00'), ('#201,000.00  - 300,000.00', '#201,000.00  - 300,000.00'), ('#301,000.00  - 400,000.00', '#301,000.00  - 400,000.00'), ('#401,000.00  - 500,000.00', '#401,000.00  - 500,000.00'), ('#501,000.00  - 600,000.00', '#501,000.00  - 600,000.00'), ('#601,000.00  - 700,000.00', '#601,000.00  - 700,000.00'), ('#701,000.00  - 800,000.00', '#701,000.00  - 800,000.00'), ('#801,000.00  - 900,000.00', '#801,000.00  - 900,000.00'), ('#901,000.00  - 1,000,000.00', '#901,000.00  - 1,000,000.00')], max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='schools',
            name='MOTTO',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='schools',
            name='NAME',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='schools',
            name='STATUS',
            field=models.CharField(blank=True, choices=[('Day', 'Day'), ('Boarding', 'Boarding'), ('Boarding and Day', 'Boarding and Day')], max_length=20),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='full_name',
            field=models.CharField(max_length=300),
        ),
    ]