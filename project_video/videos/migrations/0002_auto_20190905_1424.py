# Generated by Django 2.2.4 on 2019-09-05 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, verbose_name='説明(空欄可)'),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/', verbose_name='サムネイル(空欄可)'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=255, verbose_name='動画タイトル'),
        ),
        migrations.AlterField(
            model_name='video',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日'),
        ),
        migrations.AlterField(
            model_name='video',
            name='upload',
            field=models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='ファイル'),
        ),
    ]
