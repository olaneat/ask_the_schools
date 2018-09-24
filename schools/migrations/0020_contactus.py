# Generated by Django 2.1.1 on 2018-09-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0019_auto_20180914_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(help_text='fill in your full name', max_length=300)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('comment', models.TextField(max_length=1000)),
            ],
        ),
    ]