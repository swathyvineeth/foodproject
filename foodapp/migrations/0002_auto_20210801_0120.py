# Generated by Django 3.2.4 on 2021-07-31 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
