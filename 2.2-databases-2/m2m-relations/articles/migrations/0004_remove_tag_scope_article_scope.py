# Generated by Django 4.2 on 2023-05-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_tag_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='scope',
        ),
        migrations.AddField(
            model_name='article',
            name='scope',
            field=models.ManyToManyField(through='articles.Scope', to='articles.tag'),
        ),
    ]
