from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
import joblib
import os
import json
from .models import IrrigationRecord

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
model = joblib.load(os.path.join(BASE_DIR, "irrigation_model.pkl"))

@login_required
def dashboard(request):
    prediction = None

    if request.method == "POST":
        moisture = float(request.POST.get("moisture"))
        temperature = float(request.POST.get("temperature"))
        humidity = float(request.POST.get("humidity"))

        result = model.predict([[moisture, temperature, humidity]])[0]

        prediction = "Irrigation Required" if result == 1 else "No Irrigation Needed"

        IrrigationRecord.objects.create(
            user=request.user,
            moisture=moisture,
            temperature=temperature,
            humidity=humidity,
            prediction=prediction
        )

    records = IrrigationRecord.objects.filter(user=request.user).order_by("-created_at")[:5]

    return render(request, "dashboard.html", {
        "prediction": prediction,
        "records": records
    })

@login_required
def analytics(request):
    records = IrrigationRecord.objects.filter(user=request.user).order_by("created_at")

    moisture = [r.moisture for r in records]
    labels = [r.created_at.strftime("%H:%M") for r in records]

    return render(request, "analytics.html", {
        "moisture": json.dumps(moisture),
        "labels": json.dumps(labels)
    })
@login_required
def add_sensor_data(request):
    if request.method == "POST":
        moisture = float(request.POST.get("moisture"))
        temperature = float(request.POST.get("temperature"))
        humidity = float(request.POST.get("humidity"))

        result = model.predict([[moisture, temperature, humidity]])[0]
        prediction = "Irrigation Required" if result == 1 else "No Irrigation Needed"

        IrrigationRecord.objects.create(
            user=request.user,
            moisture=moisture,
            temperature=temperature,
            humidity=humidity,
            prediction=prediction
        )

        return redirect("dashboard")

    return render(request, "add_sensor_data.html")
