from apptwo.views import RenderedFeed
from django.urls import path

app_name='apptwo'

urlpatterns = [
    path('renderedFeed/',RenderedFeed.as_view(),name='feed')
]