from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Alert",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateField()),
                ("alert_name", models.CharField(max_length=200)),
                ("triggered_time", models.TimeField()),
                ("tower", models.CharField(choices=[("Linux", "Linux"), ("Windows", "Windows"), ("Network", "Network"), ("Tools", "Tools"), ("Other", "Other")], max_length=20)),
                ("other_tower", models.CharField(blank=True, max_length=100)),
                ("update", models.TextField(blank=True)),
                ("status", models.CharField(choices=[("Open", "Open"), ("In Progress", "In Progress"), ("Resolved", "Resolved"), ("Closed", "Closed")], default="Open", max_length=20)),
                ("entered_by", models.CharField(blank=True, max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
