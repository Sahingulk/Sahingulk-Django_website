# Generated by Django 3.2.9 on 2023-03-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_home',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
       # migrations.AlterField(
       #     model_name='blog',
       #     name='is_active',
        #    field=models.BooleanField(default=True),
       # ),
       # migrations.AlterField(
      #      model_name='category',
       #     name='name',
       #     field=models.CharField(max_length=160),
       # ),
    ]
