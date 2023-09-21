from django.contrib import admin
from jagruti.models import*
# Register your models here.

 
 


admin.site.register(Userregister)

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(Order)

admin.site.register(Cart)

admin.site.register(shipping)

admin.site.register(Question)

admin.site.site_header = "Bhramani Kirana Administration"

admin.site.index_title = "Bhramani Kirana"

admin.site.site_title = "Bhramani Kirana"