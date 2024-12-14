from django.core.management.base import BaseCommand
import random
import string

class Command(BaseCommand):
    help = 'Generate random content for testing'

    def handle(self, *args, **kwargs):
        # Lazy import inside the function to avoid circular imports
        from main.models import Language, Topic, SubTopic
        languages = Language.objects.all()

        for language in languages:
            c_topics = self.get_random_topics()  # Your function to get topics for the language
            self.create_topics_for_language(language, c_topics)

    def create_topics_for_language(self, language, topics):
        from main.models import Topic  # Lazy import inside the method
        for idx, topic_title in enumerate(topics):
            slug = self.create_unique_slug(topic_title)
            Topic.objects.create(language=language, title=topic_title, slug=slug, order=idx)

    def create_unique_slug(self, topic_title):
        from main.models import Topic  # Lazy import inside the method
        slug = topic_title.lower().replace(" ", "_")
        
        # Check if slug already exists and regenerate if necessary
        while Topic.objects.filter(slug=slug).exists():
            slug = self.generate_random_string()  # Generate a random string to ensure uniqueness
            
        return slug

    def generate_random_string(self, length=8):
        """Generate a random string to ensure uniqueness for slugs."""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def get_random_topics(self):
        """Generate random topics for testing."""
        topics = [
            "Introduction", "Getting Started", "Basic Concepts", "Syntax", "Keywords", "Comments", 
            "Variables", "Variable Names", "Assign Multiple Values", "Output Variables", 
            "Global Variables", "Variable Exercises", "Data Types"
        ]
        return random.sample(topics, len(topics))  # Shuffle topics for variety
