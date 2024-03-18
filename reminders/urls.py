from django.urls import path
from reminders.views import create_reminder_view


urlpatterns=[
    path('api/reminder/',create_reminder_view),
]