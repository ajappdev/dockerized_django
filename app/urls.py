from django.urls import path

# DECLARATIONS APPLICATION
from app import views

urlpatterns = [

    ###########################################################################
    # PAGES GENERALES
    ###########################################################################
    path('', views.landing_page, name="landing_page")
]