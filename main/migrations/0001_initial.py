# Generated by Django 3.2.5 on 2021-08-02 02:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('study', 'study'), ('hobby', 'hobby'), ('etc', 'etc')], max_length=50)),
                ('certify_method', models.CharField(choices=[('image', 'image'), ('text', 'text'), ('figure', 'figure')], max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created', models.DateField()),
                ('start_date', models.DateField()),
                ('fee', models.IntegerField(default=500)),
                ('value', models.IntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=10, null=True)),
                ('criteria', models.BooleanField(default=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('member', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]