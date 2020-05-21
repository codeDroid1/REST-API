# Generated by Django 3.0.6 on 2020-05-21 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schools', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='school_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.School'),
        ),
    ]