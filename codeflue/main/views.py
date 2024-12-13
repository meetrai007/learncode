from django.shortcuts import render, get_object_or_404
from .models import Language, SubTopic, Content
from django.http import JsonResponse
from .models import SubTopic

def language_contents(request, language_slug):
    # Get the language object by slug
    language = get_object_or_404(Language, slug=language_slug)
    language_list = Language.objects.all()
    
    # Get all topics for the selected language, ordered by their position
    topics = language.topics.all()
    
    # Get content for the first subtopic by default (if any)
    content = None
    if topics.exists():
        first_topic = topics.first()
        if first_topic.subtopics.exists():
            first_subtopic = first_topic.subtopics.first()
            content = first_subtopic.content.first()  # Get the first content related to the subtopic
    
    # Render the page with topics, subtopics, and initial content
    return render(request, 'main/language_contents.html', {
        'language': language,
        'topics': topics,
        'content': content,
        'language_list': language_list
    })
def get_content_for_subtopic(request, subtopic_id):
    subtopic = get_object_or_404(SubTopic, id=subtopic_id)
    content = subtopic.content.first()  # Get the first content related to this subtopic
    if content:
        response_data = {
            'content': {
                'title': content.title,
                'description': content.description,
                'english_content': content.english_content,
                'hinglish_content': content.hinglish_content,
            }
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Content not found'}, status=404)