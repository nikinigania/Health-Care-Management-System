from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='gallery/')),
            ],
        ),
    ]
