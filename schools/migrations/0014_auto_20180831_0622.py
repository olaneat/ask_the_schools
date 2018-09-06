# Generated by Django 2.0.5 on 2018-08-31 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0013_schools_fees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parents_remark',
            old_name='parents_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='parents_remark',
            name='School_in_review_name',
        ),
        migrations.AddField(
            model_name='parents_remark',
            name='school_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.Schools'),
        ),
        migrations.AlterField(
            model_name='parent_signup',
            name='first_name',
            field=models.CharField(help_text='enter your first name', max_length=200),
        ),
    ]
