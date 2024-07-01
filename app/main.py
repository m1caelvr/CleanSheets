import flet as ft
import app.controllers.file_treatment as ftm

def main(page: ft.Page):
    initial_width = 550
    initial_height = 600
    page.window_width = initial_width
    page.window_height = 600
    page.title = 'CleanSheets'
    page.window_always_on_top = True
    page.scroll = 'always'
    page.horizontal_alignment = 'center'
    
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
    
    def handle_close(e):
        page.add(ft.Text("Modal fechado"))
        page.close(dlg_modal)
        
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Planilhas Disponíveis"),
        actions=[
            ft.Row(
                controls=[
                    ft.TextButton("cancelar", on_click=lambda _: page.close(dlg_modal)),
                    ft.TextButton("Seguir", on_click=handle_close),
                ],
                width=initial_width,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        ],
    )
    
    def on_result(e: ft.FilePickerResultEvent):
        SUPPORTED_EXTENSIONS = ['xlsx', 'xls']
        
        if e.files:
            file_name_value = e.files[0].name
            file_path = e.files[0].path
            ext = file_name_value.split('.')[-1].lower()
            result_text.value = f"Caminho: {file_path}"

            if ext in SUPPORTED_EXTENSIONS:
                data_file, columns, sheetnames = ftm.file_treatment(e.files[0])
                
                print(f'sheet:   {sheetnames}')
                
                radio_group = ft.RadioGroup(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Radio(
                                    value=sheet,
                                    label=f'{sheet}',
                                ),
                                border=ft.border.all(1, ft.colors.WHITE10),
                                border_radius=ft.border_radius.all(7),
                                padding=ft.padding.all(5),
                            )
                            for sheet in sheetnames
                        ],
                        spacing=10,
                        expand=True,
                    )
                )
                
                # modal_content = ft.Container(
                #     content=radio_group,
                #     border=ft.border.all(1, ft.colors.BLACK),
                #     expand=False,
                # )
                
                dlg_modal.content = radio_group
                
                page.dialog = dlg_modal
                dlg_modal.open = True
                
                num_cols = columns if columns != 0 else 0
                
                file_name.value = f"Arquivo: {file_name_value}"

                if data_file is not None:
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
    file_name = ft.Text()
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
                width=130,
                height=30,
            )
            checkbox_container = ft.Container(
                content=checkbox,
                padding=ft.padding.all(5),
                border=ft.border.all(1, ft.colors.WHITE10),
                border_radius=ft.border_radius.all(7),
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
                        file_name,
                        result_columns,
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                checkboxes_row,
                result_text,
                result_title,
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