from django.contrib import admin
from django import forms
from .models import Language, Topic, SubTopic, Content

# Inline for SubTopic (allows adding SubTopics directly within a Topic)
class SubTopicInline(admin.TabularInline):
    model = SubTopic
    extra = 1  # Number of empty forms displayed by default
    fields = ['title', 'order']

# Inline for Topic (allows adding Topics directly within a Language)
class TopicInline(admin.TabularInline):
    model = Topic
    extra = 1
    fields = ['title', 'order']  # Removed 'slug' as it is non-editable

# Admin for Language
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    inlines = [TopicInline]  # Add Topics inline

# Admin for Topic
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'order', 'slug']
    list_filter = ['language']
    search_fields = ['title', 'language__name']
    inlines = [SubTopicInline]  # Add SubTopics inline
    ordering = ['language', 'order']

# Admin for SubTopic
@admin.register(SubTopic)
class SubTopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'topic', 'order']
    list_filter = ['topic']
    search_fields = ['title', 'topic__title']
    ordering = ['order']

# Custom Form for Content Admin
class ContentAdminForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filter topics based on selected language
        language = self.data.get('language') or getattr(self.instance, 'language_id', None)
        if language:
            self.fields['topic'].queryset = Topic.objects.filter(language=language)
        else:
            self.fields['topic'].queryset = Topic.objects.none()

        # Filter subtopics based on selected topic
        topic = self.data.get('topic') or getattr(self.instance, 'topic_id', None)
        if topic:
            self.fields['subtopic'].queryset = SubTopic.objects.filter(topic=topic)
        else:
            self.fields['subtopic'].queryset = SubTopic.objects.none()

# Admin for Content
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    form = ContentAdminForm
    list_display = ['language', 'topic', 'subtopic', 'title', 'slug']
    list_filter = ['language', 'topic', 'subtopic']
    search_fields = ['title', 'topic__title', 'subtopic__title', 'language__name']
    autocomplete_fields = ['language', 'topic', 'subtopic']

    # Dynamically filter topic and subtopic based on the selected values
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "topic":
            language_id = request.GET.get('language__id__exact')
            if language_id:
                kwargs["queryset"] = Topic.objects.filter(language_id=language_id)
        elif db_field.name == "subtopic":
            topic_id = request.GET.get('topic__id__exact')
            if topic_id:
                kwargs["queryset"] = SubTopic.objects.filter(topic_id=topic_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Include JavaScript for dynamic dropdown functionality
    class Media:
        js = ('admin/js/jquery.init.js', '/static/js/admin_dynamic_fields.js')  # Add your custom JS file here
    