from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_service_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='items',
        ),
        migrations.AddField(
            model_name='service',
            name='items',
            field=models.ManyToManyField(to='hospital.Item'),
        ),
    ]
