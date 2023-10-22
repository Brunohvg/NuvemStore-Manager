from reportlab.lib.pagesizes import A5
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from FreteApp.models import Entrega


def mm_p(mm):
    return mm / 0.352777


def gerar_pdf(request, identificador):
    # Crie um objeto HttpResponse com o tipo de conteúdo PDF
    response = HttpResponse(content_type="application/pdf")
    entrega = get_object_or_404(Entrega, identificador=identificador)

    # Defina o cabeçalho do PDF para download
    response[
        "Content-Disposition"
    ] = f'attachment; filename="{entrega.identificador}.pdf"'
    pdf = canvas.Canvas(response, pagesize=A5)
    pdf.drawString(mm_p(20), mm_p(100), "testes")
