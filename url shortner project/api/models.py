from random import choices
from string import ascii_letters


from django.conf import settings
from django.db import models


class Link(models.Model):
    original_link = models.URLField()
    shorten_link = models.URLField(blank=True, null=True)

    def shortener(self):
        while True:
            random_string = ''.join(choices(ascii_letters, k = 8))
            new_link = settings.HOST_URL + "/" + random_string

            if not Link.objects.filter(shorten_link=new_link).exists():
                break

        return new_link

    def save(self, *args ,**kwargs):
        if not self.shorten_link:
            new_link = self.shortener()
            self.shorten_link = new_link

        return super().save(*args, **kwargs)








