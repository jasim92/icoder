# Generated by Django 3.1.1 on 2020-09-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('msg', models.TextField(max_length=2000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
