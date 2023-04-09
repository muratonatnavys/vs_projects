# Generated by Django 4.1.7 on 2023-04-02 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, null=True)),
                ('email', models.CharField(default=None, max_length=255, null=True)),
                ('subject', models.CharField(default=None, max_length=255, null=True)),
                ('message', models.CharField(default=None, max_length=255, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]