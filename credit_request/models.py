from django.db import models
from django.contrib.auth import get_user_model


class CreditRequestModel(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    req_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Credit Request'
        verbose_name_plural = 'List Of All Credit Request'

    def __str__(self):
        return self.user.email
