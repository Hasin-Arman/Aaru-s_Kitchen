from django.shortcuts import render
from recipies.models import recipyModel
def home(request):
    items=recipyModel.objects.all()
    return render(request, 'index.html', {'items':items})