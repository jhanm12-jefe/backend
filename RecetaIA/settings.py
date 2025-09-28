import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-secret-key")
DEBUG = True
ALLOWED_HOSTS = ["*", "localhost", "127.0.0.1", "192.168.0.20"]

class IgnorePortMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "HTTP_HOST" in request.META:
            request.META["HTTP_HOST"] = request.META["HTTP_HOST"].split(":")[0]
        return self.get_response(request)

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "RecetaIA.settings.IgnorePortMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "administracion",
    "administracion2",
    "ia",
    "corsheaders",
]

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = ["http://localhost:8081"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "software"),
        "USER": os.environ.get("POSTGRES_USER", "admin"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "admin123"),
        "HOST": os.environ.get("POSTGRES_HOST", "db"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
ROOT_URLCONF = "RecetaIA.urls"
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]