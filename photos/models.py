from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

def validate_image(value):
    """
    Validate that the uploaded file is an image.
    """
    # valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    file_extension = str(value.name.split('.')[-1]).lower() 

    # if not any(file_extension == ext for ext in valid_extensions):
    #     raise ValidationError(_('Unsupported file type. Please upload a valid image file.'))

class Category(models.Model):
    name = models.CharField(max_length= 100,null = False,blank = False)
    
    def __str__(self):
        return self.name
    
class Photo(models.Model):
    category = models.ForeignKey(Category,on_delete = models.SET_NULL, null = True, blank = True)
    # image = models.ImageField(null=False,blank=False)
    image = models.FileField(null=False, blank=False, validators=[validate_image])
    description = models.TextField()
    
    def __str__(self):
        return self.description