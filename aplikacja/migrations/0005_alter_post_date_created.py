# Generated by Django 4.1.5 on 2023-01-28 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0004_alter_post_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
