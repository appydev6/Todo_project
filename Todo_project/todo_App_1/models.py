from django.db import models

# Create your models here.
class todo_App_1(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    complted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
