# Generated by Django 2.2.22 on 2021-05-12 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_cms_pages', '0007_add_kyrgyz_and_russianand_dutch_language_choices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='teaser_de',
            new_name='hero_subtitle_de',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='teaser_en',
            new_name='hero_subtitle_en',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='subtitle_de',
            new_name='hero_title_de',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='subtitle_en',
            new_name='hero_title_en',
        ),
    ]