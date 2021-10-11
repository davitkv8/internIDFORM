from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from PIL import Image

alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only contains characters.')

# class MyMaxValueValidator(MaxValueValidator):
#     message = ('errormessage')s.')


class UsersID(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    document_id = models.BigIntegerField(null=False, unique=True,
                                      validators=[MaxValueValidator(99999999999, ('Invalid ID number. It contains 11 numbers.')),
                                                  MinValueValidator(10000000000, ('Invalid ID number. It contains 11 numbers.'))])
    first_name = models.CharField(max_length=55, null=False,
                                  validators=[alphanumeric])
    last_name = models.CharField(max_length=55, null=False,
                                 validators=[alphanumeric])
    birth_date = models.DateField(blank=False, null=False)
    sex_choices = (
        ('', ''),
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    sex = models.CharField(blank=False, null=False, max_length=55,
                                     default='', choices=sex_choices)
    image = models.ImageField(blank=False, null=False, default='default.jpg',
                              upload_to='document_image')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)      #document_image resolution
        img = Image.open(self.image.path)
        if img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
