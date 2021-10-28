
from django.db import models
from account.models import Profile

class Questions(models.Model) : 
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, default="anon")
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_responses(self):
        return self.responses.filter(parent=None)

class Discussion(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, default="anon")
    forum = models.ForeignKey(Questions,blank=True,on_delete=models.CASCADE, related_name="responses")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return str(self.body)

    def get_responses(self) : 
        return Discussion.objects.filter(parent=self)