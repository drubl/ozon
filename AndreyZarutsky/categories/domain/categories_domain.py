from categories.infrastructure.models import Category

def get_ser_data(c_name: str):
    return Category.objects.get(name=c_name)

def get_all_category():
    return Category.objects.all()