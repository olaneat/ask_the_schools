# Generated by Django 2.0.5 on 2018-09-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0017_auto_20180911_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='school_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curriculum', models.CharField(choices=[('Bri', 'British'), ('Ame', 'American'), ('Bri & Ame', 'British American'), ('Ger', 'German'), ('Fre', 'French')], max_length=7)),
                ('facilites', models.CharField(max_length=10)),
                ('website', models.CharField(max_length=100)),
                ('extra_curriculum', models.CharField(max_length=20)),
                ('date_established', models.DateField(verbose_name='')),
                ('awards', models.CharField(help_text='kindly list the schools Awards', max_length=150)),
                ('Direction', models.CharField(help_text='give a brief description to your school ', max_length=100)),
            ],
        ),
    ]