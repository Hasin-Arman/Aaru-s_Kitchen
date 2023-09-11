from django.shortcuts import render
from recipies.models import recipyModel
from django.core.paginator import Paginator
def home(request):
    if 'value' in request.POST:
        items=recipyModel.objects.filter(ingredients__contains=request.POST['value'])
        paginator=Paginator(items, 1)
        page=request.GET.get('page')
        paged_items=paginator.get_page(page)
    else:   
        items=recipyModel.objects.all()
        paginator=Paginator(items, 2)
        page=request.GET.get('page')
        paged_items=paginator.get_page(page)
    return render(request, 'index.html', {'items':paged_items})