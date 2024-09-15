# Generated by Django 4.2.16 on 2024-09-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_nav_banner_created_time_banner_updated_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nav",
            name="position",
            field=models.IntegerField(
                choices=[(1, "顶部导航"), (2, "底部导航")],
                default=1,
                verbose_name="导航位置",
            ),
        ),
    ]