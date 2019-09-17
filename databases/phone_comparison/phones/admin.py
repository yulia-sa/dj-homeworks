from django.contrib import admin

from .models import Phone, AppleFeatures, GinzzuFeatures, MotorolaFeatures


class PhoneAdmin(admin.ModelAdmin):
    pass


admin.site.register(Phone, PhoneAdmin)


class AppleFeaturesAdmin(admin.ModelAdmin):
    pass


admin.site.register(AppleFeatures, AppleFeaturesAdmin)


class GinzzuFeaturesAdmin(admin.ModelAdmin):
    pass


admin.site.register(GinzzuFeatures, GinzzuFeaturesAdmin)


class MotorolaFeaturesAdmin(admin.ModelAdmin):
    pass


admin.site.register(MotorolaFeatures, MotorolaFeaturesAdmin)
