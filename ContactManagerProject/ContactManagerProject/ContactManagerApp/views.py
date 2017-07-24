from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Contact as modelContact
from .forms import ContactForm
from django.db.models import Q

def ContactList(request):
    PageSize = 5;
    if(request.GET.get('textToSearch') != None):      
      queryResult = modelContact.objects.filter(Q(LastName__contains = request.GET.get('textToSearch'))|Q(FirstName__contains = request.GET.get('textToSearch')))
    else:
      queryResult = modelContact.objects.all()
    paginator = Paginator(queryResult, PageSize)
    page = request.GET.get('page')
    try:
      ContactList = paginator.page(page)
    except PageNotAnInteger:
      ContactList = paginator.page(1)
    except EmptyPage:
      ContactList = paginator.page(paginator.num_pages)    
    return render(request, 'ContactManagerApp/index.html', {'ContactList':ContactList})

def insert_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            record = modelContact()
            record.FirstName=form['FirstName'].data
            record.LastName=form['LastName'].data
            record.Email=form['Email'].data
            record.MobileNo=form['MobileNo'].data
            record.save()
            return redirect('/contact/')
        else:
            form = ContactForm(request.POST)
            return render(request, 'ContactManagerApp/modify_contact.html', {"form":form,"Error":"Record not inserted"})
    else:
        form = ContactForm()
        return render(request, 'ContactManagerApp/modify_contact.html',{"form":form})
    

def modify_contact(request,id):
     if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            record = modelContact()
            record.id = id
            record.FirstName=form['FirstName'].data
            record.LastName=form['LastName'].data
            record.Email=form['Email'].data
            record.MobileNo=form['MobileNo'].data
            record.save()
            return redirect('/contact/')
     else:
        record = modelContact.objects.filter(pk=id)
        form = ContactForm()
        form = ContactForm(instance=record[0])
     return render(request, 'ContactManagerApp/modify_contact.html', {'form': form,'postUrl':'/contact/modify_contact/'+id})

def delete_contact(request,id):    
    record = modelContact()
    record.id = id
    record.delete()
    return redirect('/contact/')
   
       

