# Generated by Django 5.0.4 on 2024-04-23 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='DepartmentID',
            new_name='department_id',
        ),
        migrations.RenameField(
            model_name='departments',
            old_name='DepartmentName',
            new_name='department_name',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='DateOFJoining',
            new_name='date_of_joining',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='Department',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='EmployeeID',
            new_name='employee_id',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='EmployeeName',
            new_name='employee_name',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='PhotoFileName',
            new_name='photo_file_name',
        ),
    ]
