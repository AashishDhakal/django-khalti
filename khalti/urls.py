from django.urls import path
from .views import VerifyKhaltiPayment

urlpatterns = [
    path("verifypayment/",VerifyKhaltiPayment.as_view()),
]