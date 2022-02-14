from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import bedroom_choices, price_choices, state_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'listings': paged_listings}

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {'listing': listing}
    return render(request, 'listings/listing.html', context) 

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    print(queryset_list)

    # keyword
    if 'keywords' in request.GET:
        if request.GET['keywords']:
            queryset_list = queryset_list.filter(description__icontains=request.GET['keywords'])

    if 'city' in request.GET:
        # print(queryset_list)
        if request.GET['city']:
            queryset_list = queryset_list.filter(city__iexact = request.GET['city'])
        # print(queryset_list)
        # print(request.GET['city'])

    if 'state' in request.GET:
        # print(queryset_list)
        # print(request.GET['state'])
        # print(queryset_list)
        if request.GET['state']:
            queryset_list = queryset_list.filter(state__iexact = request.GET['state'])
        # print(queryset_list)

    if 'bedrooms' in request.GET:
        if request.GET['bedrooms']:
            queryset_list = queryset_list.filter(bedrooms__lte = request.GET['bedrooms'])

    if 'price' in request.GET:
        if request.GET['price']:
            queryset_list = queryset_list.filter(price__lte = request.GET['price'])


    context = {
        'price_choices': price_choices,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)