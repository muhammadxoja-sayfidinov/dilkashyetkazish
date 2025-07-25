# Generated by Django 5.2.4 on 2025-07-22 11:09

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chef_panel', '0003_botsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botsettings',
            name='broadcast_message_text',
            field=models.TextField(blank=True, help_text="Barcha foydalanuvchilarga yuborilishi mumkin bo'lgan e'lon matni", null=True, verbose_name="E'lon matni"),
        ),
        migrations.AlterField(
            model_name='botsettings',
            name='delivery_base_cost',
            field=models.DecimalField(decimal_places=2, default=5000, help_text='Har qanday masofada minimal yetkazib berish narxi', max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name="Yetkazib berish boshlang'ich narxi (so'm)"),
        ),
        migrations.AlterField(
            model_name='botsettings',
            name='delivery_cost_per_extra_km_block',
            field=models.DecimalField(decimal_places=2, default=6000, help_text="Birinchi kilometrdan keyin har km uchun qo'shimcha to'lov", max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name="Har km uchun qo'shimcha narx (so'm)"),
        ),
        migrations.AlterField(
            model_name='botsettings',
            name='delivery_max_radius_km',
            field=models.FloatField(default=10.0, help_text="Bu masofadan uzoqroqqa yetkazib berish yo'q", validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Maksimal yetkazib berish radiusi (km)'),
        ),
        migrations.AlterField(
            model_name='botsettings',
            name='service_end_time',
            field=models.TimeField(default=datetime.time(22, 0), help_text='Bot qaysi vaqtgacha buyurtma qabul qiladi', verbose_name='Xizmat tugash vaqti'),
        ),
        migrations.AlterField(
            model_name='botsettings',
            name='service_start_time',
            field=models.TimeField(default=datetime.time(10, 0), help_text='Bot qaysi vaqtdan buyurtma qabul qilishni boshlaydi', verbose_name='Xizmat boshlanish vaqti'),
        ),
    ]
