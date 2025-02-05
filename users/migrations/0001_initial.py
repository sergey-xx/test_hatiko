# Generated by Django 5.0.7 on 2025-01-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.PositiveBigIntegerField(unique=True, verbose_name='Идентификатор Telegram')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='Юзернейм телеграм')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=False, verbose_name='Доступ разрешен')),
            ],
            options={
                'verbose_name': 'Пользователь Telegram',
                'verbose_name_plural': 'Пользователи Telegram',
                'ordering': ('created_at',),
            },
        ),
    ]
