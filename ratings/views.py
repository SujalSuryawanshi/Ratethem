from django.http import JsonResponse
from django.shortcuts import render
from .models import Human, RatingCount
from .forms import HumanForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q, Count, Avg

def swipe_page(request):
    humans = Human.objects.all()
    rating=RatingCount.objects.all()
    sort_by = request.GET.get('sort_by', '')
    if sort_by == 'Excellent':
        rating = rating.order_by('excellent')
    elif sort_by == 'Good':
        rating = rating.order_by('good')
    elif sort_by == 'Okay':
        rating = rating.order_by('okay')
    elif sort_by == 'Bad':
        rating = rating.order_by('bad')
    elif sort_by == 'Pathetic':
        rating = rating.order_by('pathetic')
    # Handling AJAX request
    if request.method == 'POST' and request.is_ajax():
        import json
        data = json.loads(request.body)
        human_id = data.get('human_id')
        rating = data.get('rating')

        try:
            human = Human.objects.get(id=human_id)
            human.rating = rating
            human.save()

            # Return a JSON response with the name and rating
            return JsonResponse({'name': human.name, 'rating': rating})

        except Human.DoesNotExist:
            return JsonResponse({'error': 'Human not found'}, status=400)

    return render(request, 'swipe.html', {'humans': humans,'rating':rating})


def search(request):
    category = Human.objects.all()
    query = request.GET.get('query', '')

    if query:
        humans = Human.objects.filter(
            Q(name__icontains=query) | 
            Q(bio__icontains=query) | 
            Q(occupation__icontains=query)
        )
    context = {
        
        'categor': category,
        'humans': humans,
    }
    return render(request, 'search.html', context)





from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Human

def human_list_view(request):
    # Retrieve all humans
    humans = Human.objects.all()

    # Prepare review counts for each human
    for human in humans:
        human.excellent_count = human.reviews.filter(rating='excellent').count()
        human.good_count = human.reviews.filter(rating='good').count()
        human.okay_count = human.reviews.filter(rating='okay').count()
        human.bad_count = human.reviews.filter(rating='bad').count()
        human.pathetic_count = human.reviews.filter(rating='pathetic').count()

    return render(request, 'swipe.html', {'humans': humans})


def submit_review(request):
    if request.method == "POST":
        rating = request.POST.get('rating')
        human_id = request.POST.get('human_id')

        # Get the Human object
        human = get_object_or_404(Human, id=human_id)

        # Get or create the RatingCount object for the human
        rating_count, created = RatingCount.objects.get_or_create(human=human)

        # Update the count based on the rating
        if rating == "excellent":
            rating_count.excellent += 1
        elif rating == "good":
            rating_count.good += 1
        elif rating == "okay":
            rating_count.okay += 1
        elif rating == "bad":
            rating_count.bad += 1
        elif rating == "pathetic":
            rating_count.pathetic += 1

        # Save the updated RatingCount
        rating_count.save()

        # Return the updated rating counts
        return JsonResponse({
            'excellent_count': rating_count.excellent,
            'good_count': rating_count.good,
            'okay_count': rating_count.okay,
            'bad_count': rating_count.bad,
            'pathetic_count': rating_count.pathetic,
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)



def category_view(request, category):
    # Get all humans of the given category
    humans = Human.objects.filter(occupation=category)
    # Render the category page with humans of the selected occupation
    return render(request, 'category.html', {'humans': humans, 'category': category})



@login_required
def submit_human(request):
    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            human = form.save(commit=False)
            human.added_by = request.user
            human.status = 'pending'  # Set initial status to pending
            human.save()
            return redirect('submission_success')  # Redirect to a success page or another view
    else:
        form = HumanForm()
    return render(request, 'submit_human.html', {'form': form})



@staff_member_required
def review_humans(request):
    pending_humans = Human.objects.filter(status='pending')
    return render(request, 'review_humans.html', {'pending_humans': pending_humans})

@staff_member_required
def accept_human(request, human_id):
    human = Human.objects.get(id=human_id)
    human.status = 'accepted'
    human.save()
    return redirect('review_humans')

@staff_member_required
def reject_human(request, human_id):
    human = Human.objects.get(id=human_id)
    human.status = 'rejected'
    human.save()
    return redirect('review_humans')

def submission_success(request):
    return render(request, 'submission_success.html')