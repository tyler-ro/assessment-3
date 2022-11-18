from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
from django.views.generic.edit import DeleteView


def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    totalquant = Widget.objects
    return render(request, 'index.html', {'widgets': widgets, 'widget_form': widget_form})

def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('/')

class DeleteWidget(DeleteView):
    model = Widget
    success_url = '/'




