from django.urls import include, path
# from rest_framework import routers
from college import views


app_name='college'
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('index/',views.index ,name='index'),
  
]