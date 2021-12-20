from decouple import config

ENVIRONMENT = config('ENVIRONMENT', default='DEVELOPMENT')

if ENVIRONMENT.upper() == 'PRODUCTION':
    from project_name.settings.staging import *
elif ENVIRONMENT.upper() == 'STAGING':
    from project_name.settings.production import *
else:
    from project_name.settings.development import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
STATIC_URL = 'static/'
Path(BASE_DIR / 'static/').mkdir(parents=True, exist_ok=True)
if DEBUG:
    STATIC_DIR = BASE_DIR / 'static/'
    STATICFILES_DIRS = [
        STATIC_DIR
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static/'
