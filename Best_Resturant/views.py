from django.shortcuts import render
from recipies.models import recipyModel
from django.db.models import Q
def home(request):
    if 'value' in request.POST:
        items=recipyModel.objects.filter(ingredients__contains=request.POST['value'])
    else:   
        items=recipyModel.objects.all()
    return render(request, 'index.html', {'items':items})