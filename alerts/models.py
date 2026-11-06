from django.db import models

class Alert(models.Model):
    TOWER_CHOICES = [
        ("Linux", "Linux"),
        ("Windows", "Windows"),
        ("Network", "Network"),
        ("Tools", "Tools"),
        ("Other", "Other"),
    ]
    STATUS_CHOICES = [
        ("Open", "Open"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
        ("Closed", "Closed"),
    ]

    date = models.DateField()
    alert_name = models.CharField(max_length=200)
    triggered_time = models.TimeField()
    tower = models.CharField(max_length=20, choices=TOWER_CHOICES)
    other_tower = models.CharField(max_length=100, blank=True)
    update = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Open")
    entered_by = models.CharField(max_length=100, blank=True)
    last_updated_by = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.alert_name
