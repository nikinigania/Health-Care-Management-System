from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0008_doctor_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.TextField(default='The doctor is highly qualified'),
            preserve_default=False,
        ),
    ]
