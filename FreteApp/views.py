from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .Apis.calculador_frete import CalculadoraFrete
from django.contrib import messages
from .forms import FormEndereco, FormCliente, FormEntrega
from .models import Entrega, Endereco, Cliente
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Configurações
CEP_PADRAO = "30170130"  # Valor do CEP padrão


def converter_valor(valor):
    valor = valor.replace(",", ".")
    valor = round(float(valor), 2)  # Arredonda o valor para duas casas decimais
    return valor


def mm_p(m):
    return m / 0.352777


@login_required
def dashboard(request):
    return render(request, "FreteApp/dashboard.html")


@login_required
def calculadora(request):
    if request.method == "POST":
        return handle_post(request)
    else:
        return render(request, "FreteApp/cotacoes.html")


@login_required
def handle_post(request):
    data = {
        "cep": request.POST.get("cep"),
        "comprimento": request.POST.get("comprimento"),
        "largura": request.POST.get("largura"),
        "altura": request.POST.get("altura"),
        "peso": request.POST.get("peso"),
    }
    if data["cep"]:
        return handle_end(request, data)
    else:
        return render(request, "FreteApp/cotacoes.html")


@login_required
def handle_end(request, data):
    calculadora = CalculadoraFrete(CEP_PADRAO)
    cep = data["cep"]
    if cep:
        endereco = calculadora.consultar_endereco(cep)
        if not endereco:
            messages.error(request, f"Atenção: o CEP {cep} é inválido.")
        else:
            end_data = {
                "rua": endereco["street"],
                "bairro": endereco["district"],
                "cidade": endereco["city"],
                "uf": endereco["stateShortname"],
                "cep": endereco["zipcode"],
                "complemento": endereco["complement"],
            }
            return handle_valor_correio(request, data, end_data)
    return render(request, "FreteApp/cotacoes.html")


@login_required
def handle_valor_correio(request, data, end_data):
    calculadora = CalculadoraFrete(CEP_PADRAO)
    cep = data["cep"]
    peso = data["peso"]
    comprimento = data["comprimento"]
    largura = data["largura"]
    altura = data["altura"]

    dimensoes_max = 200
    soma = float(comprimento) + float(largura) + float(altura)

    try:
        if soma > dimensoes_max:
            raise ValueError("As dimensões excedem o limite máximo permitido.")

        data_correio = calculadora.consultar_valor_correio(
            cep, peso, comprimento, largura, altura
        )

        dados_sedex = data_correio[0]
        dados_pac = data_correio[1]

        valor_sedex = converter_valor(dados_sedex["Valor"])
        valor_pac = converter_valor(dados_pac["Valor"])

        correio_data = {
            "valor_sedex": valor_sedex,
            "prazo_sedex": dados_sedex["PrazoEntrega"],
            "valor_pac": valor_pac,
            "prazo_pac": dados_pac["PrazoEntrega"],
        }

        return handle_valor_motoboy(request, data, end_data, correio_data)

    except ValueError as e:
        error_message = str(e)
        messages.error(
            request,
            f"Erro: {error_message} => Soma das dimensões não pode ultrapassar 200 cm.",
        )
        return render(request, "FreteApp/cotacoes.html")


@login_required
def handle_valor_motoboy(request, data, end_data, correio_data):
    calculador = CalculadoraFrete(CEP_PADRAO)
    cep = data["cep"]
    if cep:
        conteudo_inicial = {
            "logradouro": end_data["rua"],
            "bairro": end_data["bairro"],
            "uf": end_data["uf"],
            "cep": end_data["cep"],
            "cidade": end_data["cidade"],
        }
        valor_motoboy = calculador.consultar_motoboy_google(cep)
        # valor = converter_valor(valor_motoboy)
        motoboy_data = {"valor_motoboy": valor_motoboy}
        # print(motoboy_data)
        preco_inicial = {"valor_entrega": motoboy_data["valor_motoboy"]}
        form_endereco = FormEndereco(initial=conteudo_inicial)
        form_cliente = FormCliente()
        form_entrega = FormEntrega(initial=preco_inicial)
        context = {
            **correio_data,
            **end_data,
            **motoboy_data,
            "form_endereco": form_endereco,
            "form_cliente": form_cliente,
            "form_entrega": form_entrega,
        }
        return render(request, "FreteApp/cotacoes.html", context)
    return render(request, "FreteApp/cotacoes.html")


