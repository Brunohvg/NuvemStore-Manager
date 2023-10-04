from django.shortcuts import render



# Create your views here.
def gerar_link(request):
    return render(request, template_name=("LinkApp/page_link.html"))
