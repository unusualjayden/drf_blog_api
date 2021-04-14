from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=255, null=False)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.author.username}'

    class Meta:
        ordering = ['created_at']
        db_table = 'post'


class Like(models.Model):
    user = models.ForeignKey(User, related_name='liked_by', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} liked {self.post.title} on {self.created_at}'

    class Meta:
        ordering = ['created_at']
        db_table = 'like'
        unique_together = ('user', 'post')
