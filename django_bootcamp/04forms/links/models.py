from django.db import models

from django.utils.text import slugify

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url  = models.URLField(max_length=200)
    # If it's blank, we'll create it from the url itself.
    slug = models.SlugField(unique=True, blank=True)
    nclicks = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.name} | {self.nclicks}'

    def update_click(self):
        self.nclicks += 1
        self.save()

    # Overwrite the .save() method to include `slug` generation.
    def save(self, *args, **kwargs):
        if not self.slug:
            # slugify(" Joel is a slug ") >>> 'joel-is-a-slug'
            # In our case, slug = slugify(name)
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)
