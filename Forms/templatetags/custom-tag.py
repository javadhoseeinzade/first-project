"""from django import template
from django.template.loader import get_template
from Forms.forms import darmanjo_forms

register = template.Library()

@register.inclusion_tag("forms/darmanjo-form.html", takes_context=True)
def Darmanjo_form(context):
    request = context['request']
    if request.method == "POST":
        forms = darmanjo_forms(request.POST)
        if forms.if_valid():
            talk_about = forms.cleaned_data(talk_about)
            forms.save()
    else:
        forms = darmanjo_forms()
    return context
users_template = get_template("forms/darmanjo-form.html")

register.inclusion_tag(users_template)(Darmanjo_form)"""