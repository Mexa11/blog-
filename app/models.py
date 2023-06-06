from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ProfileData(BaseModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="profile_data")
    description = models.TextField()

    def __str__(self):
        return self.name
