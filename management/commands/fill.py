from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
            {'name': 'Бочонок для меда', 'description': 'Материалы:липа, дерево.Объем: 1,0 кг','category: 'Посуда': '', 'price': '889 руб.'}
            {'name': 'Ложка чайная', 'description': 'Набор 6 шт.', 'category': 'Столовые приборы', 'price': '420 руб.'}
            {'name': 'Обеденный стол', 'description': 'Круглый, лофт', 'category': 'Мебель', 'price': '4000 руб.'}
        ]

        products_for_create =[]
        for product_item in products_list:
            products_for_create.append(Product(product_item))

        Product.objects.bulk-create(products_for_create)
