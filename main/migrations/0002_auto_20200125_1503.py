# Generated by Django 3.0.2 on 2020-01-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bandwidth',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='email_accounts',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='storage',
            field=models.IntegerField(default=1),
        ),
    ]