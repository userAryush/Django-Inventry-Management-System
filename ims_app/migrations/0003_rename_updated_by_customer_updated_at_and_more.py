# Generated by Django 5.1.7 on 2025-03-25 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ims_app', '0002_customer_created_at_customer_updated_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='updated_by',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='updated_by',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='updated_by',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='product_type',
            old_name='updated_by',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='updated_by',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='sell',
            old_name='updated_by',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='updated_by',
            new_name='updated_at',
        ),
    ]
