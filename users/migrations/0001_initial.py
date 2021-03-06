# Generated by Django 2.1.5 on 2019-01-10 16:25

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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arg', models.CharField(max_length=128, verbose_name='机构')),
                ('tel', models.CharField(max_length=15, verbose_name='电话')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user',
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
    ]
