from django.shortcuts import render, get_object_or_404,redirect # type: ignore
from .models import Language, SubTopic, Content,Topic
from django.http import JsonResponse # type: ignore
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

def add_content(request):
    if request.method == 'POST':
        language_id = request.POST.get('language')
        topic_id = request.POST.get('topic')
        subtopic_id = request.POST.get('subtopic')

        language = get_object_or_404(Language, id=language_id)
        topic = get_object_or_404(Topic, id=topic_id)
        subtopic = get_object_or_404(SubTopic, id=subtopic_id)

        # Create the new content
        content = Content(
            language=language,
            topic=topic,
            subtopic=subtopic,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            keywords=request.POST.get('keywords'),
            english_content=request.POST.get('english_content'),
            hinglish_content=request.POST.get('hinglish_content'),
            og_title=request.POST.get('og_title'),
            og_description=request.POST.get('og_description'),
            og_image_url=request.POST.get('og_image_url'),
            important_links=request.POST.get('important_links')
        )
        content.save()
        return redirect('language_contents', language_slug=language.slug)

    languages = Language.objects.all()
    return render(request, 'main/add_content.html', {'languages': languages})


def get_topics(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    topics = language.topics.all()
    topic_data = [{'id': topic.id, 'title': topic.title} for topic in topics]
    return JsonResponse({'topics': topic_data})

def get_subtopics(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    subtopics = topic.subtopics.all()
    subtopic_data = [{'id': subtopic.id, 'title': subtopic.title} for subtopic in subtopics]
    return JsonResponse({'subtopics': subtopic_data})



def fetch_topics(request):
    language_id = request.GET.get('language_id')
    if language_id:
        # Filter topics based on language_id
        topics = Topic.objects.filter(language_id=language_id).values('id', 'title')
        results = [{'id': topic['id'], 'text': topic['title']} for topic in topics]
    else:
        results = []  # Return an empty list if no language_id is provided
    
    return JsonResponse({'results': results})

def fetch_subtopics(request):
    topic_id = request.GET.get('topic_id')
    if topic_id:
        # Filter subtopics based on topic_id
        subtopics = SubTopic.objects.filter(topic_id=topic_id).values('id', 'title')
        results = [{'id': subtopic['id'], 'text': subtopic['title']} for subtopic in subtopics]
    else:
        results = []  # Return an empty list if no topic_id is provided
    
    return JsonResponse({'results': results})
