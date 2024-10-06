from django.db import models
import uuid

# A class BaseModel class which will be used in other apps like destination and other app also so that we don't have to write the same code everywhere

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_date = models.models.DateTimeField(auto_now_add=True)
    updated_date = models.models.DateTimeField(auto_add=True)

    class Meta:
        abstract = True