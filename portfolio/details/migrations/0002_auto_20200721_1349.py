# Generated by Django 3.0.8 on 2020-07-21 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialmediasettings',
            options={'verbose_name': 'Social media accounts'},
        ),
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(help_text='Your mobile number beginning with 0', max_length=255)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Contact Information',
            },
        ),
    ]
