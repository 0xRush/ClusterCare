from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from ..models import Mobileclinic, Resources
from ..forms import ResourceForm

# this route to show resource by it's id
@login_required(login_url='login')
def resource(request, pk):
    resource = Resources.objects.get(id=pk)
    context = {'resource': resource}
    return render(request, 'base/resource.html', context)

# this route to ceate resource
@login_required(login_url='login')
def createResource(request, fk):
    form = ResourceForm()
    mobileclinic = Mobileclinic.objects.get(id=fk)

    if request.user != mobileclinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')

    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.mobile_clinic = mobileclinic
            resource.save()
            messages.success(request, 'resource created successfully')
            return redirect('mobileclinic', pk=resource.mobile_clinic.id)

    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

@login_required(login_url='login')
def updateResource(request, pk):
    resource = Resources.objects.get(id=pk)
    form = ResourceForm(instance=resource)

    if request.user != resource.mobile_clinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')
    
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            messages.success(request, 'resource updated successfully')
            return redirect('resource', pk=resource.id)
        
    context = {'form': form}
    return render(request, 'base/mobileclinic_form.html', context)

@login_required(login_url='login')
def deleteResource(request, pk):
    resource = Resources.objects.get(id=pk)

    if request.user != resource.mobile_clinic.manager:
        messages.error(request, 'you are not allowed here')
        return redirect('home')

    if request.method == 'POST':
        try:
            resource.delete()
            messages.success(request, 'resource deleted successfully')
            return redirect('mobileclinic', pk=resource.mobile_clinic.id)
        except:
            messages.error(request, 'somthing went wrong!')
            return redirect('mobileclinic', pk=resource.mobile_clinic.id)
    
    context = {'obj': resource}
    return render(request, 'base/delete.html', context)