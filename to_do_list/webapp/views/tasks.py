from django.shortcuts import get_object_or_404, redirect, render
from webapp.forms import TaskForm
from webapp.models import Tasks
from django.views.generic import TemplateView



class TaskDetailView(TemplateView):
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class TaskCreateView(TemplateView):
    template_name = 'task_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Tasks.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TaskForm
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TaskForm(request.POST)
        context['form'] = form
        if form.is_valid():
            types = form.cleaned_data.pop('type')
            task = form.save()
            task.type.set(types)
            task.save()
            return redirect('index')
        return render(request, 'task_create.html', context)

class TaskUpdateView(TemplateView):
    template_name = 'task_edit.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TaskForm(instance=context['task'])
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        task = get_object_or_404(Tasks, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=task)
        context['form'] = form
        if form.is_valid():
            task = form.save()
            return redirect('index')
        return render(request, 'task_edit.html', context)


class TaskDeleteView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Tasks, pk=kwargs['pk'])
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['task'].delete()
        return redirect('index')