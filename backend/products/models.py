from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    # owner = models.ForeignKey(User)
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    title = models.CharField(max_length=50, blank=False,
                             default=" Enter Your Title ")
    content = models.CharField(
        max_length=50, blank=True, null=False, default=" Enter Your Content ")
    price = models.DecimalField(max_digits=8, decimal_places=4, default=00.000)

    def __str__(self) -> str:
        return self.title

    @property
    def disc_price(self):
        return "%.2f" % (float(self.price)*0.8)

    def get_discount(self):
        return "122"
