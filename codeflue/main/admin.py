from django.contrib import admin
from .models import Language, Topic, SubTopic, Content

# Register Language model without customization
admin.site.register(Language)

# Custom admin class for Topic
class TopicAdmin(admin.ModelAdmin):  # Use PascalCase for class names
    model = Topic
    list_display = ('language', 'title', 'order')  # Specify fields to display
    ordering = ('language', 'order')  # Sort first by language, then by order
    
# Custom admin class for SubTopic
class SubTopicAdmin(admin.ModelAdmin):  # Use PascalCase for class names
    model = SubTopic
    list_display = ('topic', 'title', 'order')  # Specify fields to display
    

# Custom admin class for Content
class ContentAdmin(admin.ModelAdmin):  # Use PascalCase for class names
    model = Content
    list_display = ('language','topic', 'subtopic', 'title')  # Specify fields to display
    ordering = ('language','topic', 'subtopic', 'title')

# Register models with their respective admin classes
admin.site.register(Topic, TopicAdmin)
admin.site.register(SubTopic, SubTopicAdmin)
admin.site.register(Content, ContentAdmin)
