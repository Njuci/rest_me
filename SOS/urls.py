
from django.urls import path,include
from .views import touslesHopital,UnseulHopital
api1="ApiTousleshopitaux/"
api2="unseulHopital/<int:id>"

urlpatterns = [

    path(api1,touslesHopital().as_view()),
    path(api2,UnseulHopital.as_view()),
    ]
