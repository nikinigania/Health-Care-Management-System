from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_doctor_expertize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='facebook',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='instagram',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='twitter',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
