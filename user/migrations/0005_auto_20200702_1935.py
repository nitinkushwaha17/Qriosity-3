# Generated by Django 3.0.7 on 2020-07-02 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200702_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='question_level',
            field=models.IntegerField(default=1),
        ),
    ]