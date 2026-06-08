import os
import django

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'perfume_shop.settings')
django.setup()

from store.models import Category, Brand, Product
from django.utils.text import slugify

def seed():
    print("Seeding database...")

    # 1. Create Categories
    categories_data = [
        {'name': 'Perfume', 'image': 'https://perfumeworld.com.bd/images/thumbs/0000186_perfume_450.jpeg'},
        {'name': 'Perfume Set', 'image': 'https://perfumeworld.com.bd/images/thumbs/0000191_perfume-set_450.jpeg'},
        {'name': 'Body Product', 'image': 'https://perfumeworld.com.bd/images/thumbs/0000195_body-product_450.jpeg'},
        {'name': 'Makeup', 'image': 'https://perfumeworld.com.bd/images/thumbs/0000179_makeup_450.jpeg'},
        {'name': 'Hair Care', 'image': 'https://perfumeworld.com.bd/images/thumbs/0000199_hair-care_450.jpeg'},
    ]

    categories = {}
    for cat in categories_data:
        obj, created = Category.objects.get_or_create(
            name=cat['name'],
            defaults={
                'slug': slugify(cat['name']),
                'image_url': cat['image']
            }
        )
        categories[cat['name']] = obj
        if created:
            print(f"Created Category: {cat['name']}")

    # 2. Create Brands
    brands_data = [
        {'name': 'Dior', 'logo': 'https://perfumeworld.com.bd/images/thumbs/0000763_dior_345.png'},
        {'name': 'Chanel', 'logo': 'https://perfumeworld.com.bd/images/thumbs/0000774_chanel_345.png'},
        {'name': 'Versace', 'logo': 'https://perfumeworld.com.bd/images/thumbs/0000758_versace_345.png'},
        {'name': 'Tom Ford', 'logo': 'https://perfumeworld.com.bd/images/thumbs/0000777_tom-ford_345.png'},
        {'name': 'Creed', 'logo': 'https://perfumeworld.com.bd/images/thumbs/0001251_creed_345.jpeg'},
        {'name': 'Carolina Herrera', 'logo': 'https://perfumeworld.com.bd/images/thumbs/0000790_carolina-herrera_345.png'},
        {'name': 'Rasasi', 'logo': 'https://perfumeworld.com.bd/images/thumbs/0000767_rasasi_345.png'},
        {'name': 'YSL', 'logo': 'https://perfumeworld.com.bd/images/thumbs/0000775_ysl_345.png'},
        {'name': 'Gucci', 'logo': 'https://perfumeworld.com.bd/images/thumbs/0000752_gucci_345.png'},
        {'name': 'Afnan', 'logo': 'https://perfumeworld.com.bd/images/thumbs/0000792_afnan_345.png'},
    ]

    brands = {}
    for br in brands_data:
        obj, created = Brand.objects.get_or_create(
            name=br['name'],
            defaults={
                'slug': slugify(br['name']),
                'logo_url': br['logo']
            }
        )
        brands[br['name']] = obj
        if created:
            print(f"Created Brand: {br['name']}")

    # 3. Create Products
    products_data = [
        {
            'name': 'Rasasi Hawas Ice',
            'description': 'Hawas Ice by Rasasi is a Citrus Aromatic fragrance for men. An icy, refreshing version of the famous Hawas pour Homme, featuring mint, lemon, cardamon, and amberwood notes.',
            'price': 3800.00,
            'discount_price': None,
            'rating': 4.8,
            'category': 'Perfume',
            'brand': 'Rasasi',
            'image_url': 'https://perfumeworld.com.bd/images/thumbs/0000845_rasasi-hawas-ice_440.jpeg',
            'size_ml': '100ml',
            'is_featured': True
        },
        {
            'name': 'Tom Ford Lost Cherry',
            'description': 'Lost Cherry by Tom Ford is an amber floral fragrance for women and men. A full-bodied journey into the once-forbidden; a contrasting scent that reveals a tempting dichotomy of playful, candy-like gleam on the outside and luscious flesh on the inside.',
            'price': 49000.00,
            'discount_price': 45000.00,
            'rating': 4.9,
            'category': 'Perfume',
            'brand': 'Tom Ford',
            'image_url': 'https://perfumeworld.com.bd/images/thumbs/0001249_tom-ford-lost-cherry_440.webp',
            'size_ml': '100ml',
            'is_featured': True
        },
        {
            'name': 'Creed Aventus',
            'description': 'The exceptional Aventus was inspired by the dramatic life of a historic emperor, celebrating strength, power and success. Featuring premium pineapple, blackcurrant, birch, patchouli, and oakmoss.',
            'price': 39900.00,
            'discount_price': None,
            'rating': 4.9,
            'category': 'Perfume',
            'brand': 'Creed',
            'image_url': 'https://perfumeworld.com.bd/images/thumbs/0001192_creed-aventus_440.jpeg',
            'size_ml': '100ml',
            'is_featured': True
        },
        {
            'name': "Chanel N'5",
            'description': "Chanel N°5 is the very essence of femininity. An abstract, mysterious, powdered floral bouquet. The ultimate in luxury and sophistication, loved by generations.",
            'price': 26000.00,
            'discount_price': None,
            'rating': 4.7,
            'category': 'Perfume',
            'brand': 'Chanel',
            'image_url': 'https://perfumeworld.com.bd/images/thumbs/0000069_chanel-n5_440.jpeg',
            'size_ml': '100ml',
            'is_featured': True
        },
        {
            'name': 'YSL MYSLF L’Absolu',
            'description': 'MYSLF L’Absolu by Yves Saint Laurent is a new, intense woody floral ambery interpretation of masculinity. Bold, sensual, and modern with orange blossom and rich woods.',
            'price': 21500.00,
            'discount_price': 19900.00,
            'rating': 4.6,
            'category': 'Perfume',
            'brand': 'YSL',
            'image_url': 'https://perfumeworld.com.bd/images/thumbs/0001492_ysl-myslf-labsolu_440.webp',
            'size_ml': '100ml',
            'is_featured': True
        },
        {
            'name': 'Carolina Herrera Very Good Girl',
            'description': 'Very Good Girl is a floral fruity fragrance for women. Fun, fabulous and fearless, this fragrance takes you on a surprising olfactory journey, starting with top notes of playful redcurrant and exotic lychee.',
            'price': 14500.00,
            'discount_price': None,
            'rating': 4.5,
            'category': 'Perfume',
            'brand': 'Carolina Herrera',
            'image_url': 'https://perfumeworld.com.bd/images/thumbs/0001043_carolina-herrera-very-good-girl_440.jpeg',
            'size_ml': '80ml',
            'is_featured': True
        },
        {
            'name': 'Versace Eros EDP',
            'description': 'Eros Eau de Parfum embodies excess and provocation. The fragrance has a signature that is not afraid to show off itself, its extremes: the stark contrast between the extremely citrusy and the extremely delicate.',
            'price': 10500.00,
            'discount_price': None,
            'rating': 4.8,
            'category': 'Perfume',
            'brand': 'Versace',
            'image_url': 'https://perfumeworld.com.bd/images/thumbs/0000516_versace-eros-edp_440.jpeg',
            'size_ml': '100ml',
            'is_featured': True
        },
        {
            'name': 'Dior Sauvage EDP',
            'description': 'The powerful freshness of Sauvage exudes new sensual and mysterious facets, amply renewing itself with the signature of an ingenious composition. Calabrian bergamot, spirited and juicy, invites new spicy notes.',
            'price': 20500.00,
            'discount_price': 18500.00,
            'rating': 4.9,
            'category': 'Perfume',
            'brand': 'Dior',
            'image_url': 'https://perfumeworld.com.bd/images/thumbs/0001193_dior-sauvage-edp_440.webp',
            'size_ml': '100ml',
            'is_featured': True
        },
        {
            'name': 'Gucci Flora Gorgeous Gardenia',
            'description': 'Gorgeous Gardenia is a delicious potion of joy built around the Gardenia flower blended with solar Jasmine Absolute, cheerful Pear Blossom accord and sweet Brown Sugar accord.',
            'price': 15500.00,
            'discount_price': None,
            'rating': 4.7,
            'category': 'Perfume',
            'brand': 'Gucci',
            'image_url': 'https://perfumeworld.com.bd/images/thumbs/0000473_gucci-flora-gorgeous-gardenia_440.jpeg',
            'size_ml': '100ml',
            'is_featured': False
        }
    ]

    for prod in products_data:
        category_obj = categories[prod['category']]
        brand_obj = brands[prod['brand']]
        
        obj, created = Product.objects.get_or_create(
            name=prod['name'],
            defaults={
                'slug': slugify(prod['name']),
                'description': prod['description'],
                'price': prod['price'],
                'discount_price': prod['discount_price'],
                'stock': 15,
                'rating': prod['rating'],
                'category': category_obj,
                'brand': brand_obj,
                'image_url': prod['image_url'],
                'size_ml': prod['size_ml'],
                'is_featured': prod['is_featured']
            }
        )
        if created:
            print(f"Created Product: {prod['name']}")

    print("Database seeding completed!")

if __name__ == '__main__':
    seed()
