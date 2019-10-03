from django.shortcuts import render

# Create your views here.
def food_view(request):
    return render(request, 'food.html')