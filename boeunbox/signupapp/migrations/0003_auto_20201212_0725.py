# Generated by Django 3.1.2 on 2020-12-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupapp', '0002_boeun_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boeun_user',
            name='address',
            field=models.CharField(blank=True, max_length=200, verbose_name='주소'),
        ),
        migrations.AlterField(
            model_name='boeun_user',
            name='anniversary',
            field=models.CharField(blank=True, max_length=200, verbose_name='기념일'),
        ),
        migrations.AlterField(
            model_name='boeun_user',
            name='contact',
            field=models.CharField(blank=True, max_length=200, verbose_name='연락처'),
        ),
        migrations.AlterField(
            model_name='boeun_user',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=200, verbose_name='생년월일'),
        ),
        migrations.AlterField(
            model_name='boeun_user',
            name='etc',
            field=models.CharField(blank=True, max_length=200, verbose_name='기타사항'),
        ),
        migrations.AlterField(
            model_name='boeun_user',
            name='health',
            field=models.CharField(blank=True, max_length=200, verbose_name='건강상태'),
        ),
        migrations.AlterField(
            model_name='boeun_user',
            name='relation',
            field=models.CharField(blank=True, max_length=200, verbose_name='관계'),
        ),
    ]