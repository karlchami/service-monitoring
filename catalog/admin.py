from django.contrib import admin
from catalog.models import *

# Register your models here.
admin.site.register(Agenthostname)
admin.site.register(Client)
admin.site.register(Clientworkflow)
admin.site.register(Environment)
admin.site.register(Result)
admin.site.register(Resultdetail)
admin.site.register(Resultdetailtext)
admin.site.register(State)
admin.site.register(Task)
admin.site.register(Technology)
admin.site.register(Test)
admin.site.register(Trigger)
admin.site.register(Workflow)