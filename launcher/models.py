from django.db import models

# Create your models here please.


class InterestedUser(models.Model):
    name = models.CharField(max_length=64, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=128, null=True)
    content = models.TextField()
    via = models.CharField(max_length=24)

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_subject(self, subject):
        self.subject = subject

    def set_content(self, content):
        self.content = content

    def set_via(self, via):
        self.via = via

    def __unicode__(self):
        return self.email + " Via " + self.via