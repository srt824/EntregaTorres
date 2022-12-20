# Generated by Django 4.1.4 on 2022-12-20 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMundial', '0008_rename_playoffs_fase_grupos_rename_lafinal_la_final'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tercer_puesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('versus', models.CharField(blank=True, max_length=60, null=True)),
                ('fecha', models.DateField()),
                ('estadio', models.CharField(blank=True, max_length=20, null=True)),
                ('arbitro', models.CharField(blank=True, max_length=30, null=True)),
                ('horario', models.TimeField()),
                ('resultado', models.CharField(blank=True, max_length=60, null=True)),
                ('ganador', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='grupos',
            old_name='GrupoA',
            new_name='grupoA',
        ),
        migrations.RenameField(
            model_name='grupos',
            old_name='GrupoB',
            new_name='grupoB',
        ),
        migrations.RenameField(
            model_name='grupos',
            old_name='GrupoC',
            new_name='grupoC',
        ),
        migrations.RenameField(
            model_name='grupos',
            old_name='GrupoD',
            new_name='grupoD',
        ),
        migrations.RenameField(
            model_name='grupos',
            old_name='GrupoE',
            new_name='grupoE',
        ),
        migrations.RenameField(
            model_name='grupos',
            old_name='GrupoF',
            new_name='grupoF',
        ),
        migrations.RenameField(
            model_name='grupos',
            old_name='GrupoG',
            new_name='grupoG',
        ),
        migrations.RenameField(
            model_name='grupos',
            old_name='GrupoH',
            new_name='grupoH',
        ),
        migrations.AddField(
            model_name='estadios',
            name='capacidad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
