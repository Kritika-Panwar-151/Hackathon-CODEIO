from django.shortcuts import render
from .apps_data import APPS_DATA, compute_risk

def home(request):
    query = request.GET.get("q", "").strip()
    real_app = None
    fake_apps = []
    official_pkg = None

    # extract official app
    for app in APPS_DATA:
        if app["label"] == "genuine":
            real_app = app
            official_pkg = app["package"]
            break

    # compute scores
    if query:
        for app in APPS_DATA:
            if app["label"] == "fake":
                score, reasons = compute_risk(app, query, official_pkg)
                app_copy = app.copy()
                app_copy["risk_score"] = score
                app_copy["reasons"] = reasons
                fake_apps.append(app_copy)

    return render(request, "home.html", {
        "query": query,
        "real_app": real_app,
        "fake_apps": fake_apps
    })
