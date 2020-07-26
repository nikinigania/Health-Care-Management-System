from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_service_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expertize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('speciality', models.CharField(max_length=120)),
                ('details', models.TextField()),
                ('twitter', models.CharField(max_length=120)),
                ('facebook', models.CharField(max_length=120)),
                ('instagram', models.CharField(max_length=120)),
                ('expertize', models.ManyToManyField(related_name='doctors', to='hospital.Expertize')),
            ],
        ),
    ]
