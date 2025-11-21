# app/apps_data.py
'''
APPS_DATA = [

    # ---------------------------------------------------
    # 1) REAL GENUINE PHONEPE APP
    # ---------------------------------------------------
    {
        "name": "PhonePe UPI, Payment, Recharge",
        "package": "com.phonepe.app",
        "publisher": "PhonePe Pvt. Ltd",
        "description": "Official UPI payments, recharge, bill pay app.",
        "permissions": ["SMS", "Location", "Contacts", "Camera", "Storage", "Accounts", "Call", "Microphone"],
        "rating": 4.4,
        "installs": "500M+",
        "icon_path": "icons/phonepe_official.webp",
        "label": "genuine",
        "risk": 0
        
    },

    # ---------------------------------------------------
    # 2) FAKE APP – Update Scam
    # ---------------------------------------------------
    {
        "name": "PhonePe Update 2025",
        "package": "com.phonepe.update.secure",
        "publisher": "PhonePe Support Team",
        "description": "Update your PhonePe app to get cashback rewards.",
        "permissions": ["READ_SMS", "READ_CONTACTS", "READ_CALL_LOG", "INTERNET"],
        "rating": 2.1,
        "installs": "50K+",
        "icon_path": "icons/fake_update.avif",
        "label": "fake",
        "risk": 85
    },

    # ---------------------------------------------------
    # 3) FAKE APP – Cashback Scam
    # ---------------------------------------------------
    {
        "name": "PhonePay Free Cashback",
        "package": "com.phonepay.cashback.free",
        "publisher": "UPI Rewards Inc",
        "description": "Get instant cashback by updating your UPI app.",
        "permissions": ["READ_SMS", "RECORD_AUDIO", "ACCESS_FINE_LOCATION"],
        "rating": 1.9,
        "installs": "10K+",
        "icon_path": "icons/fake_cashback.png",
        "label": "fake",
        "risk": 92
    },

    # ---------------------------------------------------
    # 4) FAKE APP – Guide / Tricks Scam
    # ---------------------------------------------------
    {
        "name": "PhonePe Guide & Tricks 2025",
        "package": "com.phonepe.tricks.learn",
        "publisher": "UPI Helper",
        "description": "Learn tricks to earn money using PhonePe.",
        "permissions": ["INTERNET", "READ_CONTACTS"],
        "rating": 3.0,
        "installs": "100K+",
        "icon_path": "icons/fake_tricks.png",
        "label": "fake",
        "risk": 70
    },

    # ---------------------------------------------------
    # 5) FAKE APP – Lookalike Icon
    # ---------------------------------------------------
    {
        "name": "ФhonePe UPI Original 2025",   # note: cyrillic F
        "package": "com.phonepe.original.upi",
        "publisher": "PhonePe India Org",
        "description": "This is PhonePe official UPI app.",
        "permissions": ["READ_SMS", "READ_CALL_LOG"],
        "rating": 2.8,
        "installs": "5K+",
        "icon_path": "icons/fake_lookalike.png",
        "label": "fake",
        "risk": 88
    },

    # ---------------------------------------------------
    # 6) FAKE APP – Dangerous Permissions
    # ---------------------------------------------------
    {
        "name": "PhonePe UPI Banking Pro",
        "package": "com.phonepe.banking.pro",
        "publisher": "Pro Banking Apps",
        "description": "Advanced PhonePe banking features with unlimited cashback.",
        "permissions": ["READ_SMS", "READ_CONTACTS", "RECORD_AUDIO", "WRITE_SETTINGS"],
        "rating": 1.6,
        "installs": "1K+",
        "icon_path": "icons/fake_banking.png",
        "label": "fake",
        "risk": 95
    },

    # ---------------------------------------------------
    # 7) FAKE APP – “Update Required” Malware
    # ---------------------------------------------------
    {
        "name": "PhonePe UPI Update Required",
        "package": "com.phonepe.update.required",
        "publisher": "SecureUpdate Ltd",
        "description": "Security update required! Install now.",
        "permissions": ["READ_SMS", "READ_CONTACTS", "WRITE_SETTINGS"],
        "rating": 1.5,
        "installs": "2K+",
        "icon_path": "icons/fake_warning.png",
        "label": "fake",
        "risk": 97
    },

    # ---------------------------------------------------
    # 8) FAKE APP – Low Install Clone
    # ---------------------------------------------------
    {
        "name": "PhonePe UPI Lite",
        "package": "com.phonepe.lite.app",
        "publisher": "UPI Lite Dev",
        "description": "Lite version of PhonePe for faster payments.",
        "permissions": ["INTERNET", "READ_CONTACTS"],
        "rating": 3.2,
        "installs": "5K+",
        "icon_path": "icons/fake_lite.png",
        "label": "fake",
        "risk": 60
    }
]
'''

# app/apps_data.py

from difflib import SequenceMatcher
from PIL import Image
import imagehash
from pathlib import Path
from django.conf import settings

