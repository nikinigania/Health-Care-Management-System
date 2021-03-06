from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=150)),
                ('slogan', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='sliders/')),
            ],
        ),
    ]
