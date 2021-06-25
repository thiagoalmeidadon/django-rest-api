# Generated by Django 3.2.4 on 2021-06-25 03:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id_livro', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('ano_lancamento', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('paginas', models.IntegerField()),
                ('empresa', models.CharField(max_length=255)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
