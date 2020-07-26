from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_auto_20190501_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='doctors/'),
            preserve_default=False,
        ),
    ]
