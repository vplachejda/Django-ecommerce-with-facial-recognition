# Generated by Django 3.1.7 on 2021-03-14 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210314_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.transaction'),
        ),
    ]
