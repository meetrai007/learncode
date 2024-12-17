# models.py

from django.db import models # type: ignore
from autoslug import AutoSlugField # type: ignore

class Language(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name',unique=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    language = models.ForeignKey(Language, related_name="topics", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title',unique=True)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']  # Ensures topics are displayed in the correct order

    def __str__(self):
        return self.title


class SubTopic(models.Model):
    topic = models.ForeignKey(Topic, related_name="subtopics", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']  # Ensures subtopics are displayed in the correct order

    def __str__(self):
        return self.title


class Content(models.Model):
    language = models.ForeignKey(Language, related_name="content", on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, related_name="content", on_delete=models.CASCADE)
    subtopic = models.ForeignKey(SubTopic, related_name="content", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title",unique=True)
    description = models.TextField()
    keywords = models.TextField(default="")
    english_content = models.TextField()
    hinglish_content = models.TextField()
    og_title = models.CharField(max_length=200, null=True, blank=True)
    og_description = models.TextField(null=True, blank=True)
    og_image_url = models.URLField(null=True, blank=True)
    important_links = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/{self.language.slug}/{self.topic.slug}/{self.slug}/"
