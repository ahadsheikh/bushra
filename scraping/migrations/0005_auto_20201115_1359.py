# Generated by Django 3.1.3 on 2020-11-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_auto_20201115_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]