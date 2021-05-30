class Answer(model.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    like = models.ForeignKey(like)
    comment = models.ForeignKey(Comment)