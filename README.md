# Django REST framework struture
how to integrate an app into project

# Main packages

* Python 3.13.9
* Django 5.2
* djangorestframework 3.16.1
* djangorestframework_simplejwt 5.5.1
* drf-access-policy 1.5.0
* injector 0.22.0
* python-dotenv 1.2.1

---

# Quickstart

  ### Step1. Configure to use base app setup
  Add the following to your `settings.py` module:
  ```python
  from dotenv import load_dotenv
  
  # Load environment variables from .env file
  load_dotenv()

  INSTALLED_APPS = [
      # ... make sure to include the default installed apps here.
      'rest_framework',
      'rest_framework_simplejwt',
      'base_app',
  ]

  AUTH_USER_MODEL = 'base_app.User'

  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework_simplejwt.authentication.JWTAuthentication',
      ],
      'EXCEPTION_HANDLER': 'base_app.exceptions.exception_handler'
  }
  
  SIMPLE_JWT = {
      "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
      "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
      "UPDATE_LAST_LOGIN": True,
      "TOKEN_OBTAIN_SERIALIZER": "base_app.serializers.UserTokenObtainPairSerializer",
      "AUTH_HEADER_TYPES": ("Bearer",),
  }
  ```

  ### Step2. Add base_app urls
  Add the following to your `urls.py` in project folder:
  ```python
  path("base/", include("base_app.urls")),
  ```

  ### Step3. take a look at example app
