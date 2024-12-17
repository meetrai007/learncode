from django.urls import path
from . import views

urlpatterns = [
    # urls for homepage
    path('', views.homepage, name='homepage'),

    # urls for add content
    path('add-content/', views.add_content, name='add_content'),
    path('get-topics/<int:language_id>/', views.get_topics, name='get_topics'),
    path('get-subtopics/<int:topic_id>/', views.get_subtopics, name='get_subtopics'),

    # url for language contents showing
    path('<slug:language_slug>/', views.language_contents, name='language_contents'),
    path('get-content/<int:subtopic_id>/', views.get_content_for_subtopic, name='get_content_for_subtopic'),

    # urls for admin
    path('admin/main/topic/', views.fetch_topics, name='fetch_topics'),
    path('admin/main/subtopic/', views.fetch_subtopics, name='fetch_subtopics'),

]
