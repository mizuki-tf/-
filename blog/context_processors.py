from .models import Category
from django.db.models import Count

def common(request):

    context = {
        'category_list':Category.objects.annotate(post_count=Count('post')).order_by('-post_count'),
    }
    return context
