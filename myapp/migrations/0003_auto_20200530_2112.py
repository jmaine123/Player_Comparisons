# Generated by Django 3.0.4 on 2020-05-30 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_debate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='debate',
            options={'managed': True},
        ),
        migrations.RenameField(
            model_name='debate',
            old_name='votes',
            new_name='p1_vote',
        ),
        migrations.AddField(
            model_name='debate',
            name='p2_vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='debate',
            name='user_pick',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterModelTable(
            name='debate',
            table='debate',
        ),
    ]