from django.core.management.base import BaseCommand
from faker import Faker
import random
import string

class Command(BaseCommand):
    help = 'Generate random content for testing all models'

    def handle(self, *args, **kwargs):
        # Lazy import inside the function to avoid circular imports
        from main.models import Language, Topic, SubTopic, Content

        fake = Faker()
        languages = Language.objects.all()

        # Generate data for each language
        for language in languages:
            self.stdout.write(f"Generating data for language: {language.name}")
            num_topics = random.randint(3, 7)  # Random number of topics

            for topic_idx in range(num_topics):
                topic_title = fake.sentence(nb_words=3).replace(".", "")
                topic = Topic.objects.create(
                    language=language,
                    title=topic_title,
                    slug=self.create_unique_slug(topic_title),
                    order=topic_idx
                )

                # Generate subtopics for each topic
                num_subtopics = random.randint(2, 5)
                for subtopic_idx in range(num_subtopics):
                    subtopic_title = fake.sentence(nb_words=4).replace(".", "")
                    subtopic = SubTopic.objects.create(
                        topic=topic,
                        title=subtopic_title,
                        order=subtopic_idx
                    )

                    # Generate content for each subtopic
                    num_contents = random.randint(1, 3)
                    for _ in range(num_contents):
                        content_title = fake.sentence(nb_words=5).replace(".", "")
                        Content.objects.create(
                            language=language,
                            topic=topic,
                            subtopic=subtopic,
                            title=content_title,
                            slug=self.create_unique_slug(content_title),
                            description=fake.paragraph(nb_sentences=3),
                            english_content=fake.text(max_nb_chars=500),
                            hinglish_content=fake.text(max_nb_chars=500),
                            og_title=fake.sentence(nb_words=6),
                            og_description=fake.paragraph(nb_sentences=2),
                            og_image_url=fake.image_url(),
                            important_links="\n".join([fake.url() for _ in range(3)])
                        )

            self.stdout.write(self.style.SUCCESS(f"Successfully generated data for language: {language.name}"))

    def create_unique_slug(self, title):
        """Create a unique slug using a random string if the slug already exists."""
        from main.models import Content
        slug = title.lower().replace(" ", "_")
        while Content.objects.filter(slug=slug).exists():
            slug = f"{slug}_{self.generate_random_string(4)}"
        return slug

    def generate_random_string(self, length=6):
        """Generate a random alphanumeric string."""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
