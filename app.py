import flet as ft
import random

def main(page: ft.Page):
    page.window.icon = ft.icons.WINE_BAR
    page.title = 'Aplicativo de Sorteio'
    page.window.height = 550
    page.window.width = 380
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND

    def close_banner(e):
        for overlay in page.overlay:
            if isinstance(overlay, ft.Banner):
                overlay.open = False
        page.update()

    def sortear(e):
        if min.value == "" or max.value == "" or qt_winners.value == "":
            for overlay in page.overlay:
                if isinstance(overlay, ft.Banner):
                    overlay.content = ft.Text(
                            'Ops, preencha todos os campos!',
                            color=ft.colors.YELLOW,
                            weight=ft.FontWeight.BOLD
                    )
                    overlay.open = True
            page.update()
        elif not (min.value.isdigit() and max.value.isdigit() and qt_winners.value.isdigit()):
            for overlay in page.overlay:
                if isinstance(overlay, ft.Banner):
                    overlay.content = ft.Text(
                        'Os campos devem conter apenas números!',
                        color=ft.colors.YELLOW,
                        weight=ft.FontWeight.BOLD
                    )
                    overlay.open = True
            page.update()
        else:
            vl_min = int(min.value)
            vl_max = int(max.value)
            vl_qt_winners = int(qt_winners.value)
            if vl_qt_winners > (vl_max - vl_min + 1):
                for overlay in page.overlay:
                    if isinstance(overlay, ft.Banner):
                        overlay.content = ft.Text(
                            'Quantidade de vencedores maior que o intervalo de números!',
                            color=ft.colors.YELLOW,
                            weight=ft.FontWeight.BOLD
                        )
                        overlay.open = True
                page.update()
            else:
                winners = random.sample(range(vl_min, vl_max + 1), vl_qt_winners)
                txt_winners.value = f'Vencedores: {", ".join(map(str, winners))}'
                page.update()
                
    page.overlay.append(ft.Banner(
        bgcolor=ft.colors.SURFACE_VARIANT,
        leading=ft.Icon(ft.icons.WARNING_AMBER_OUTLINED, color=ft.colors.RED, size=40),
        content=ft.Text(''),
        actions=[
            ft.TextButton('OK', on_click=close_banner),
        ],
    ))

    header = ft.Row(
        controls=[
            ft.Image(src='images/line01.png', height=100),
            ft.Image(src='images/luck.webp', height=100),
            ft.Image(src='images/line02.png', height=100)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    min = ft.TextField(label='Número Mínimo', hint_text='Mínimo')

    max = ft.TextField(label='Número Máximo', hint_text='Máximo')

    qt_winners = ft.TextField(label='Quantidade de Vencedores', hint_text='Quantidade')

    luck_button=ft.ElevatedButton('SORTEAR', icon=ft.icons.WINE_BAR, on_click=sortear)

    txt_winners=ft.Text('', size=20, weight="bold")

    layout = ft.ResponsiveRow(
        [
            ft.Container(
                min,
                padding=5,
                col={"sm":4, "md":4, "xl":1},
                alignment=ft.alignment.center,
            ),
            ft.Container(
                max,
                padding=5,
                col={"sm":12, "md":3, "xl":3},
            ),
            ft.Container(
                qt_winners,
                padding=5,
                col={"sm":12, "md":3, "xl":3},
            ),
            ft.Container(
                luck_button,
                padding=20,
                col={"sm":12, "md":3, "xl":3},
            ),
            ft.Container(
                txt_winners,
                padding=20,
                col={"sm":12, "md":3, "xl":3},
            ),
        ]
    )

    page.add(header, layout)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')