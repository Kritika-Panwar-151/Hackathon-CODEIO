
from difflib import SequenceMatcher
from pathlib import Path

from django.conf import settings
from PIL import Image
import imagehash


APPS_DATA = [
    {
        "name": "PhonePe UPI, Payment, Recharge",
        "package": "com.phonepe.app",
        "publisher": "PhonePe Pvt. Ltd",
        "description": "Official UPI payments, recharge, bill pay app.",
        "permissions": ["SMS", "Location", "Contacts", "Camera", "Storage", "Accounts", "Call", "Microphone"],
        "rating": 4.4,
        "installs": "500M+",
        "icon_path": "phonepe_official.webp",
        "store_url": "https://play.google.com/store/apps/details?id=com.phonepe.app",
    },
    {
        "name": "PhonePe Update 2025",
        "package": "com.phonepe.update.secure",
        "publisher": "PhonePe Support Team",
        "description": "Update your PhonePe app to get cashback rewards.",
        "permissions": ["READ_SMS", "READ_CONTACTS", "READ_CALL_LOG", "INTERNET"],
        "rating": 2.1,
        "installs": "50K+",
        "icon_path": "fake_update.avif",
        "store_url": "https://play.google.com/store/apps/details?id=com.phonepe.update.secure",
    },
    {
        "name": "PhonePay Free Cashback",
        "package": "com.phonepay.cashback.free",
        "publisher": "UPI Rewards Inc",
        "description": "Get instant cashback by updating your UPI app.",
        "permissions": ["READ_SMS", "RECORD_AUDIO", "ACCESS_FINE_LOCATION"],
        "rating": 1.9,
        "installs": "10K+",
        "icon_path": "fake_cashback.webp",
        "store_url": "https://play.google.com/store/apps/details?id=com.phonepay.cashback.free",
    },
    {
        "name": "PhonePe Guide & Tricks 2025",
        "package": "com.phonepe.tricks.learn",
        "publisher": "UPI Helper",
        "description": "Learn tricks to earn money using PhonePe.",
        "permissions": ["INTERNET", "READ_CONTACTS"],
        "rating": 3.0,
        "installs": "100K+",
        "icon_path": "fake_tricks.jpeg",
        "store_url": "https://play.google.com/store/apps/details?id=com.phonepe.tricks.learn",
    },
    {
        "name": "ФhonePe UPI Original 2025",  # Cyrillic F
        "package": "com.phonepe.original.upi",
        "publisher": "PhonePe India Org",
        "description": "This is PhonePe official UPI app.",
        "permissions": ["READ_SMS", "READ_CALL_LOG"],
        "rating": 2.8,
        "installs": "5K+",
        "icon_path": "fake_lookalike.jpeg",
        "store_url": "https://play.google.com/store/apps/details?id=com.phonepe.original.upi",
    },
    {
        "name": "PhonePe UPI Banking Pro",
        "package": "com.phonepe.banking.pro",
        "publisher": "Pro Banking Apps",
        "description": "Advanced PhonePe banking features with unlimited cashback.",
        "permissions": ["READ_SMS", "READ_CONTACTS", "RECORD_AUDIO", "WRITE_SETTINGS"],
        "rating": 1.6,
        "installs": "1K+",
        "icon_path": "fake_banking.jpeg",
        "store_url": "https://play.google.com/store/apps/details?id=com.phonepe.banking.pro",
    },
    {
        "name": "PhonePe UPI Update Required",
        "package": "com.phonepe.update.required",
        "publisher": "SecureUpdate Ltd",
        "description": "Security update required! Install now.",
        "permissions": ["READ_SMS", "READ_CONTACTS", "WRITE_SETTINGS"],
        "rating": 1.5,
        "installs": "2K+",
        "icon_path": "fake_warning.jpeg",
        "store_url": "https://play.google.com/store/apps/details?id=com.phonepe.update.required",
    },
]


ICON_CACHE = {}  


def get_icon_hash(icon_filename: str):
    """Return perceptual hash of an icon, or None if can't load."""
    if icon_filename in ICON_CACHE:
        return ICON_CACHE[icon_filename]

    icon_path = Path(settings.BASE_DIR) / "app" / "icons" / icon_filename
    try:
        img = Image.open(icon_path)
        h = imagehash.phash(img)
        ICON_CACHE[icon_filename] = h
        return h
    except Exception:
        ICON_CACHE[icon_filename] = None
        return None


