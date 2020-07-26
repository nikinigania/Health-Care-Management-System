from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='services/')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='services/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='services/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name_plural': 'Slider'},
        ),
    ]
