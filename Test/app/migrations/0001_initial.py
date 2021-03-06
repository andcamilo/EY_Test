# Generated by Django 3.0.2 on 2020-02-02 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100)),
                ('PathernalLastName', models.CharField(blank=True, max_length=100)),
                ('MathernalLastName', models.CharField(blank=True, max_length=100)),
                ('Edad', models.IntegerField(blank=True, default=0)),
                ('Cedula', models.CharField(blank=True, max_length=20)),
                ('Sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(blank=True, max_length=100)),
                ('Orden', models.IntegerField(default=0)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Persona')),
            ],
        ),
    ]
