# Generated by Django 4.1.5 on 2023-01-10 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0003_remove_kitob_muallif_remove_record_talaba_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitob',
            name='muallif',
        ),
        migrations.AddField(
            model_name='kitob',
            name='muallif',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='asosiy.muallif'),
            preserve_default=False,
        ),
    ]