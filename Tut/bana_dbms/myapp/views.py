
# Create your views here.
from django.shortcuts import render
from .models import Fabric, Fvendor, Inventory, F_V, Saleprice
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FabricNameForm, FabricQueryForm

def fabric_list(request):
    fabrics = Fabric.objects.all()
    context = {'fabrics': fabrics}
    return render(request, 'fabric_list.html', context)

def fvendor_list(request):
    vendors = Fvendor.objects.all()
    context = {'vendors': vendors}
    return render(request, 'fvendor_list.html', context)

def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {'inventories': inventories}
    return render(request, 'inventory_list.html', context)

def fv_list(request):
    fvs = F_V.objects.all()
    context = {'fvs': fvs}
    return render(request, 'fv_list.html', context)

def saleprice_list(request):
    saleprices = Saleprice.objects.all()
    context = {'saleprices': saleprices}
    return render(request, 'saleprice_list.html', context)

def fabric_inventory(request):
    if request.method == 'POST':
        form = FabricNameForm(request.POST)
        if form.is_valid():
            fabric_name = form.cleaned_data['fabric_name']
            fabric = get_object_or_404(Fabric, FabricName=fabric_name)
            inventory = Inventory.objects.filter(FabricID=fabric)
            context = {'fabric': fabric, 'inventory': inventory}
            return render(request, 'fabric_inventory.html', context)
    else:
        form = FabricNameForm()

    return render(request, 'fabric_inventory_form.html', {'form': form})




def fabric_query(request):
    if request.method == 'POST':
        form = FabricQueryForm(request.POST)
        if form.is_valid():
            fabric_name = form.cleaned_data['fabric_name']
            query_type = form.cleaned_data['query_type']
            fabric = get_object_or_404(Fabric, FabricName=fabric_name)

            if query_type == 'inventory':
                data = Inventory.objects.filter(FabricID=fabric)
                context = {'fabric': fabric, 'data': data, 'query_type': 'Inventory'}
            elif query_type == 'vendors':
                data = F_V.objects.filter(FabricID=fabric)
                context = {'fabric': fabric, 'data': data, 'query_type': 'Vendors'}
            elif query_type == 'saleprice':
                data = Saleprice.objects.filter(FabricID=fabric)
                context = {'fabric': fabric, 'data': data, 'query_type': 'Sale Price'}

            return render(request, 'fabric_query.html', context)
    else:
        form = FabricQueryForm()

    return render(request, 'fabric_query_form.html', {'form': form})
