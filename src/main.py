import flet as ft
import random

def main (page: ft.Page):
    page.title = "Pasword Generator"
    page.window.icon = "assets/icon.png"
    page.adaptative = True
    page.window.height = 680
    page.window.width = 550
    page.fonts = {
        "titulo": "src/fonts/BebasNeue-Regular.ttf",
        "texto" : "src/fonts/SourceCodePro-Regular.ttf"
    }

    #design 
    colors = {
        "darkBlue": "#143CCA",
        "blue": "#0179E8",
        "green": "#38E7C5"
    }

    #funções

    def criadorSenhas(num):
        letrasMa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letrasMi = "abcdefghijklmnopqrstuvwxyz"
        numeros = "0123456789"
        simbolos = "!@#$%&*()_+"
        param = ""
        senha = ""

        if(cNumbers.value == False and cSymbols.value == False and cLettersMa.value == False and cLettersMi.value == False):
            param = numeros
        param += numeros if(cNumbers.value) else ""
        param += simbolos if(cSymbols.value) else ""
        param += letrasMa if(cLettersMa.value) else ""
        param += letrasMi if(cLettersMi.value) else ""

        for i in range(num):
            senha += random.choice(param)

        print("Senha Gerada!") # test no terminal
        return senha

    def copiarSenha(e):
        page.set_clipboard(senha.value)
        print("Senha copiada!") # test no terminal

        page.open(ft.SnackBar(ft.Text("Senha copiada com sucesso para a área de transferência!", size= 17, color=colors["green"], style= ft.TextStyle(weight=ft.FontWeight.BOLD), text_align= ft.TextAlign.CENTER), duration=2000, bgcolor=colors["darkBlue"]))

        page.update()

    def updateProgram(e): 
        if(qntdElements.visible and qntdElements.value == ""):
            page.open(ft.SnackBar(ft.Text("Por favor, informe o tamanho da senha!", size= 18, color=colors["green"], style= ft.TextStyle(weight=ft.FontWeight.BOLD), text_align= ft.TextAlign.CENTER), duration=2500, bgcolor=colors["darkBlue"]))
            qntdElements.focus()
        else:

            if(qntdElements.visible):
                try:
                    num  = int(qntdElements.value)
                    senha.value = criadorSenhas(int(num))
                except ValueError:
                    page.open(ft.SnackBar(ft.Text("Por favor, insira apenas números!", size= 18, color=colors["green"], style= ft.TextStyle(weight=ft.FontWeight.BOLD), text_align= ft.TextAlign.CENTER), duration=2500, bgcolor=colors["darkBlue"]))
                    qntdElements.value = ""
                    qntdElements.focus()
                    return
                if (num == 0 or num < 0 or num > 30):
                    page.open(ft.SnackBar(ft.Text("Valor inválido! Insira outro valor.", size= 18, color=colors["green"], style= ft.TextStyle(weight=ft.FontWeight.BOLD), text_align= ft.TextAlign.CENTER), duration=2500, bgcolor=colors["darkBlue"]))
                    qntdElements.value = ""
                    qntdElements.focus()
                    return
            else:
                num = int(slider.value)
                senha.value = criadorSenhas(num)
            page.remove(line2Base)
            page.add(line2Updated)
            textPage.value = "Senha Gerada:"

        page.update()

    def voltarInicio(e):
        page.remove(line2Updated)
        page.add(line2Base)
        textPage.value = "Informe os parâmetros para gerar a senha:"

        page.update()

    def switchInput(e):
        if(qntdElements.visible):
            qntdElements.visible = False
            slider.visible = True
            btnswitch.tooltip = "Trocar para a caixa de texto"
            btnswitch.icon = ft.icons.SWITCH_LEFT_ROUNDED
        else:
            slider.visible = False
            qntdElements.visible = True
            btnswitch.tooltip = "Trocar para o slider"
            btnswitch.icon = ft.icons.SWITCH_RIGHT_ROUNDED

        page.update()

    # criação dos elementos
    titulo = ft.Text("Password Generator", size=35, color="white", text_align= ft.TextAlign.CENTER, font_family="titulo")
    btnBack = ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=voltarInicio, icon_color=colors["blue"], icon_size=30, tooltip="Voltar para o início")
    logo = ft.Image("icon.png", width=60, height=60, fit= ft.ImageFit.CONTAIN)
    divider = ft.Divider(color= colors["blue"], thickness= 3)
    btnswitch = ft.IconButton(icon=ft.Icons.SWITCH_RIGHT_ROUNDED, on_click=switchInput, icon_color=colors["green"], tooltip="Trocar para o slider")

    textPage = ft.Text("Informe os parâmetros para gerar a senha", size=18, color="white", width= 480, text_align= ft.TextAlign.CENTER, font_family="texto")
    slider = ft.Slider(min=4, max=30, divisions=26, label= "{value}", width=450, visible=False, active_color=colors["green"])
    qntdElements = ft.TextField(label="Digite o tamanho da senha",width=450, border_color="white", text_style= ft.TextStyle(font_family="texto"), focused_border_color= colors["green"])
    cSymbols = ft.Checkbox(label="Deve conter símbolos", label_style= ft.TextStyle(size=18, font_family="texto"), active_color=colors["green"])
    cNumbers = ft.Checkbox(label="Deve conter números", label_style= ft.TextStyle(size=18, font_family="texto"), active_color=colors["green"])
    cLettersMa = ft.Checkbox(label="Deve conter letras maiúsculas", label_style= ft.TextStyle(size=18, font_family="texto"), active_color=colors["green"])
    cLettersMi = ft.Checkbox(label="Deve conter letras minúsculas", label_style= ft.TextStyle(size=18, font_family="texto"), active_color=colors["green"])
    btnSend = ft.ElevatedButton("Gerar Senha", on_click=updateProgram, style = ft.ButtonStyle(text_style= ft.TextStyle(size= 18, weight=ft.FontWeight.BOLD), shadow_color= colors["green"]), width= 200, height= 50, color=colors["blue"])

    senha = ft.Text("", size=22, color="white", width= 280, style=ft.TextStyle(weight=ft.FontWeight.BOLD), text_align= ft.TextAlign.CENTER, font_family="texto")
    btnCopy = ft.IconButton(icon=ft.Icons.COPY_ALL_ROUNDED, on_click=copiarSenha, icon_color=colors["green"], tooltip="Copiar senha para área de transferência")

    #variáveis de layout
    lineInicial = ft.Row(
        [logo,titulo],
        alignment= ft.MainAxisAlignment.CENTER
    )

    textoPagina = ft.Column(
        [textPage, divider],
        horizontal_alignment= ft.CrossAxisAlignment.CENTER
    )

    line2Base = ft.Column(
        [ft.Row([qntdElements, slider, btnswitch], alignment= ft.MainAxisAlignment.CENTER), cSymbols, cNumbers, cLettersMa, cLettersMi, btnSend],
        horizontal_alignment= ft.CrossAxisAlignment.CENTER
    )

    line2Updated = ft.Column(
        [senha, ft.Row([btnBack, btnCopy], alignment= ft.MainAxisAlignment.SPACE_AROUND)],
        horizontal_alignment= ft.CrossAxisAlignment.CENTER
    )

    #adiciona os elementos na página
    page.add(lineInicial, textoPagina, line2Base)

ft.app(main, assets_dir="assets")

#fazer a build
