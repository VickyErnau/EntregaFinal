
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Posteo
from .forms import PosteoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.db.models.functions import Lower

# Create your views here.

def inicio(request):
    return render(request, "index.html")

def error(request):
    return render(request, "error.html")


#---------------------------------
# ABOUT ME
#---------------------------------

def about(request):
    return render(request, "about.html")


#---------------------------------
#POSTEOS
#---------------------------------

def post_create(request):
    if request.method == "POST":
        form = PosteoForm(request.POST, request.FILES)
        
        if form.is_valid():

            #autor_selected = Autor.objects.get(id=form.cleaned_data['autor'])

            posteo = Posteo(titulo=form.cleaned_data['titulo'],resumen=form.cleaned_data['resumen']
                        ,texto=form.cleaned_data['texto'], imagen=form.cleaned_data['imagen']) #, autor=autor_selected) 
            posteo.save()
            return redirect('posts')
        else:
            print("Operación Incorrecta!")

    form = PosteoForm()
    return render(request, 'post_create.html', {'form':form})

@login_required
def post_update(request, id):
    
    try:
        post = get_object_or_404(Posteo, id=id)

        form = {
            "post": PosteoForm(instance=post) 
        }

        if request.method == "POST":
            formulario = PosteoForm(request.POST, instance=post)

            if formulario.is_valid():
                formulario.save()
                return redirect('posts')
            else:
                form["post"] = formulario

        return render(request, 'post_update.html', form)
    except:
        return render(request, 'no_page.html')

class PosteoListView(ListView):
    model = Posteo
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.annotate(
            titulo_lower=Lower('titulo'),
            resumen_lower=Lower('resumen'),
            texto_lower=Lower('texto')
            ).filter(
                (Q(titulo_lower__icontains=query.lower())) |
                (Q(resumen_lower__icontains=query.lower())) |
                (Q(texto_lower__icontains=query.lower()))
            )
        return queryset
    

class PosteoDetailView(DetailView):
    model = Posteo
    template_name = 'post_detail.html'
    context_object_name = 'post'

class PosteoDeleteView(LoginRequiredMixin,DeleteView):
    model = Posteo
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')
    raise_exception = False