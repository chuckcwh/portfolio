from django.db import models

# Create your models here.

# class Project(models.Model):
#     PROJECTS = ((1, "a"), (2, "b"), (3, "c", (4, "d"), (5, "e"))
#     name = models.PositiveSmallIntegerField(choices=PROJECTS)
#     image = models.ImageField(upload_to='project_images', blank=True, null=True)
#     description = models.TextField())
#
#     def __unicode__(self):
#         return u"{}".format(self.name)

class Email(models.Model):
    subject = models.CharField(max_length=40)
    message = models.TextField()
    sender = models.EmailField()
    receiver = models.EmailField()

    def __unicode__(self):
        return u"{}".format(self.name)