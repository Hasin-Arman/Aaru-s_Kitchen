from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import recipyForm
from .models import recipyModel
from django.views.generic.edit import UpdateView
# Create your views here.
def create_recipy(request):
    form=recipyForm()
    if request.method == 'POST':
        form = recipyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'recipy.html', {'form':form})
    
    
def recipy_profile(request):
    obj=recipyModel.objects.all()
    return render(request,'profile.html',{'items':obj})

class update_recipy(UpdateView):
   model=recipyModel
   form_class=recipyForm
   template_name='recipy.html'
   success_url=reverse_lazy('recipy')
   
def search_recipy(request):
    ingredient=request.POST.get('ingredients')
    print(ingredient)
    item=recipyModel.objects.filter(ingredients=ingredient)
    return render(request, 'index.html', {'items':item})