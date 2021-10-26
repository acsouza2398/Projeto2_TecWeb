from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return "{}. {}".format(str(self.id), self.title)