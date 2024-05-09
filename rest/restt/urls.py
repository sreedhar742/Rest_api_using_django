
from django.urls import path,include
from rest_framework import routers
from .views import *
router=routers.DefaultRouter()
router.register(r"sreedhar",Storeview)
router.register(r"zeelan",Storeview)
urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include("rest_framework.urls")),
]
