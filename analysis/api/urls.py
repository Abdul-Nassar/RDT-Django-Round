""" Module includes urls of views
"""
from django.conf.urls import url
from analysis.api.views import (
    PercentageChangeView,
    TopVolumesView
)

urlpatterns = [
    url(r'^percentages/$', PercentageChangeView.as_view()),
    url(r'^topvolumes/$', TopVolumesView.as_view())
]
