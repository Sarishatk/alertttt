from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("alerts", "0001_initial")]
    operations = [
        migrations.AddField(
            model_name="alert",
            name="last_updated_by",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="alert",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
