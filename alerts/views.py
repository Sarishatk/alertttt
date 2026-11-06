from django.shortcuts import render, redirect, get_object_or_404
from .models import Alert
from .forms import AlertForm

def records(request):
    alerts = Alert.objects.all().order_by("-date", "-triggered_time", "-id")
    return render(request, "alerts/records.html", {"alerts": alerts})

def add_alert(request):
    if request.method == "POST":
        form = AlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.entered_by = request.POST.get("entered_by", "").strip()
            alert.save()
            return redirect("records")
    else:
        form = AlertForm()
    return render(request, "alerts/form.html", {"form": form, "page_title": "Add Alert"})

def edit_alert(request, pk):
    alert = get_object_or_404(Alert, pk=pk)
    if request.method == "POST":
        form = AlertForm(request.POST, instance=alert)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.last_updated_by = request.POST.get("updated_by", "").strip()
            alert.save()
            return redirect("records")
    else:
        form = AlertForm(instance=alert)
    return render(request, "alerts/form.html", {"form": form, "page_title": "Edit Alert"})

def delete_alert(request, pk):
    alert = get_object_or_404(Alert, pk=pk)
    if request.method == "POST":
        alert.delete()
        return redirect("records")
    return render(request, "alerts/delete.html", {"alert": alert})
