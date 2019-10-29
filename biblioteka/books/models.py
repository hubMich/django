from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

COVER_TYPES = (
    ('soft', _('soft')),
    ('hard', _('hard')),
)

SEX_TYPES = (
    ('male', _('male')),
    ('female', _('female')),
)

class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
# Create your models here.

class Author(TimeStamp):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    is_in_public_domain  = models.BooleanField(default=False)
    sex = models.CharField(max_length=10,choices=SEX_TYPES,blank=True, null=True)
    birtday = models.DateField(blank=True, null=True)
    biogram = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="authors/%Y/%m/%d", blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.birtday.year})"

class Book(TimeStamp):
    title = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=30)
    cover_type = models.CharField(choices=COVER_TYPES, default='soft',max_length=30)
    pages = models.IntegerField()
    author = models.ManyToManyField(Author)
    cover_image = models.ImageField(upload_to="covers/%Y/%m/%d", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pub_date = models.DateField(blank=True, null=True)
    loan_data = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_avaiable = models.BooleanField(default=True)

    @property
    def authors(self):
        return ", ".join([str(a) for a in self.author.all()])

    def __str__(self):
        return f"{self.title} - {self.authors}"