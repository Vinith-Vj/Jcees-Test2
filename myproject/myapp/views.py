from django.shortcuts import render, redirect
from .models import Boat,ItineraryItem, ItinerarySection, BoatingPackage, AttractionBulletPoint, MainAttraction, FoodStyle, FoodTimings, FoodBulletPoint, WhenDoesitRun, Duration, StartAndEndPoints, Inclusion, Exclusion, GoodToKnow
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def index(request):
    boats= Boat.objects.all()
    return render(request, 'index.html', {
        'boats': boats,
    })

def boat(request, slug):
    boat= Boat.objects.get(slug=slug)
    packages = BoatingPackage.objects.filter(boat=boat)

    return render(request, 'boat.html', {
        'packages': packages,
        'boat': boat,
    })


def package(request, slug):
    package = BoatingPackage.objects.get(slug=slug)

    # main_attraction = MainAttraction.objects.filter(section=package)
    # attraction_bullet_point = AttractionBulletPoint.objects.filter(section=package)
    # iteneray_desc = ItinerarySection.objects.filter(section=package)
    # iteneray_item = ItineraryItem.objects.filter(section=package)
    # food_style = FoodStyle.objects.filter(section=package)
    # food_timing = FoodTimings.objects.filter(section=package)
    # food_bullet_point = FoodBulletPoint.objects.filter(section=package)
    # when_does_it_run = WhenDoesitRun.objects.filter(section=package)
    # duration = Duration.objects.filter(section=package)
    # start_and_end_points = StartAndEndPoints.objects.filter(section=package)
    # inclusion = Inclusion.objects.filter(section=package)
    # exclusion = Exclusion.objects.filter(section=package)
    # good_to_know = GoodToKnow.objects.filter(section=package)

    return render(request, 'package.html', {
        'package': package,
        # 'main_attraction': main_attraction,
        # 'attraction_bullet_point': attraction_bullet_point,
        # 'iteneray_desc': iteneray_desc,
        # 'iteneray_item': iteneray_item,
        # 'food_style': food_style,
        # 'food_timing': food_timing,
        # 'food_bullet_point': food_bullet_point,
        # 'when_does_it_run': when_does_it_run,
        # 'duration': duration,
        # 'start_and_end_points': start_and_end_points,
        # 'inclusion': inclusion,
        # 'exclusion': exclusion,
        # 'good_to_know': good_to_know
    })

def property(request):
    return render(request, 'property.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()  # Save to DB

            # Optional: Send email to yourself
            subject = f"New Contact Form Submission from {contact.first_name} {contact.last_name}"
            message = f"""
            Name: {contact.first_name} {contact.last_name}
            Email: {contact.email}
            Phone: {contact.phone}
            Selected Topic: {contact.package_type}
            Message: {contact.message}
            """
            send_mail(
                subject, 
                message, 
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            return render(request, 'contact_success.html')  # Show success page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})