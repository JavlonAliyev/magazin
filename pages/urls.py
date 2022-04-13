from django.urls import path

from pages.views import ContactCreatView, AboutTemplateView, HomeTemplateView

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactCreatView.as_view(), name="contact"),
    path('about/', AboutTemplateView.as_view(), name="about"),
    path('', HomeTemplateView.as_view(), name="home"),
]