from app.core.rules.categories import Category

SENDER_RULES = {

    # Job
    "google careers": Category.JOB,
    "hackerrank": Category.JOB,
    "naukri": Category.JOB,
    "foundit": Category.JOB,
    "indeed": Category.JOB,
    "linkedin": Category.JOB,
    "unstop": Category.JOB,

    # Software
    "google play": Category.SOFTWARE,
    "firebase": Category.SOFTWARE,
    "google cloud": Category.SOFTWARE,
    "aws": Category.SOFTWARE,
    "github": Category.SOFTWARE,
    "render": Category.SOFTWARE,
    "supabase": Category.SOFTWARE,
    "vercel": Category.SOFTWARE,
    "cloudflare": Category.SOFTWARE,
    "canva": Category.SOFTWARE,

    # Tech
    "medium": Category.TECH,
    "daily.dev": Category.TECH,
    "substack": Category.TECH,
    "real python": Category.TECH,

    # Bank
    "hdfc": Category.BANK,
    "icici": Category.BANK,
    "axis": Category.BANK,
    "sbi": Category.BANK,
    "groww": Category.BANK,
}