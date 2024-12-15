from django.contrib import admin
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
    ordering = ['order']

# Admin for SubTopic
@admin.register(SubTopic)
class SubTopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'topic', 'order']
    list_filter = ['topic']
    search_fields = ['title', 'topic__title']
    ordering = ['order']

# Admin for Content
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = [ 'language', 'topic', 'subtopic','title', 'slug']
    list_filter = ['language', 'topic', 'subtopic']
    search_fields = ['title', 'topic__title', 'subtopic__title', 'language__name']
    autocomplete_fields = ['language', 'topic', 'subtopic']
    fieldsets = (
        ("Basic Information", {
            "fields": ('language', 'topic', 'subtopic', 'title', 'slug', 'description')
        }),
        ("Content Details", {
            "fields": ('english_content', 'hinglish_content')
        }),
        ("SEO Details", {
            "fields": ('og_title', 'og_description', 'og_image_url')
        }),
        ("Additional Information", {
            "fields": ('important_links',)
        }),
    )
