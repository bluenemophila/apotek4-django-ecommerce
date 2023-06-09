from .models import Product,ProductAttribute
from django.db.models import Min,Max
def get_filters(request):
	cats=Product.objects.distinct().values('category__title','category__id')
	brands=Product.objects.distinct().values('brand__title','brand__id')
	sizes=ProductAttribute.objects.distinct().values('size__title','size__id')
	#labels=Product.objects.distinct().values('label__title')
	minMaxPrice=ProductAttribute.objects.aggregate(Min('price'),Max('price'))
	data={
		'cats':cats,
		'brands':brands,
		'sizes':sizes,
		#'labels':labels,
		'minMaxPrice':minMaxPrice,
	}
	return data