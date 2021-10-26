from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=200)

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    id = models.AutoField(primary_key=True)
    tag = models.ForeignKey(Tag, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}. {}".format(str(self.id), self.title)