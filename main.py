import flet as ft

def main(page: ft.Page):
    page.title = "Flet App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # یک متن ساده در وسط صفحه
    page.add(
        ft.Row(
            [
                ft.Text("سلام! این اولین برنامه فلت من است.", size=24, weight=ft.FontWeight.BOLD)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
