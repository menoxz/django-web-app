from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from listings.models import Band, Prod

def band_list(request):
    bands = Band.objects.all()
    prods = Prod.objects.all()
    return render(request, 'listings/band_list.html',{'bands': bands ,'prods': prods})

def band_detail(request, band_id):  # notez le paramètre id supplémentaire
    # band = Band.objects.get(id=band_id)
    band = get_object_or_404(Band, pk=band_id)
    return render(request,
          'listings/band_detail.html',
         {'band': band}) # nous passons l'id au modèle

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>listings</h1> <p>Nous adorons merch !</p>')

def contact_us(request):
    return HttpResponse('<h1>Contactez-nous</h1> <p>Nous adorons merch !</p>')