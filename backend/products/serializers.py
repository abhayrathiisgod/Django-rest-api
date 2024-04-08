from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title, validate_title_no_hello
from api.serializers import UserPublicSerializer


class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)


class ProductFormSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    related_products = UserProductInlineSerializer(
        source='user.product_set.all', read_only=True, many=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk')
    # not a good practice to put email in public serializer --- put all users in user serializer
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(
        validators=[validate_title, validate_title_no_hello])
    # name = serializers.CharField()

    class Meta:
        model = Product
        fields = [
            'email',
            'url',
            'user',
            'edit_url',
            'pk',
            'title',
            # 'name',
            'content',
            'price',
            'my_discount',
            'related_products',
        ]

    # custom validation with serializers

    # def validate_title(self, value):
    #     # __exact not null ig
    #     qs = Product.objects.filter(title__exact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")

    #     return value

    def create(self, validated_data):
        email = validated_data.pop('email')
        return super().create(validated_data)

    def get_edit_url(self, obj):
        # return f'/api/products/{obj.pk}/'
        request = self.context.get('request')

        # edge case
        if request is None:
            return None

        return reverse("product-edit", kwargs={'pk': obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
