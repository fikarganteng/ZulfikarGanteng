# Generated by Django 3.2.8 on 2021-12-30 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artikel',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Artikel'},
        ),
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': 'Kategori'},
        ),
    ]
