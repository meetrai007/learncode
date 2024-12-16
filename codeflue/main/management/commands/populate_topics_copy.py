import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codeflue.settings")  # Replace 'codeflue' with your project name
django.setup()

from main.models import Language, Topic, SubTopic, Content  # Adjust the import based on your app name

# Define topics and subtopics structure
data = data = [
    {
        "topic": "Introduction",
        "subtopics": [
            {
                "title": "Introduction",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Getting Started",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Basic Concepts",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            }
        ]
    },
    {
        "topic": "Syntax",
        "subtopics": [
            {
                "title": "Keywords",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Comments",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            }
        ]
    },
    {
        "topic": "Variables",
        "subtopics": [
            {
                "title": "Variables",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Variable Names",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Assign Multiple Values",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Output Variables",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Global Variables",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Variable Exercises",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            }
        ]
    },
    {
        "topic": "Data Types",
        "subtopics": [
            {
                "title": "Data Types",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Numbers",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Booleans",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Dates",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Casting",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            }
        ]
    },
    {
        "topic": "Strings",
        "subtopics": [
            {
                "title": "Strings",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Slicing Strings",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Modify Strings",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Concatenate Strings",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Format Strings",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Escape Characters",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "String Methods",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "String Exercises",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            }
        ]
    },
    {
        "topic": "Operators",
        "subtopics": [
            {
                "title": "Operators",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            }
        ]
    },
    {
        "topic": "Collections",
        "subtopics": [
            {
                "title": "Lists",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Access List Items",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Dictionaries",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "Access Dictionary Items",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            # Continue adding other subtopics here, following the same pattern
        ]
    },
    {
        "topic": "Control Flow",
        "subtopics": [
            {
                "title": "if-else",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            {
                "title": "While Loops",
                "content": {
                    "description": "",
                    "keywords": "",
                    "english_content": "",
                    "hinglish_content": "",
                    "og_title": "",
                    "og_description": "",
                    "og_image_url": "",
                    "important_links": ""
                }
            },
            # Continue with more subtopics if needed
        ]
    }
    # Add remaining topics here following the same pattern...
]

# Create the Python language
python_language, created = Language.objects.get_or_create(name="Python", slug="python")

# Add topics and subtopics
for topic_order, topic_data in enumerate(data, start=1):
    # Create or update the topic
    topic, created = Topic.objects.get_or_create(
        title=topic_data["title"],
        language=python_language,
        defaults={"order": topic_order}
    )
    if not created:
        # Update the order if the topic already exists
        topic.order = topic_order
        topic.save()

    # Add subtopics under the created or updated topic
    for subtopic_order, subtopic_title in enumerate(topic_data["subtopics"], start=1):
        subtopic, created = SubTopic.objects.get_or_create(
            title=subtopic_title,
            topic=topic,
            defaults={"order": subtopic_order}
        )

        # Create blank content for each subtopic
        Content.objects.get_or_create(
            language=python_language,
            topic=topic,
            subtopic=subtopic,
            defaults={
                "title": "",
                "slug": "",
                "description": "",
                "keywords": "",
                "english_content": "",
                "hinglish_content": "",
                "og_title": "",
                "og_description": "",
                "og_image_url": "",
                "important_links": "",
            }
        )

print("Topics, subtopics, and blank content added successfully.")
