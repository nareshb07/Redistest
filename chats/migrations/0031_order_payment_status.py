# Generated by Django 4.2.1 on 2023-09-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0030_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.CharField(null=True),
        ),
    ]
