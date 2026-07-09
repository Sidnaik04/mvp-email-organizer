from app.core.rules.categories import Category

DOMAIN_RULES = {
    # ---------------- JOB ----------------
    "linkedin.com": {
        "category": Category.JOB,
        "weight": 40,
    },
    "greenhouse.io": {
        "category": Category.JOB,
        "weight": 50,
    },
    "lever.co": {
        "category": Category.JOB,
        "weight": 50,
    },
    "ashbyhq.com": {
        "category": Category.JOB,
        "weight": 50,
    },
    "wellfound.com": {
        "category": Category.JOB,
        "weight": 45,
    },
    "naukri.com": {
        "category": Category.JOB,
        "weight": 60,
    },
    "foundit.in": {
        "category": Category.JOB,
        "weight": 60,
    },
    # --------------- TECH ----------------
    "medium.com": {
        "category": Category.TECH,
        "weight": 60,
    },
    "daily.dev": {
        "category": Category.TECH,
        "weight": 60,
    },
    "realpython.com": {
        "category": Category.TECH,
        "weight": 45,
    },
    "substack.com": {
        "category": Category.TECH,
        "weight": 60,
    },
    "google.com": {
        "category": Category.SOFTWARE,
        "weight": 40,
    },
    # ------------- SOFTWARE -------------
    "render.com": {
        "category": Category.SOFTWARE,
        "weight": 60,
    },
    "vercel.com": {
        "category": Category.SOFTWARE,
        "weight": 35,
    },
    "supabase.com": {
        "category": Category.SOFTWARE,
        "weight": 35,
    },
    "neon.tech": {
        "category": Category.SOFTWARE,
        "weight": 35,
    },
    "github.com": {
        "category": Category.SOFTWARE,
        "weight": 60,
    },
}