# ---------------------------------------------------
# DATASET OF REAL + FAKE APPS
# ---------------------------------------------------

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
        "label": "genuine",
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
        "label": "fake",
    },

    {
        "name": "PhonePay Free Cashback",
        "package": "com.phonepay.cashback.free",
        "publisher": "UPI Rewards Inc",
        "description": "Get instant cashback by updating your UPI app.",
        "permissions": ["READ_SMS", "RECORD_AUDIO", "ACCESS_FINE_LOCATION"],
        "rating": 1.9,
        "installs": "10K+",
        "icon_path": "fake_cashback.png",
        "label": "fake",
    },

    {
        "name": "PhonePe Guide & Tricks 2025",
        "package": "com.phonepe.tricks.learn",
        "publisher": "UPI Helper",
        "description": "Learn tricks to earn money using PhonePe.",
        "permissions": ["INTERNET", "READ_CONTACTS"],
        "rating": 3.0,
        "installs": "100K+",
        "icon_path": "fake_tricks.png",
        "label": "fake",
    },

    {
        "name": "ФhonePe UPI Original 2025",
        "package": "com.phonepe.original.upi",
        "publisher": "PhonePe India Org",
        "description": "This is PhonePe official UPI app.",
        "permissions": ["READ_SMS", "READ_CALL_LOG"],
        "rating": 2.8,
        "installs": "5K+",
        "icon_path": "fake_lookalike.png",
        "label": "fake",
    },

    {
        "name": "PhonePe UPI Banking Pro",
        "package": "com.phonepe.banking.pro",
        "publisher": "Pro Banking Apps",
        "description": "Advanced PhonePe banking features with unlimited cashback.",
        "permissions": ["READ_SMS", "READ_CONTACTS", "RECORD_AUDIO", "WRITE_SETTINGS"],
        "rating": 1.6,
        "installs": "1K+",
        "icon_path": "fake_banking.png",
        "label": "fake",
    },

    {
        "name": "PhonePe UPI Update Required",
        "package": "com.phonepe.update.required",
        "publisher": "SecureUpdate Ltd",
        "description": "Security update required! Install now.",
        "permissions": ["READ_SMS", "READ_CONTACTS", "WRITE_SETTINGS"],
        "rating": 1.5,
        "installs": "2K+",
        "icon_path": "fake_warning.png",
        "label": "fake",
    },

    {
        "name": "PhonePe UPI Lite",
        "package": "com.phonepe.lite.app",
        "publisher": "UPI Lite Dev",
        "description": "Lite version of PhonePe for faster payments.",
        "permissions": ["INTERNET", "READ_CONTACTS"],
        "rating": 3.2,
        "installs": "5K+",
        "icon_path": "fake_lite.png",
        "label": "fake",
    }
]

# ---------------------------------------------------
# HASHING + SCORING LOGIC
# ---------------------------------------------------

def get_icon_hash(icon_filename):
    """Return perceptual hash of an icon."""
    icon_path = Path(settings.BASE_DIR) / "app" / "app_icons" / icon_filename
    try:
        img = Image.open(icon_path)
        return imagehash.phash(img)
    except:
        return None


# Compute official icon hash
OFFICIAL_HASH = None
for app in APPS_DATA:
    if app["label"] == "genuine":
        OFFICIAL_HASH = get_icon_hash(app["icon_path"])
        break


def name_similarity(a, b):
    """Return fuzzy similarity between two strings."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def compute_risk(app, brand_name, official_pkg):
    """Compute final risk score + explanation list."""
    score = 0
    reasons = []

    # 1️⃣ Name similarity
    sim = name_similarity(app["name"], brand_name)
    name_score = (1 - sim) * 40
    score += name_score
    reasons.append(f"Low name similarity: {round(name_score, 2)} points")

    # 2️⃣ Package mismatch
    if app["package"] != official_pkg:
        score += 30
        reasons.append("Package name mismatch")

    # 3️⃣ Publisher suspicious
    if "update" in app["publisher"].lower() or "helper" in app["publisher"].lower():
        score += 20
        reasons.append("Publisher looks suspicious")

    # 4️⃣ Icon hash check
    fake_hash = get_icon_hash(app["icon_path"])
    if OFFICIAL_HASH and fake_hash:
        diff = OFFICIAL_HASH - fake_hash
        icon_score = min(30, diff * 2)
        score += icon_score
        reasons.append(f"Icon similarity score: {icon_score} (hash diff = {diff})")

    # 5️⃣ Dangerous permissions
    bad_perms = {"READ_SMS", "READ_CALL_LOG", "RECORD_AUDIO", "WRITE_SETTINGS"}
    overlap = bad_perms.intersection(set(app["permissions"]))
    if overlap:
        score += 15
        reasons.append(f"Dangerous permissions detected: {', '.join(overlap)}")

    return min(100, round(score)), reasons
