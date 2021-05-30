class Comment(model.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
