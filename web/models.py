from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator

class EnglishLettersUsernameValidator(RegexValidator):
    regex = r'^[a-z0-9]{8,16}$'
    message = _(
        'Username can only contain lowercase English letters (a-z) and numbers (0-9), and must be between 8 and 16 characters long.'
    )
    flags = 0

class PasswordValidator(RegexValidator):
    regex = r'^[a-zA-Z0-9]{8,128}$'
    message = _(
        'Password must be at least 8 characters and at most 128 characters long, and can only contain English letters and numbers.'
    )
    flags = 0

class PhoneValidator(RegexValidator):
    regex=r'^\+\d{12}$'
    message =_("Phone number must be in the format: '+123456789012'.")

    flags = 0

# Users
class UserModel(AbstractUser):
    user_image = models.ImageField(upload_to=' users/profile/profile-image/%Y/%m/%d/', default='default-user.jpg')
    company = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    mobileNumber = models.CharField(max_length=13, blank=True, null=True, validators=[PhoneValidator()])
    socialMedia = models.URLField(blank=True, null=True)

    username = models.CharField(
        _('username'),
        max_length=16,
        unique=True,
        help_text=_('Required. Up to 16 characters. Only English letters (a-z)(0-9).'),
        validators=[EnglishLettersUsernameValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    password = models.CharField(
        _('password'),
        max_length=128, 
        validators=[PasswordValidator()],
        help_text=_("Password must be at least 8 characters and at most 32 characters long, and can only contain English letters and numbers."),
    )

class FunctionsModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Function'
        verbose_name_plural = 'Functions'
        ordering = ('-id',)

class BlogCategoryModel(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.category}"
    
    class Meta: 
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    text = RichTextField()
    image = models.ImageField(upload_to='blogs/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(BlogCategoryModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self): 
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ('-id',)