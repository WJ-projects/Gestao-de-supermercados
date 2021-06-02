# Generated by Django 3.2 on 2021-06-02 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GDS', '0003_alter_funcionario_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.TextField(blank=True, max_length=255, null=True, verbose_name='Situação')),
                ('data_hora_postagem', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
