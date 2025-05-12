from django.db import models

# Create your models here.

class Boat(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='bots/', default=1)
    video_link = models.CharField(max_length=1255, default=1)
    short_desc = models.TextField(max_length=1255)

    def __str__(self):
        return self.name

class AboutDistrictAndService(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, related_name='about')
    about = models.TextField()

    def __str__(self):
        return self.about[:30]
    
    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"

class TourPackagesSection(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, related_name='tour_about')
    about_tour_place = models.TextField()

    def __str__(self):
        return self.about_tour_place[:30]
    
class BoatFAQ(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, related_name='boat_faq')
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question[:30]


class BoatingPackage(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, related_name='packages', default=1)
    slug = models.SlugField(unique=True)
    package_name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='packages/')
    short_overview = models.CharField(max_length=250)
    places_covering = models.TextField()

    def __str__(self):
        return self.package_name
    
class PackageImage(models.Model):
    package = models.ForeignKey(BoatingPackage, related_name='package_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='package_images/')
    
class MainAttraction(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='main_attraction')
    main_attraction = models.TextField()

    def __str__(self):
        return self.main_attraction
    
class AttractionBulletPoint(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='attraction_bullet_points')
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text
    
class ItinerarySection(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, default=1, related_name='itinerary_desc')
    short_description = models.TextField()

    def __str__(self):
        return self.short_description
    
class ItineraryItem(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='itinerary_items')
    time = models.CharField(max_length=20)
    plan = models.TextField()

    def __str__(self):
        return f"{self.time} - {self.plan[:30]}..."
    
class FoodStyle(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='food_styles')
    food_style = models.CharField(max_length=200)

    def __str__(self):
        return self.food_style
    
class FoodTimings(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='foodtiming')
    time = models.CharField(max_length=20)
    food = models.TextField()

    def __str__(self):
        return f"{self.time} - {self.food[:30]}..."
    
class FoodBulletPoint(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='food_bullet_points')
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text
    
class WhenDoesitRun(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='run')
    when_does_it_run = models.CharField(max_length=300)

    def __str__(self):
        return self.when_does_it_run
    
class Duration(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='durations')
    duration = models.CharField(max_length=300)
    start_time = models.CharField(max_length=300, default='10:00 AM')
    end_time = models.CharField(max_length=300, default='5:00 PM')

    def __str__(self):
        return self.duration
    
class StartAndEndPoints(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE ,related_name='start_end_points')
    starting_point = models.TextField()
    ending_point = models.TextField()

    def __str__(self):
        return self.starting_point
    
    
class Inclusion(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='inclusion')
    bullet_points = models.CharField(max_length=300)

    def __str__(self):
        return self.bullet_points
    
class Exclusion(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='exclusions')
    bullet_points = models.CharField(max_length=300)

    def __str__(self):
        return self.bullet_points
    
class GoodToKnow(models.Model):
    section = models.ForeignKey(BoatingPackage, on_delete=models.CASCADE, related_name='goodtoknow')
    good_to_know = models.TextField()

    def __str__(self):
        return self.good_to_know
    

class Contacts(models.Model):
    first_name = models.CharField(max_length=100, default='Bruno')
    last_name = models.CharField(max_length=100, default='Mars')
    email = models.EmailField()
    PACKAGE_CHOICES = [
        ('boat', 'Boating Package'),
        ('Home stay', 'Home Stays'),
    ]

    package_type = models.CharField(max_length=20, choices=PACKAGE_CHOICES, default='boat')
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
    

class Property(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='property/')
    short_desc = models.TextField(max_length=1255)

    def __str__(self):
        return self.name

class ThumbnailImages(models.Model):
    section = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='thumbnail')
    image = models.ImageField(upload_to='property/')
    
class PropertyDetails(models.Model):
    section = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='detail')
    video = models.FileField(upload_to='property/')
    heading = models.CharField(max_length=250)
    bullet_point_heading = models.CharField(max_length=250)

    def __str__(self):
        return self.heading
    
class PropertyDetailsBulletPoints(models.Model):
    section = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='detail_bullets')
    bullet_points = models.CharField(max_length=1000)

class PropertyRemaingDetails(models.Model):
    section = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='detail_remaining')
    short_desc = models.TextField()
    welcome = models.CharField(max_length=1000)

class PropertyGallery(models.Model):
    section = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='property/') 

class PropertyAmenities(models.Model):
    section = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='amenity')
    amentity = models.CharField(max_length=350)
    amentity_image = models.ImageField(upload_to='property/') 

class StartYourLuxuriousSection(models.Model):
    section = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='luxury')
    background_image = models.ImageField(upload_to='property/') 
    short_desc = models.TextField()
    
class PropertyDiningSection(models.Model):
    section = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='dining')
    image = models.ImageField(upload_to='property/') 

class PropertyTestimonialSection(models.Model):
    section = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='testimonial_section')
    desc = models.TextField()
    image = models.ImageField(upload_to='property/') 

class PropertyTestimonial(models.Model):
    section = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='testimonial')
    guest_name = models.CharField(max_length=350)
    guest_words = models.TextField()

class DiscoverSection(models.Model):
    section = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='discover')
    place_name = models.CharField(max_length=300)
    why_choose_place = models.TextField()
