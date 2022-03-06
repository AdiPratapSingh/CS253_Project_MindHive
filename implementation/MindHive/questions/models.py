from pyexpat import model
from django.db import models
from ..MindHive.models import Content
from ..users.models import User
class Question(Content):
    # Question-specific fields
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
    numViews = models.IntegerField(default=0)
    viewedBy = models.ManyToManyField(User, related_name='viewedBy')