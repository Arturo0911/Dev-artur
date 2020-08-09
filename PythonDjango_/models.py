from django.db import models


class Topic(models.Model):
    # A topic the user is learning about
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey("Topic",on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):

        if (len(str(self.text)) > 50):
            return str(self.text)[:50] + "..."
        else:
            return str(self.text)[:50] + "este textfield tiene menos de 50 letras"

        
        # Return a string representation of the mdodel.



# Create your models here.
