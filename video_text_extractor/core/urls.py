from django.urls import path
from .views import index, process_frame, translate_text

urlpatterns = [
    path('', index, name='index'),
    path('process_frame/', process_frame, name='process_frame'),
    path('translate_text/', translate_text, name='translate_text'),
]
