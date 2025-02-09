import graphene
from graphene_django import DjangoObjectType
from .models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price")


class Query(graphene.ObjectType):
   
    get_products = graphene.List(ProductType)
  
    get_product = graphene.Field(ProductType, id=graphene.ID(required=True))

    def resolve_get_products(root, info):
        return Product.objects.all()

    def resolve_get_product(root, info, id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return None


class CreateProduct(graphene.Mutation):
    product = graphene.Field(ProductType)
    id = graphene.ID()

    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        price = graphene.Float(required=True)

    def mutate(root, info, name, description, price):
        product = Product(name=name, description=description, price=price)
        product.save()
        return CreateProduct(product=product, id=product.id)


class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
