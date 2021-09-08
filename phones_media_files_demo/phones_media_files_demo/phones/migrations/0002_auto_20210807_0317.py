# Generated by Django 3.2.6 on 2021-08-07 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='image',
        ),
        migrations.CreateModel(
            name='PhoneImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='phones')),
                ('is_selected', models.BooleanField(default=False)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.phone')),
            ],
        ),
    ]