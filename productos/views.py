from django.shortcuts import render

# Create your views here.
def market(request):
    context = {}
    return render(request, 'store.html', context=context)
