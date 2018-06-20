from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactUsForm
from .models import Book


def home(request):
    return render(request, 'scraper/home.html')


def search(request):
    search_query = request.GET['search_query']
    technology = request.GET.get('technology','off')
    web = request.GET.get('web','off')
    software = request.GET.get('software','off')
    hacking = request.GET.get('hacking','off')
    programming = request.GET.get('programming','off')

    if search_query:
        if technology == 'on':
            book_list = Book.objects.filter(
                Q(title__icontains=search_query),
                Q(category__icontains='technology') |  # Add keywords to categories here
                Q(category__icontains='hardware') |
                Q(category__icontains='technical')
            )
        elif web == 'on':
            book_list = Book.objects.filter(
                Q(title__icontains=search_query),
                Q(category__icontains='web') |
                Q(category__icontains='development')
            )
        elif software == 'on':
            book_list = Book.objects.filter(
                Q(title__icontains=search_query),
                Q(category__icontains='software') |
                Q(category__icontains='photoshop')
            )
        elif hacking == 'on':
            book_list = Book.objects.filter(
                Q(title__icontains=search_query),
                Q(category__icontains='hacking') |
                Q(category__icontains='cracking')
            )
        elif programming == 'on':
            book_list = Book.objects.filter(
                Q(title__icontains=search_query),
                Q(category__icontains='programming') |
                Q(category__icontains='game') |
                Q(category__icontains='java') |
                Q(category__icontains='.net') |
                Q(category__icontains='javascript') |
                Q(category__icontains='python') |
                Q(category__icontains='c')
            )
        else:
            book_list = Book.objects.filter(title__icontains=search_query)

        results_count = book_list.count()
        paginator = Paginator(book_list, 36)
        page = request.GET.get('page')
        if paginator.num_pages > 1:
            p = True
        else:
            p = False
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        return render(request, 'scraper/search.html', {
            'books':books,
            'search_query':search_query,
            'results_count':results_count
        })
    else:
        return redirect('home')


def about(request):
    return render(request, 'scraper/about.html')


def policy(request):
    return render(request, 'scraper/policy.html')


def contact_us(request):
    if request.method == 'POST':
        contactform = ContactUsForm(data=request.POST or None)
        if contactform.is_valid():
            contactform.save()
            return render(request, 'scraper/contact.html', {'message': 'Message/Feedback sent successfully.'})
    else:
        return render(request, 'scraper/contact.html')
