# Generated by Django 4.1.5 on 2023-02-24 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdor', models.PositiveIntegerField()),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('narx', models.PositiveBigIntegerField()),
                ('tolandi', models.PositiveBigIntegerField()),
                ('qarz', models.PositiveBigIntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.client')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
                ('ombor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asosiy.ombor')),
            ],
        ),
    ]