from django.contrib import admin
from .models import IT_Certificate
from .models import DMarketing_Certificate
from .models import WebDev_Certificate

admin.site.register(IT_Certificate)
admin.site.register(DMarketing_Certificate)
admin.site.register(WebDev_Certificate)