@login_required
def listar_entregas(request):
    todas_entregas = Entrega.objects.all()
    t_entregas = {
        "todas_entregas": todas_entregas,
    }

    if request.method == "POST":
        try:
            create_endereco(request)
            messages.success(request, "Endereço criado com sucesso!")
            return redirect(
                "FreteApp:entregas"
            )  # Redirecionar para a página de listagem
        except ValidationError as e:
            messages.error(request, f"Atenção: o CEP {e} é inválido.")
            return redirect(
                "FreteApp:entregas"
            )  # Redirecionar para a página de listagem com mensagem de erro

    return render(request, "FreteApp/list_entregas.html", context=t_entregas)


@login_required
def create_endereco(request):
    endereco_data = {
        "logradouro": request.POST.get("logradouro"),
        "cidade": request.POST.get("cidade"),
        "bairro": request.POST.get("bairro"),
        "numero": request.POST.get("numero"),
        "complemento": request.POST.get("complemento"),
        "uf": request.POST.get("uf"),
        "cep": request.POST.get("cep"),
    }

    create_cliente(request, endereco_data)


@login_required
def create_cliente(request, endereco_data):
    cliente_data = {
        "endereco": Endereco.objects.create(**endereco_data),
        "nome": request.POST.get("nome"),
        "telefone": request.POST.get("telefone"),
    }

    create_entrega(request, cliente_data)


@login_required
def create_entrega(request, cliente_data):
    entrega_data = {
        "cliente": Cliente.objects.create(**cliente_data),
        "pedido_numero": request.POST.get("pedido_numero"),
        "informacoes": request.POST.get("informacoes"),
        "valor_entrega": request.POST.get("valor_entrega"),
        "payment_pedido": request.POST.get("payment_pedido"),
        "payment_motoboy": request.POST.get("payment_motoboy"),
    }

    Entrega.objects.create(**entrega_data)


@login_required
def detalhes(request, identificador):
    entrega = get_object_or_404(Entrega, identificador=identificador)

    entrega = {"entrega": entrega}
    return render(request, "FreteApp/ordem_servico.html", entrega)


@login_required
def gerar_pdf(request, identificador):
    # Crie um objeto HttpResponse com o tipo de conteúdo PDF
    response = HttpResponse(content_type="application/pdf")
    entrega = get_object_or_404(Entrega, identificador=identificador)

    # Defina o cabeçalho do PDF para download
    response[
        "Content-Disposition"
    ] = f'attachment; filename="{entrega.cliente}{entrega.identificador}.pdf"'
    pdf = canvas.Canvas(response, pagesize=A4)
    pdf.drawString(mm_p(100), mm_p(280), "Loja Bibelô")

    pdf.drawString(mm_p(10), mm_p(270), "Nº Pedido.")
    pdf.drawString(mm_p(36), mm_p(270), f"{entrega.pedido_numero}")

    pdf.drawString(mm_p(10), mm_p(264), "Cliente.")
    pdf.drawString(mm_p(36), mm_p(264), f"{entrega.cliente}")

    pdf.drawString(mm_p(10), mm_p(258), "Telefone.")
    pdf.drawString(mm_p(36), mm_p(258), f"{entrega.cliente.telefone}")

    text_mult = f"{entrega.cliente.endereco.logradouro}, N°. {entrega.cliente.endereco.numero} - {entrega.cliente.endereco.complemento}"
    pdf.drawString(mm_p(10), mm_p(252), "Endereco.")
    pdf.drawString(mm_p(36), mm_p(252), text_mult)

    pdf.drawString(mm_p(10), mm_p(246), "Bairro.")
    pdf.drawString(
        mm_p(36),
        mm_p(246),
        f"{entrega.cliente.endereco.bairro} - {entrega.cliente.endereco.cep}",
    )

    pdf.drawString(mm_p(10), mm_p(240), "Produto.")
    pdf.drawString(mm_p(36), mm_p(240), f"{entrega.get_payment_pedido_display()}")

    pdf.drawString(mm_p(10), mm_p(234), "Valor Boy.")
    pdf.drawString(
        mm_p(36),
        mm_p(234),
        f"R$ {entrega.valor_entrega} - {entrega.get_payment_motoboy_display()}",
    )

    pdf.drawString(mm_p(10), mm_p(228), "Informações.")
    pdf.drawString(mm_p(36), mm_p(228), f"{entrega.informacoes}")

    pdf.showPage()
    pdf.save()

    return response


@login_required
def deletar_entrega(request, identificador):
    entrega = get_object_or_404(Entrega, identificador=identificador)

    # Certifique-se de que seu modelo de Entrega tem um relacionamento com Cliente e Endereco.
    # Se o relacionamento for chamado "cliente" e "endereco", o código ficaria assim:
    cliente = entrega.cliente
    endereco = cliente.endereco

    # Exclua o endereço associado ao cliente
    endereco.delete()

    # Em seguida, você pode excluir a entrega
    entrega.delete()

    return redirect("FreteApp:entregas")
