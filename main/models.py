
from django.db import models
from django.contrib.auth.models import User
from account.models import Profile

class Questions(models.Model) : 
    id = models.AutoField(primary_key=True)
    # author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, default=1)
    # user = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_responses(self):
        return self.responses.filter(parent=None)

# Create your models here.
 
#child model
class Discussion(models.Model):
    # user = models.AutoField(primary_key=True)
    id = models.AutoField(primary_key=True)
    # author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, default=1)
    # user = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, default=1)
    # author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, default=1)
    forum = models.ForeignKey(Questions,blank=True,on_delete=models.CASCADE, related_name="responses")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return str(self.body)

    def get_responses(self) : 
        return Discussion.objects.filter(parent=self)