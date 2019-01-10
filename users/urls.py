from django.urls import path

from .views import login, credit_request, screenshot, me

urlpatterns = [
    path('login/', login),
    # Below all need to provide token
    path('me/', me),  # Get own info
    path('credit/', credit_request),  # Asking for Credit
    path('screenshot/', screenshot)  # Making a screenshot so reduce Credit point
]
