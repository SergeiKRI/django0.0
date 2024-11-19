# Generated by Django 4.2.2 on 2024-11-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_blogrecord_count_views_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('name', 'category', 'price', 'date_created_at', 'date_updated_at'), 'permissions': [('can_unpublish_product', 'Can Unpublish Product')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AddField(
            model_name='products',
            name='status_public',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
