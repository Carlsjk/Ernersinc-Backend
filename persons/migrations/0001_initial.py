# Generated by Django 4.0.3 on 2023-01-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('CÉDULA DE CIUDADANÍA', 'Cc'), ('PASAPORTE', 'Pp'), ('CÉDULA DE EXTRANJERÍA', 'Ce')], default='CÉDULA DE CIUDADANÍA', max_length=255)),
                ('document', models.CharField(max_length=50, unique=True)),
                ('names', models.CharField(max_length=255)),
                ('last_names', models.CharField(max_length=255)),
                ('hobbie', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
