import graphene
from graphene_django import DjangoObjectType
from .models import Product

# Определяем тип товара на основе модели
class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price")

# Определяем запросы (Query)
class Query(graphene.ObjectType):
    # Возвращает список всех товаров
    get_products = graphene.List(ProductType)
    # Возвращает один товар по его ID
    get_product = graphene.Field(ProductType, id=graphene.ID(required=True))

    def resolve_get_products(root, info):
        return Product.objects.all()

    def resolve_get_product(root, info, id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return None

# Определяем мутацию для создания товара
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

# Регистрируем мутации
class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()

# Собираем схему
schema = graphene.Schema(query=Query, mutation=Mutation)
