from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import InvestorCreationForm, InvestorChangeForm
from .models import Investor, Qualification, Passport, Document


class InvestorAdmin(UserAdmin):
    add_form = InvestorCreationForm
    form = InvestorChangeForm
    model = Investor
    list_display = ['email', 'username', ]


admin.site.register(Investor, InvestorAdmin)
admin.site.register(Passport)
admin.site.register(Document)
admin.site.register(Qualification)
