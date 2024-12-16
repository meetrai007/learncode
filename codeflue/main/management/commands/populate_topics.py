from django.core.management.base import BaseCommand
from main.models import Language, Topic, SubTopic

class Command(BaseCommand):
    help = "Populate topics and subtopics for the Python language"

    def handle(self, *args, **options):
        data = [
    {
        "title": "Introduction",
        "subtopics": ["Introduction", "Getting Started", "Basic Concepts"]
    },
    {
        "title": "Syntax",
        "subtopics": ["Keywords", "Comments"]
    },
    {
        "title": "Variables",
        "subtopics": [
            "Variables", "Variable Names", "Assign Multiple Values", "Output Variables", "Global Variables", "Variable Exercises"
        ]
    },
    {
        "title": "Data Types",
        "subtopics": ["Data Types", "Numbers", "Booleans", "Dates", "Casting"]
    },
    {
        "title": "Strings",
        "subtopics": [
            "Strings", "Slicing Strings", "Modify Strings", "Concatenate Strings", "Format Strings", "Escape Characters", "String Methods", "String Exercises"
        ]
    },
    {
        "title": "Operators",
        "subtopics": ["Operators"]
    },
    {
        "title": "Collections",
        "subtopics": [
            "Lists", "Access List Items", "Change List Items", "Add List Items", "Remove List Items", "Loop Lists", "List Comprehension", "Sort Lists",
            "Copy Lists", "Join Lists", "List Methods", "List Exercises", "Tuples", "Access Tuples", "Update Tuples", "Unpack Tuples", "Loop Tuples",
            "Join Tuples", "Tuple Methods", "Tuple Exercises", "Sets", "Access Set Items", "Add Set Items", "Remove Set Items", "Loop Sets", "Join Sets",
            "Set Methods", "Set Exercises", "Dictionaries", "Access Items", "Change Items", "Add Items", "Remove Items", "Loop Dictionaries", "Copy Dictionaries",
            "Nested Dictionaries", "Dictionary Methods", "Dictionary Exercises"
        ]
    },
    {
        "title": "Control Flow",
        "subtopics": ["if-else", "While Loops", "For Loops", "Iterators"]
    },
    {
        "title": "Functions",
        "subtopics": ["Functions", "Lambda"]
    },
    {
        "title": "Object-Oriented Programming (OOP)",
        "subtopics": ["Classes/Objects", "Inheritance", "Polymorphism", "Scope"]
    },
    {
        "title": "Modules",
        "subtopics": ["Modules", "JSON", "Module Reference"]
    },
    {
        "title": "File Handling",
        "subtopics": ["File Handling", "Read Files", "Write/Create Files", "Delete Files"]
    },
    {
        "title": "Data Science Libraries",
        "subtopics": ["NumPy Tutorial", "Pandas Tutorial", "SciPy Tutorial"]
    },
    {
        "title": "Matplotlib",
        "subtopics": [
            "Matplotlib Intro", "Matplotlib Get Started", "Matplotlib Pyplot", "Matplotlib Plotting", "Matplotlib Markers", "Matplotlib Line",
            "Matplotlib Labels", "Matplotlib Grid", "Matplotlib Subplot", "Matplotlib Scatter", "Matplotlib Bars", "Matplotlib Histograms",
            "Matplotlib Pie Charts"
        ]
    },
    {
        "title": "References",
        "subtopics": [
            "Overview", "Built-in Functions", "String Methods", "List Methods", "Dictionary Methods", "Tuple Methods", "Set Methods",
            "File Methods", "Exceptions", "Glossary"
        ]
    },
    {
        "title": "Module References",
        "subtopics": ["Random Module", "Logging Module", "Requests Module", "Statistics Module", "Math Module", "cMath Module"]
    },
    {
        "title": "How To",
        "subtopics": ["Remove List Duplicates", "Reverse a String", "Add Two Numbers"]
    },
    {
        "title": "Examples",
        "subtopics": ["Examples Overview", "Compiler", "Exercises", "Quiz"]
    },
    {
        "title": "Additional Sections",
        "subtopics": ["Server", "Interview Q&A", "Bootcamp", "Certificate"]
    }
]


        python_language, created = Language.objects.get_or_create(
            name="Python", slug="python"
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Created Language: {python_language.name}"))
        else:
            self.stdout.write(self.style.WARNING(f"Language {python_language.name} already exists"))

        for topic_data in data:
            topic, created = Topic.objects.get_or_create(
                title=topic_data["title"], language=python_language
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added Topic: {topic.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Topic {topic.title} already exists"))

            for subtopic_title in topic_data["subtopics"]:
                subtopic, created = SubTopic.objects.get_or_create(
                    title=subtopic_title, topic=topic
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added SubTopic: {subtopic.title}"))
                else:
                    self.stdout.write(self.style.WARNING(f"SubTopic {subtopic.title} already exists"))

        self.stdout.write(self.style.SUCCESS("Topics and subtopics added successfully."))
