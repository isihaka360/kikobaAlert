# Generated by Django 5.0.2 on 2024-03-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kikobaAlert', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='comfirm_password',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
