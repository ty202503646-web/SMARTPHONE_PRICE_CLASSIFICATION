import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SmartphoneForm
from .models import Prediction
from .utils import predict_price


PRICE_LABELS = {
    0: "Low-End Phone",
    1: "Budget Phone",
    2: "Mid-Range Phone",
    3: "Flagship Phone",
}


def predict_price_view(request):
    result = None
    form = SmartphoneForm()

    if request.method == "POST":
        form = SmartphoneForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            prediction = predict_price(data)

            result = PRICE_LABELS.get(prediction, prediction)

            Prediction.objects.create(
                battery_power=data["battery_power"],
                blue=data["blue"],
                clock_speed=data["clock_speed"],
                dual_sim=data["dual_sim"],
                fc=data["fc"],
                four_g=data["four_g"],
                int_memory=data["int_memory"],
                m_dep=data["m_dep"],
                mobile_wt=data["mobile_wt"],
                n_cores=data["n_cores"],
                pc=data["pc"],
                px_height=data["px_height"],
                px_width=data["px_width"],
                ram=data["ram"],
                sc_h=data["sc_h"],
                sc_w=data["sc_w"],
                talk_time=data["talk_time"],
                three_g=data["three_g"],
                touch_screen=data["touch_screen"],
                wifi=data["wifi"],
                prediction=prediction,
            )
            return redirect("dashboard")

    return render(
        request,
        "predictor/form.html",
        {
            "form": form,
            "result": result,
        },
    )


def history_view(request):
    history = Prediction.objects.all().order_by("-created_at")

    context = {
        "history": history,
        "low": history.filter(prediction=0).count(),
        "budget": history.filter(prediction=1).count(),
        "mid": history.filter(prediction=2).count(),
        "flagship": history.filter(prediction=3).count(),
    }

    return render(request, "predictor/dashboard.html", context)


def update_prediction(request, id):
    item = get_object_or_404(Prediction, id=id)

    if request.method == "POST":
        form = SmartphoneForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            prediction = predict_price(data)

            for field, value in data.items():
                setattr(item, field, value)

            item.prediction = prediction
            item.save()

            return redirect("dashboard")

    else:
        form = SmartphoneForm(
            initial={
                "battery_power": item.battery_power,
                "blue": item.blue,
                "clock_speed": item.clock_speed,
                "dual_sim": item.dual_sim,
                "fc": item.fc,
                "four_g": item.four_g,
                "int_memory": item.int_memory,
                "m_dep": item.m_dep,
                "mobile_wt": item.mobile_wt,
                "n_cores": item.n_cores,
                "pc": item.pc,
                "px_height": item.px_height,
                "px_width": item.px_width,
                "ram": item.ram,
                "sc_h": item.sc_h,
                "sc_w": item.sc_w,
                "talk_time": item.talk_time,
                "three_g": item.three_g,
                "touch_screen": item.touch_screen,
                "wifi": item.wifi,
            }
        )

    return render(
        request,
        "predictor/update.html",
        {
            "form": form,
            "item": item,
        },
    )


def delete_prediction(request, id):
    item = get_object_or_404(Prediction, id=id)
    item.delete()
    return redirect("dashboard")


def export_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="predictions.csv"'

    writer = csv.writer(response)

    writer.writerow([
        "Battery",
        "RAM",
        "Storage",
        "Prediction",
        "Date",
    ])

    for item in Prediction.objects.all():
        writer.writerow([
            item.battery_power,
            item.ram,
            item.int_memory,
            PRICE_LABELS.get(item.prediction, item.prediction),
            item.created_at,
        ])

    return response


def view_prediction(request, id):
    item = get_object_or_404(Prediction, id=id)

    return render(
        request,
        "predictor/view_prediction.html",
        {
            "item": item,
        },
    )