from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_auto_20190501_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='cover',
            field=models.ImageField(default='cover1.img', upload_to='services/'),
            preserve_default=False,
        ),
    ]
