# Generated by Django 3.1.1 on 2020-10-19 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('author', models.CharField(max_length=2000)),
                ('tags', models.CharField(max_length=100)),
                ('book', models.FileField(upload_to='document')),
            ],
        ),
    ]
