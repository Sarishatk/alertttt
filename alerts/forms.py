from django import forms
from .models import Alert

class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ["date", "alert_name", "triggered_time", "tower", "other_tower", "update", "status"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "triggered_time": forms.TimeInput(attrs={"type": "time"}),
            "update": forms.Textarea(attrs={"rows": 3}),
        }

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("tower") == "Other" and not cleaned.get("other_tower", "").strip():
            self.add_error("other_tower", "Please enter the tower name.")
        if cleaned.get("tower") != "Other":
            cleaned["other_tower"] = ""
        return cleaned
