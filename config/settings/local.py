from .base import *  # noqa
from .base import env

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

ADMIN_URL = env.str("ADMIN_URL", default="admin/")

# Email settings
# ----------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Channels
# ----------------------------------------------------------------
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

# Celery
# ----------------------------------------------------------------
CELERY_BROKER_URL = env.str("CELERY_BROKER", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = env.str("CELERY_BACKEND", "redis://127.0.0.1:6379/0")
