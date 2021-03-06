# Generated by Django 4.0.4 on 2022-07-16 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subasta_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('descripcion', models.CharField(max_length=240)),
                ('precio_minimo', models.IntegerField(blank=True, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='articulos_images')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subasta_app.categoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
