from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.template import TemplateDoesNotExist

from pages.forms import ContactMessageForm


def _page_context():
    return {"contact_form": ContactMessageForm()}


# @login_required
def root_page_view(request):
    try:
        return render(request, 'pages/demo-1.html', _page_context())
    except TemplateDoesNotExist:
        return render(request, 'pages/pages-404.html')


# @login_required
def dynamic_pages_view(request, template_name):
    try:
        return render(request, f'pages/{template_name}.html', _page_context())
    except TemplateDoesNotExist:
        return render(request, f'pages/pages-404.html')


def contact_message_view(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    form = ContactMessageForm(request.POST)
    if form.is_valid():
        form.save()
        if request.headers.get("HX-Request") == "true":
            return render(request, "partials/contact_success.html")
        return redirect("pages:index")

    context = {"contact_form": form}
    if request.headers.get("HX-Request") == "true":
        return render(request, "partials/contact_form.html", context)
    return render(request, "pages/demo-1.html", context, status=422)
