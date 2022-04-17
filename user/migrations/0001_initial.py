# Generated by Django 3.2 on 2022-04-15 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('fullname', models.CharField(blank=True, max_length=50, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='media/user/avatar/%Y/%m/%d')),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('sex', models.CharField(choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('-', '-')], default='-', max_length=10)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
