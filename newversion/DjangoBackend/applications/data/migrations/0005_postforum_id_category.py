# Generated by Django 4.1.5 on 2023-01-26 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_forumcategories_remove_commentforum_delete_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postforum',
            name='id_category',
            field=models.ForeignKey(db_column='id_category', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='data.forumcategories'),
            preserve_default=False,
        ),
    ]