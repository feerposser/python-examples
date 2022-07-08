from django.shortcuts import render

from home.models import Declaration


def home(request):

  declarations = Declaration.objects.filter(status="A")

  return render(request, "index.html", {"declarations": declarations})