def name_similarity(a: str, b: str) -> float:
    """Fuzzy similarity between two strings in [0,1]."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def is_high_installs(installs: str) -> bool:
    """Very rough heuristic for 'big' apps."""
    s = installs.upper()
    return ("M" in s) or ("CR" in s) or ("B" in s)




def find_official_app(query: str):
    """
    Given a brand name or package ID typed by user,
    pick the best matching app from APPS_DATA as the 'official' reference.
    """
    q = query.lower().strip()
    best_app = None
    best_score = -1.0

    for app in APPS_DATA:
        name_sim = name_similarity(q, app["name"])
        pkg = app["package"].lower()

        pkg_bonus = 0.0
        if q == pkg:
            pkg_bonus = 0.7
        elif q in pkg:
            pkg_bonus = 0.4
        elif q in app["name"].lower():
            pkg_bonus = 0.2

        rating_bonus = 0.2 if app["rating"] >= 4.0 else 0.0
        installs_bonus = 0.3 if is_high_installs(app["installs"]) else 0.0

        score = name_sim + pkg_bonus + rating_bonus + installs_bonus

        if score > best_score:
            best_score = score
            best_app = app

    return best_app




def compute_risk(app: dict, official: dict):
    """
    Compare one candidate app against the detected official app.
    Return:
      risk_score (0–100),
      reasons (list of strings for UI),
      evidence (dict for JSON/table)
    """
   
    if app["package"] == official["package"]:
        evidence = {
            "app_name": app["name"],
            "package_id": app["package"],
            "store_url": app.get("store_url", ""),
            "name_similarity": 1.0,
            "publisher_similarity": 1.0,
            "package_similarity": 1.0,
            "icon_hash_diff": 0,
            "official_icon_hash": str(get_icon_hash(official["icon_path"]) or ""),
            "candidate_icon_hash": str(get_icon_hash(app["icon_path"]) or ""),
            "permission_risk_points": 0,
            "install_risk_points": 0,
            "rating_risk_points": 0,
            "total_score": 0,
        }
        return 0, ["Chosen as baseline official app based on highest similarity and popularity."], evidence

    score = 0
    reasons = []

    
    name_sim = name_similarity(app["name"], official["name"])
    pkg_sim = name_similarity(app["package"], official["package"])
    pub_sim = name_similarity(app["publisher"], official["publisher"])

    name_points = 0
    if name_sim >= 0.8:
        name_points = 25
        reasons.append(f"App name very similar to official ({name_sim:.2f}).")
    elif name_sim >= 0.5:
        name_points = 10
        reasons.append(f"App name partially similar to official ({name_sim:.2f}).")
    else:
        reasons.append(f"App name not very similar to official ({name_sim:.2f}).")
    score += name_points

    package_points = 0
    if app["package"] != official["package"]:
        package_points = 25
        reasons.append("Package ID is different from the official app.")
        score += package_points

    pub_mismatch_points = 0
    if app["publisher"].lower().strip() != official["publisher"].lower().strip():
        pub_mismatch_points = 15
        reasons.append("Publisher does not match the official developer.")
        score += pub_mismatch_points

    
    suspicious_pub_points = 0
    suspicious_keywords = ("update", "helper", "lite", "pro", "reward", "cashback", "guide", "trick")
    app_pub_lower = app["publisher"].lower()
    if any(k in app_pub_lower for k in suspicious_keywords):
        suspicious_pub_points = 10
        reasons.append("Publisher name contains suspicious words (update/guide/reward/etc.).")
        score += suspicious_pub_points

    
    off_hash = get_icon_hash(official["icon_path"])
    app_hash = get_icon_hash(app["icon_path"])
    icon_diff = None
    icon_points = 0

    if off_hash and app_hash:
        icon_diff = off_hash - app_hash
        if icon_diff <= 5:
            icon_points = 25
            reasons.append(f"Icon almost identical to official (hash difference = {icon_diff}).")
        elif icon_diff <= 15:
            icon_points = 10
            reasons.append(f"Icon visually similar to official (hash difference = {icon_diff}).")
        else:
            reasons.append(f"Icon looks different from official (hash difference = {icon_diff}).")
        score += icon_points
    else:
        reasons.append("Icon hash could not be computed (image not found or invalid).")

   
    bad_perms = {"READ_SMS", "READ_CALL_LOG", "RECORD_AUDIO", "WRITE_SETTINGS"}
    overlap = bad_perms.intersection(set(app["permissions"]))
    perm_points = 0
    if overlap:
        perm_points = 15
        score += perm_points
        reasons.append("App requests dangerous permissions: " + ", ".join(sorted(overlap)))

    
    install_points = 0
    if is_high_installs(official["installs"]) and not is_high_installs(app["installs"]):
        install_points = 10
        score += install_points
        reasons.append("Install count much lower than official app.")

    
    rating_points = 0
    if app["rating"] < 3.0:
        rating_points = 5
        score += rating_points
        reasons.append("User rating is low (< 3.0).")

    if score > 100:
        score = 100

    evidence = {
        "app_name": app["name"],
        "package_id": app["package"],
        "store_url": app.get("store_url", ""),
        "name_similarity": round(name_sim, 2),
        "publisher_similarity": round(pub_sim, 2),
        "package_similarity": round(pkg_sim, 2),
        "icon_hash_diff": icon_diff,
        "official_icon_hash": str(off_hash) if off_hash else "",
        "candidate_icon_hash": str(app_hash) if app_hash else "",
        "permission_risk_points": perm_points,
        "install_risk_points": install_points,
        "rating_risk_points": rating_points,
        "total_score": score,
    }

    return score, reasons, evidence
