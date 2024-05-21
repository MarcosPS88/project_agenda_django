from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from contact.forms import ContactForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

                
        


# Create your views here.
@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm( request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():   #Só retorna true se o formulario não tiver nenhum erro
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contact:update', contact_id = contact.pk)
      
        return render(request,
                  'contact/create.html',
                  context= context)
    
    context = {
            'form': ContactForm(),
            'form_action': form_action,
        }
    return render(request,
                  'contact/create.html',
                  context= context)

@login_required(login_url='contact:login')
def update(request, contact_id):

    contact = get_object_or_404(Contact, 
                                pk=contact_id, 
                                show=True,
                                owner=request.user)
    form_action = reverse('contact:update', args=(contact_id,))
    
    if request.method == 'POST':
        form = ContactForm( request.POST, request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():   #Só retorna true se o formulario não tiver nenhum erro
            contact = form.save(commit=False)
            contact.save()
            return redirect('contact:update', contact_id = contact.pk)
      
        return render(request,
                  'contact/create.html',
                  context= context)
    
    context = {
            'form': ContactForm(instance=contact),
            'form_action': form_action,
        }
    return render(request,
                  'contact/create.html',
                  context= context)

@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(
                        Contact, pk=contact_id, 
                        show=True,
                        owner=request.user
    )
    confirmation = request.POST.get('confirmation', 'no')
    print('confirmation', confirmation)
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        "contact/contact.html",
        context= {'contact':contact,
        'confirmation': confirmation,
        }   ,
    )