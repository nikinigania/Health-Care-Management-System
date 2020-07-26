from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20190501_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='items',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hospital.Item'),
            preserve_default=False,
        ),
    ]
