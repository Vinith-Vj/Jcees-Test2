from django.contrib import admin
from .models import Boat ,AboutDistrictAndService ,TourPackagesSection,BoatFAQ ,ItineraryItem, ItinerarySection, BoatingPackage, AttractionBulletPoint, MainAttraction, FoodStyle, FoodTimings, FoodBulletPoint, WhenDoesitRun, Duration, StartAndEndPoints, Inclusion, Exclusion, GoodToKnow, PackageImage, Contacts, Property, PropertyDetails, PropertyDetailsBulletPoints, PropertyRemaingDetails, ThumbnailImages, PropertyGallery, PropertyAmenities, StartYourLuxuriousSection, PropertyDiningSection, PropertyTestimonial, PropertyTestimonialSection, DiscoverSection

# Register your models here.

class AboutDistrictAndServiceInline(admin.TabularInline):
    model = AboutDistrictAndService
    extra = 1

class TourPackagesSectionInline(admin.TabularInline):
    model = TourPackagesSection
    extra = 1

class BoatFAQInline(admin.TabularInline):
    model = BoatFAQ
    extra = 1

class BoatAdmin(admin.ModelAdmin):
    inlines =[AboutDistrictAndServiceInline, TourPackagesSectionInline, BoatFAQInline]

admin.site.register(Boat, BoatAdmin)

class PackageImageInline(admin.TabularInline):
    model = PackageImage
    extra = 1

class MainAttractionInline(admin.TabularInline):
    model = MainAttraction
    extra = 1

class AttractionBulletInline(admin.TabularInline):
    model = AttractionBulletPoint
    extra = 1


class ItineraryItemInline(admin.TabularInline):
    model = ItineraryItem
    extra = 1

class ItenerarySectionInline(admin.TabularInline):
    model = ItinerarySection
    extra = 1


class FoodStyleInline(admin.TabularInline):
    model = FoodStyle
    extra = 1

class FoodTimingInline(admin.TabularInline):
    model = FoodTimings
    extra = 1

class FoodBulletInline(admin.TabularInline):
    model = FoodBulletPoint
    extra = 1

class WhenDoesItRunInline(admin.TabularInline):
    model = WhenDoesitRun
    extra = 1

class DurationInline(admin.TabularInline):
    model = Duration
    extra = 1

class StartAndEndingPointsInline(admin.TabularInline):
    model = StartAndEndPoints
    extra = 1

class InclusionInline(admin.TabularInline):
    model = Inclusion
    extra = 1

class ExclusionInline(admin.TabularInline):
    model = Exclusion
    extra = 1

class GoodToKnowInline(admin.TabularInline):
    model = GoodToKnow
    extra = 1

class AttractionAdmin(admin.ModelAdmin):
    inlines = [PackageImageInline, MainAttractionInline, AttractionBulletInline,  ItenerarySectionInline, ItineraryItemInline, FoodStyleInline, FoodTimingInline, FoodBulletInline, WhenDoesItRunInline, DurationInline, StartAndEndingPointsInline, InclusionInline, ExclusionInline, GoodToKnowInline]

admin.site.register(BoatingPackage, AttractionAdmin)


admin.site.register(Contacts)

class PropertyDetailsInline(admin.TabularInline):
    model = PropertyDetails
    extra = 1

class ThumbnailImagesInline(admin.TabularInline):
    model = ThumbnailImages
    extra = 1

class PropertyDetailsBulletPointsInline(admin.TabularInline):
    model = PropertyDetailsBulletPoints
    extra = 1

class PropertyRemaingDetailsInline(admin.TabularInline):
    model = PropertyRemaingDetails
    extra = 1

class PropertyGalleryInline(admin.TabularInline):
    model = PropertyGallery
    extra = 1

class PropertyAmenitiesInline(admin.TabularInline):
    model = PropertyAmenities
    extra = 1

class StartYourLuxuriousSectionInline(admin.TabularInline):
    model = StartYourLuxuriousSection
    extra = 1

class PropertyDiningSectionInline(admin.TabularInline):
    model = PropertyDiningSection
    extra = 1

class PropertyTestimonialSectionInline(admin.TabularInline):
    model = PropertyTestimonialSection
    extra = 1

class PropertyTestimonialInline(admin.TabularInline):
    model = PropertyTestimonial
    extra = 1

class DiscoverSectionInline(admin.TabularInline):
    model = DiscoverSection
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyDetailsInline, ThumbnailImagesInline, PropertyDetailsBulletPointsInline, PropertyRemaingDetailsInline, PropertyGalleryInline, PropertyAmenitiesInline, StartYourLuxuriousSectionInline, PropertyDiningSectionInline, PropertyTestimonialSectionInline, PropertyTestimonialInline, DiscoverSectionInline]

admin.site.register(Property, PropertyAdmin)