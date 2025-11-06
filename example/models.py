import uuid
from django.db import models

from base_app.models import User

# Create your models here.
class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)