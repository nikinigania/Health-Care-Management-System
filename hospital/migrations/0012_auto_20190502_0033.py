from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Galleries'},
        ),
    ]
