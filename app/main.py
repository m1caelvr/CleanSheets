import flet as ft
import app.controllers.file_treatment as ftm

def main(page: ft.Page):
    initial_width = 450
    initial_height = 550
    page.window_width = initial_width
    page.window_height = 600
    page.title = 'CleanSheets'
    page.window_always_on_top = True
    page.window_resizable = False
    page.scroll = 'always'
    
    title = ft.Text(
        size=25,
        weight="bold",
        value='CleanSheets, XLS Minifier',
    )
    display = ft.Row(
        controls=[title],
        alignment='center',
    )

    wrapper_title_value = ft.Text(
        value='Selecione o arquivo',
        size=20,
    )

        # main_window_width = page.window_width
        # main_window_height = page.window_height
        
    # def modal(e):
    #     modal_window = ft.AlertDialog(
    #         [
    #             ft.Text(value="Janela Modal", size=20),
    #             ft.Text(value="Esta janela deve ser fechada para interagir com a de fundo."),
    #             ft.ElevatedButton(
    #                 text="Fechar Janela Modal",
    #                 on_click=lambda _: page.remove(modal_window),
    #             ),
    #         ],
    #         alignment=ft.MainAxisAlignment.CENTER,
    #         expand=1,
    #     )
    
    def handle_close(e):
        page.add(ft.Text("Modal fechado"))
        
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Planilhas Disponíveis"),
        actions=[
            ft.TextButton("Fechar", on_click=lambda _: page.close(dlg_modal)),
        ],
        on_dismiss=handle_close,
    )
    
    def on_result(e: ft.FilePickerResultEvent):
        SUPPORTED_EXTENSIONS = ['xlsx', 'xls']
        
        if e.files:
            file_name_value = e.files[0].name
            file_path = e.files[0].path
            ext = file_name_value.split('.')[-1].lower()
            # result_text.value = f"Arquivo selecionado: {file_name_value}\nCaminho: {file_path}"
            result_text.value = f"Caminho: {file_path}"

            if ext in SUPPORTED_EXTENSIONS:
                data_file, columns, sheetnames = ftm.file_treatment(e.files[0])
                
                print(f'sheet:   {sheetnames}')
                
                modal_content = ft.Column(
                    controls=[
                        ft.Text(value="Planilhas encontradas:", size=18),
                        *[ft.Text(value=f"- {sheet}") for sheet in sheetnames],
                    ],
                )
                dlg_modal.content = modal_content
                
                page.open(dlg_modal)
                                
                num_cols = columns if columns != 0 else 0
                
                file_info.value = f"Arquivo: {file_name_value}"

                if data_file is not None:
                    # result_title.value = 'Resultado:'
                    # result_text.value = f'Dados processados: {data_file}'
                    result_columns.value = f'Número de colunas: {num_cols}'
                else:
                    result_title.value = 'Erro:'
                    result_text.value = 'Erro ao processar arquivo.'

                inputs_create(num_cols, data_file)
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

    def inputs_create(num_checkboxes, column_names):
        checkboxes.clear()
        for i in range(num_checkboxes):
            checkbox = ft.Checkbox(
                label=f'{i+1} - {column_names[i]}' if i < len(column_names) else f'None {i+1}',
                value=False,
                width=100,
                height=30,
            )
            checkbox_container = ft.Container(
                content=checkbox,
                padding=ft.padding.all(5),
                border=ft.border.all(1, ft.colors.BLACK),
            )
            checkboxes.append(checkbox_container)
        checkboxes_row.controls = checkboxes

    checkboxes_row = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=initial_width,
        spacing=10,
        wrap=True,
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
                checkboxes_row,
                result_title,
                result_text,
            ],
        )
    )

    wrapper = ft.Container(
        padding=ft.margin.all(20),
        width=initial_width,
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[wrapper_title_value]
                ),
                pick_file_button,
                result_container,
            ],
        ),
    )

    page.add(
        display,
        wrapper
    )

    page.update()