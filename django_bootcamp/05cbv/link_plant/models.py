from django.db import models


# Create your models here.
class Profile(models.Model):
    BG_COLORS = (
        # (saved_in_db, shows_in_admin_and_website)
        ('blue', 'Blue'),
        ('green', 'Green'),

    )
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)
    bg_color = models.CharField(choices=BG_COLORS, max_length=10)

    def __str__(self):
        return self.name


class Link(models.Model):
    text = models.CharField(max_length=100)
    url = models.URLField()
    # related_name='links' allows `Profile` to have access to related link via `.links`
    # by default it'll be `.<ClassName>_set`
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='links')

    def __str__(self):
        return f'{self.profile.name} -- {self.text} | {self.url}'
