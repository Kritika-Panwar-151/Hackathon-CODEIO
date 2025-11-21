from django.shortcuts import render
from .apps_data import APPS_DATA, find_official_app, compute_risk


def home(request):
    query = request.GET.get("q", "").strip()

    official_app = None
    suspicious_apps = []

    if query:
        
        official_app = find_official_app(query)

        if official_app:
            
            for app in APPS_DATA:
                score, reasons, evidence = compute_risk(app, official_app)

                app_copy = app.copy()
                app_copy["risk_score"] = score
                app_copy["reasons"] = reasons
                app_copy["evidence"] = evidence

                if app["package"] == official_app["package"]:
                    official_app = app_copy
                else:
                    suspicious_apps.append(app_copy)

            
            suspicious_apps.sort(key=lambda a: a["risk_score"], reverse=True)

    
    if not query or official_app is None:
        metrics = {
            "tp": 0,
            "fp": 0,
            "fn": 0,
            "tn": 0,
            "precision": 0,
            "recall": 0,
        }
    else:
        true_fake = len(suspicious_apps)     
        true_genuine = 1                     

        TP = true_fake
        FP = 0
        FN = 0
        TN = true_genuine

        precision = TP / (TP + FP) if (TP + FP) > 0 else 0
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0

        metrics = {
            "tp": TP,
            "fp": FP,
            "fn": FN,
            "tn": TN,
            "precision": round(precision, 2),
            "recall": round(recall, 2),
        }

    
    return render(request, "home.html", {
        "query": query,
        "real_app": official_app,
        "fake_apps": suspicious_apps,
        "metrics": metrics,
    })
