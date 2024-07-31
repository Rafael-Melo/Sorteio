import flet as ft
from random import Random

def main(page: ft.Page):
    page.window.icon = ft.icons.WINE_BAR
    page.title = 'Aplicativo de Sorteio'
    page.window.height = 400
    page.window.width = 350
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND

    def close_banner(e):
        page.banner.open = False
        page.update()

    def sortear(e):
        if vl_min.value=="" or vl_max.value=="" or qt_winners.value=="":
            page.banner.open = True
            page.update()
        else:
            print('Sorteio!')
        pass

    page.banner = ft.Banner(
        bgcolor=ft.colors.SURFACE_VARIANT,
        leading=ft.Icon(ft.icons.WARNING_AMBER_OUTLINED, color=ft.colors.RED, size=40),
        content=ft.Text("Ops, preencha todos os campos!", color=ft.colors.YELLOW, weight=ft.FontWeight.BOLD),
        actions=[
            ft.TextButton("OK", on_click=close_banner),
        ],
    )

    winners = [1, 2, 3]

    vl_min = ft.TextField(label='Número Mínimo', hint_text='Mínimo')

    vl_max = ft.TextField(label='Número Máximo', hint_text='Máximo')

    qt_winners = ft.TextField(label='Quantidade de Vencedores', hint_text='Quantidade')

    luck_button=ft.ElevatedButton('SORTEAR', icon=ft.icons.WINE_BAR, on_click=sortear)

    txt_winners=ft.Text(f'{winners}', size=20, weight="bold")

    layout = ft.ResponsiveRow(
        [
            ft.Container(
                vl_min,
                padding=5,
                col={"sm":4, "md":4, "xl":1},
                alignment=ft.alignment.center,
            ),
            ft.Container(
                vl_max,
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

    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)