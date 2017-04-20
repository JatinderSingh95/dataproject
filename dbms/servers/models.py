from django.db import models
from django.core.urlresolvers import reverse

class Server(models.Model):
    name = models.CharField(max_length=200)
    ip = models.GenericIPAddressField()
    order = models.IntegerField()
    imageid = models.AutoField()
	class Image(models.Model):
   imagepath = models.ImageField(upload_to='https://source.unsplash.com/S1qSBlXnHlg') 


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('server_edit', kwargs={'pk': self.pk})