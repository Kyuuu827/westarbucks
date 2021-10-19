# Generated by Django 3.2.7 on 2021-10-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(related_name='movies', to='movies.Actor'),
        ),
        migrations.DeleteModel(
            name='Actor_movie',
        ),
    ]
