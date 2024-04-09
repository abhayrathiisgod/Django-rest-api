from django.db import models
from django.conf import settings
from django.db.models import Q
User = settings.AUTH_USER_MODEL


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):

        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)

        if user is not None:
            # return query sets corresponding to the user only
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
            # return qs
        return qs

# to filter whether a product is public or not


class ProductManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return Product.objects.get_queryset().search(query, user)


class Product(models.Model):
    # owner = models.ForeignKey(User)
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    title = models.CharField(max_length=50, blank=False,
                             default=" Enter Your Title ")
    content = models.CharField(
        max_length=50, blank=True, null=False, default=" Enter Your Content ")
    price = models.DecimalField(max_digits=8, decimal_places=4, default=00.000)
    public = models.BooleanField(default=True)
    objects = ProductManager()

    def __str__(self) -> str:
        return self.title

    @property
    def disc_price(self):
        return "%.2f" % (float(self.price)*0.8)

    def get_discount(self):
        return "122"
