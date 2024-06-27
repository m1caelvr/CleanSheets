import flet as ft
# from app.routes.home_page import home_page

def main(page: ft.Page):
    # home = home_page()
    # page.add(home)
    
    title = ft.Text(
        "CleanSheets, XLS Minifier",
        size=30,
        weight=ft.FontWeight.BOLD,
    )
    
    page.add(title)
    
    page.update()
    pass
    