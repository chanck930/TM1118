from django.shortcuts import render, redirect
from datetime import date, datetime
from .models import Entry
from django.db.models import Count
#from .forms import EntryForm

# Create your views here.
def index(request):
    entries = Entry.objects.all()
    entriesPrice = entries.filter(unitPrice__gt = 10000)
    entriesYear = entries.filter(acqDate__year__lte = datetime.today().year - 5)
    entriesGroupLoc = entries.values('loc').annotate(total=Count('loc'))
    entriesGroupUser = entries.values('endUser').annotate(total=Count('endUser'))
    context = {'entries' : entries, 'entriesPrice' : entriesPrice, 'entriesYear' : entriesYear, 'entriesGroupLoc' : entriesGroupLoc, 'entriesGroupUser' : entriesGroupUser} # Store the data in "context" dictionaries
    return render(request, 'inventory/index.html', context) # Pass the context to HTML template
