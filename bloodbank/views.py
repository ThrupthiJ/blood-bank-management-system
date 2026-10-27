from django.shortcuts import render, redirect
from django.contrib import messages

from .models import (
    DonorScreening,
    ComponentSeparation,
    ColdStorage,
    Dispatch,
)

from .forms import (
    DonorScreeningForm,
    ComponentSeparationForm,
    ColdStorageForm,
    DispatchForm,
)


def dashboard(request):
    context = {
        'donor_count': DonorScreening.objects.count(),
        'component_count': ComponentSeparation.objects.count(),
        'storage_count': ColdStorage.objects.count(),
        'dispatch_count': Dispatch.objects.count(),
    }
    return render(request, 'bloodbank/dashboard.html', context)


def donors(request):
    records = DonorScreening.objects.all().order_by('-id')
    return render(request, 'bloodbank/records.html', {
        'records': records,
        'page_title': 'Donor Screening',
        'record_type': 'donors',
        'add_url': 'donor_add',
    })


def donor_add(request):
    form = DonorScreeningForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Donor record saved successfully.')
        return redirect('donors')

    return render(request, 'bloodbank/form.html', {
        'form': form,
        'page_title': 'Register Donor',
        'back_url': 'donors',
    })


def components(request):
    records = ComponentSeparation.objects.select_related(
        'donor'
    ).all().order_by('-id')

    return render(request, 'bloodbank/records.html', {
        'records': records,
        'page_title': 'Component Separation',
        'record_type': 'components',
        'add_url': 'component_add',
    })


def component_add(request):
    form = ComponentSeparationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Component record saved successfully.')
        return redirect('components')

    return render(request, 'bloodbank/form.html', {
        'form': form,
        'page_title': 'Add Component Batch',
        'back_url': 'components',
    })


def storage(request):
    records = ColdStorage.objects.select_related(
        'component'
    ).all().order_by('-id')

    return render(request, 'bloodbank/records.html', {
        'records': records,
        'page_title': 'Cold Storage',
        'record_type': 'storage',
        'add_url': 'storage_add',
    })


def storage_add(request):
    form = ColdStorageForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Storage record saved successfully.')
        return redirect('storage')

    return render(request, 'bloodbank/form.html', {
        'form': form,
        'page_title': 'Add Storage Record',
        'back_url': 'storage',
    })


def dispatches(request):
    records = Dispatch.objects.select_related(
        'storage'
    ).all().order_by('-id')

    return render(request, 'bloodbank/records.html', {
        'records': records,
        'page_title': 'Dispatch Management',
        'record_type': 'dispatches',
        'add_url': 'dispatch_add',
    })


def dispatch_add(request):
    form = DispatchForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Dispatch record saved successfully.')
        return redirect('dispatches')

    return render(request, 'bloodbank/form.html', {
        'form': form,
        'page_title': 'Create Dispatch',
        'back_url': 'dispatches',
    })

# Create your views here.
