# Generated by Django 3.2.9 on 2023-03-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230311_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
       # migrations.AlterField(
       #     model_name='blog',
       #     name='is_active',
       #     field=models.BooleanField(default=True),
       # ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
      # migrations.AlterField(
      #      model_name='category',
       #     name='name',
      #     field=models.CharField(max_length=160),
      #  ),
    ]
