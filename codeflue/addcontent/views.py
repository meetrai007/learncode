from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import Language, Topic, SubTopic, Content
from .forms import ContentForm, TopicForm, SubTopicForm

def add_content(request):
    languages = Language.objects.all()

    if request.method == "POST":
        content_form = ContentForm(request.POST)
        if content_form.is_valid():
            content_form.save()
            return redirect(reverse('content-success'))  # Replace with your success page/view

    else:
        content_form = ContentForm()

    return render(request, 'add_content.html', {
        'languages': languages,
        'content_form': content_form,
    })


def fetch_topics(request, language_id):
    """AJAX View to fetch topics for a given language."""
    topics = Topic.objects.filter(language_id=language_id).order_by('order')
    topics_data = [{'id': topic.id, 'title': topic.title} for topic in topics]
    return JsonResponse(topics_data, safe=False)


def fetch_subtopics(request, topic_id):
    """AJAX View to fetch subtopics for a given topic."""
    subtopics = SubTopic.objects.filter(topic_id=topic_id).order_by('order')
    subtopics_data = [{'id': subtopic.id, 'title': subtopic.title} for subtopic in subtopics]
    return JsonResponse(subtopics_data, safe=False)
