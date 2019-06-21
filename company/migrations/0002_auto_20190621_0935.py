# Generated by Django 2.2.2 on 2019-06-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ('name',), 'verbose_name': 'company', 'verbose_name_plural': 'companies'},
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='orgNr',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]