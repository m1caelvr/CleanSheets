# app/components/upload_component.py

import flet as ft

def upload_component():
    title_text = ft.Text(value="Selecione seu arquivo", size=15)
    upload_field = ft.TextField(label="< Fazer upload >")

    component = ft.Column(
        [
            title_text,
            upload_field
        ],
        alignment="center",
        spacing=20
    )

    return component
