class like(model.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)