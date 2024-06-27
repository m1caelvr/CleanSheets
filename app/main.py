import flet as ft
from app.controllers.file_treatment import file_treatment

def main(page: ft.Page):
    initial_width = 400
    page.window_width = initial_width
    page.window_height = 600
    page.title = 'CleanSheets'
    page.window_always_on_top = True
    page.window_resizable = False
    
    title = ft.Text(
        size=25,
        weight=ft.FontWeight.BOLD,
        value='CleanSheets, XLS Minifier',
    )

    wrapper_title_value = ft.Text(
        value='Selecione o arquivo',
        size=20,
    )

    def on_result(e: ft.FilePickerResultEvent):
        SUPPORTED_EXTENSIONS = ['xlsx', 'xls']

        if e.files:
            file_name_value = e.files[0].name
            file_path = e.files[0].path
            ext = file_name_value.split('.')[-1].lower()

            if ext in SUPPORTED_EXTENSIONS:
                result_text.value = f"Arquivo selecionado: {file_name_value}\nCaminho: {file_path}"
                file_info.value = f"Arquivo: {file_name_value}"

                data_file, num_cols = file_treatment(e.files[0])

                inputs_create(num_cols)

                if data_file is not None:
                    result_title.value = 'Resultado:'
                    result_text.value = f'Dados processados: {data_file}'
                    result_columns.value = f'Número de colunas: {num_cols}'
                else:
                    result_title.value = 'Erro:'
                    result_text.value = 'Erro ao processar arquivo.'

            else:
                result_title.value = 'Erro:'
                result_text.value = 'Apenas arquivos de planilha (Excel) são permitidos.'

            page.update()

    file_picker = ft.FilePicker(on_result=on_result)
    file_info = ft.Text()
    result_title = ft.Text(size=16)
    result_text = ft.Text()
    result_columns = ft.Text()

    page.overlay.append(file_picker)

    pick_file_button = ft.ElevatedButton(
        on_click=lambda _: file_picker.pick_files(),
        width=initial_width,
        text="Upload",
    )

    checkboxes = []
    quntity_box = 15

    def inputs_create(num_checkboxes):
        for i in range(num_checkboxes):
            checkbox = ft.Checkbox(
                label=f'Checkbox {i+1}',
                value=False,
            )
            checkboxes.append(checkbox)

    checkboxes_contain = ft.Checkbox(
        label=f'Checkbox',
        value=False
    )

    result_container = ft.Container(
        width=initial_width,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        file_info,
                        result_columns,
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    # controls=checkboxes,
                    controls=[checkboxes_contain],
                    wrap=True,
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                ),
                # result_title,
                # result_text,
            ],
        )
    )

    wrapper = ft.Container(
        padding=ft.margin.all(20),
        bgcolor=ft.colors.LIGHT_BLUE_50,
        width=initial_width,
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        wrapper_title_value
                    ]
                ),
                pick_file_button,
                result_container,  # Adiciona o contêiner de resultado aqui
            ],
        ),
    )

    display = ft.Row(
        controls=[title],
        alignment='center',
    )

    page.add(
        display,
        wrapper
    )

    page.update()