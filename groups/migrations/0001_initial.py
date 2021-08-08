# Generated by Django 3.2.5 on 2021-08-02 02:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CertifyText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField()),
                ('text', models.TextField()),
                ('achievement', models.BooleanField(default=False)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='main.goal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CertifyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField()),
                ('image', models.ImageField(upload_to='certify_image/')),
                ('achievement', models.BooleanField(default=False)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.goal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CertifyFigure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField()),
                ('figure', models.IntegerField()),
                ('achievement', models.BooleanField(default=False)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='figures', to='main.goal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]