import flet as ft
    
def page(page: ft.Page):
    
    def login(e):
        
        if not entrada_nome.value:
            entrada_nome.error_text = "*"
            page.update()
            
        if not entrada_senha.value:
            entrada_senha.error_text = "*"
            page.update()
            
        else:
            homePage()
            
    def homePage():
            nome = entrada_nome.value
            senha = entrada_senha.value
            print(f"Nome: {nome}\nSenha: {senha}")
            
            page.clean()
            page.add(ft.Text(f"Olá, {nome}!\nSeja bem vindo ao meu app."))
            pass
    
    text = ft.Text(value="Tela de login", size=30)
    entrada_nome = ft.TextField(label="Digite seu usuário")
    entrada_senha = ft.TextField(label="Digite sua senha")
    
    page.add(
        text,
        entrada_nome,
        entrada_senha,
        ft.ElevatedButton("Entrar", on_click=login)
    )
    
    page.update()
    pass
    
ft.app(target=page)