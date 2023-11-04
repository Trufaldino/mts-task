
from django.shortcuts import render, redirect
from .models import ModelA, ModelB, ModelC
from .forms import UniversalModelForm


def get_universal_model_form(model_class):
    class UniversalForm(UniversalModelForm):
        class Meta(UniversalModelForm.Meta):
            model = model_class
    return UniversalForm


def model_list(request, model='A'):
    model_classes = {'A': ModelA, 'B': ModelB, 'C': ModelC}
    model_class = model_classes.get(model, ModelA)
    data = model_class.objects.all()
    model_fields = [field.name for field in model_class._meta.get_fields()][1:]

    UniversalForm = get_universal_model_form(model_class)

    if request.method == 'POST':
        form = UniversalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model_list', model=model)

    model_list = [(key, key) for key in model_classes.keys()]

    return render(
        request,
        'model_list.html',
        {'data': data, 'model': model, 'form': UniversalForm(), 'model_fields': model_fields, 'model_list': model_list}
    )


def add_model(request, model='A'):
    if request.method == 'POST':
        if model == 'A':
            model_class = ModelA
        elif model == 'B':
            model_class = ModelB
        else:
            model_class = ModelC

        UniversalForm = get_universal_model_form(model_class)
        form = UniversalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model_list', model=model)
    
    return redirect('model_list', model=model)