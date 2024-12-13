from django.urls import path
from . import views

urlpatterns = [
    path('<slug:language_slug>/', views.language_contents, name='language_contents'),
    path('get-content/<int:subtopic_id>/', views.get_content_for_subtopic, name='get_content_for_subtopic'),
]
