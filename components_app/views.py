from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .forms import ComponentForm
from .models import Component
from django.http import JsonResponse
from django.views import View
from .models import Component

def components_view(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('components_view')
    else:
        form = ComponentForm()

    components = Component.objects.all().order_by('order')
    return render(request, 'components.html', {'components': components, 'form': form})


@require_POST
def delete_component_view(request, component_id):
    component = get_object_or_404(Component, id=component_id)
    component.delete()
    return redirect('components_view')


def generate_commands(request):
    components = Component.objects.order_by('order')
    commands = ' + '.join([component.label for component in components])
    return JsonResponse({'commands': commands if commands else 'Empty'})





class GenerateNextflowView(View):
    def get(self, request, *args, **kwargs):
        components = list(Component.objects.all().values())
        return JsonResponse(components, safe=False)
