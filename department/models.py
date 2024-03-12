from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name



class DynamicFormData(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    form_structure = JSONField()
    submission_data = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.department} - {self.created_at}"