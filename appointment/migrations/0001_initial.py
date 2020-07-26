
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0012_auto_20190502_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('time', models.CharField(choices=[('morning', 'Morning'), ('evening', 'Evening')], max_length=10)),
                ('note', models.TextField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='hospital.Doctor')),
            ],
        ),
    ]
