import flet as ft

def home_page():
    # Criação do componente de texto para o título
    title = ft.Text("CleanSheets, XLS Minifier", size=30, weight=ft.FontWeight.BOLD)
    
    # Criação do contêiner para envolver o título
    wrapper = ft.Container(
        content=[title],
        alignment=ft.alignment.center,
        margin=20,
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.LIGHT_BLUE_50
    )
    
    return wrapper
