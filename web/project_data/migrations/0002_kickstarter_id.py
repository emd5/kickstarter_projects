# Generated by Django 2.1.1 on 2018-09-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kickstarter',
            name='ID',
            field=models.CharField(default=1, max_length=1024),
            preserve_default=False,
        ),
    ]
