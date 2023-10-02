# Generated by Django 4.2.2 on 2023-10-01 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('HORROR', 'horror'), ('COMEDY', 'comedy'), ('ROMANCE', 'romance'), ('ACTION', 'action')], max_length=20, verbose_name='the genre of this book')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.book')),
            ],
        ),
    ]