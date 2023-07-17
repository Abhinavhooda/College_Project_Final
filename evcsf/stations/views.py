from django.shortcuts import render, get_object_or_404, redirect
from.models import * 

# Create your views here.

def stations(request, slug):
    stations = get_object_or_404(Station, slug=slug)
    
    if request.method == "POST":
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        if content:
            reviews = Review.objects.filter(created_by=request.user, stations=stations)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(
                    stations=stations,
                    rating=rating,
                    content=content,
                    created_by=request.user
                )
            return redirect('stations', slug=slug)
        
    return render(request, 'stations/stations.html', {'stations':stations})
        
                