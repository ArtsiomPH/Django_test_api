# Generated by Django 4.1.2 on 2022-10-21 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_user_age_gte_0_remove_user_age_user_height'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name']},
        ),
    ]
