import flet as ft
import app.controllers.file_treatment as ftm

def main(page: ft.Page):
    initial_width = 550
    initial_height = 600
    page.window_width = initial_width
    page.window_height = initial_height
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
    
    selected_sheet = None
    selected_file = None  # Variável global para armazenar o arquivo selecionado

    def handle_close(e):
        if selected_sheet and selected_file:
            column_names = ftm.get_columns_from_sheet(selected_file, selected_sheet)
            inputs_create(len(column_names), column_names)
            dlg_modal.open = False
            page.update()
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
        nonlocal selected_file 

        if e.files:
            selected_file = e.files[0]  
            file_name_value = selected_file.name
            file_path = selected_file.path
            ext = file_name_value.split('.')[-1].lower()
            file_path_text.value = f"Caminho: {file_path}"

            if ext in SUPPORTED_EXTENSIONS:
                data_file, columns, sheetnames = ftm.file_treatment(selected_file)
                
                print(f'sheet: {sheetnames}')

                def on_radio_selected(ev):
                    nonlocal selected_sheet
                    selected_sheet = ev.control.value

                radio_group = ft.RadioGroup(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Radio(
                                    value=sheet,
                                    label=sheet,
                                ),
                                border=ft.border.all(1, ft.colors.WHITE10),
                                border_radius=ft.border_radius.all(7),
                                padding=ft.padding.all(5),
                            )
                            for sheet in sheetnames
                        ],
                        spacing=10,
                        expand=True,
                    ),
                    on_change=on_radio_selected
                )
                
                dlg_modal.content = radio_group
                
                page.dialog = dlg_modal
                dlg_modal.open = True
                
                file_name.value = f"Arquivo: {file_name_value}"

                if data_file is not None:
                    result_columns.value = f'Número de colunas: {columns}'
                else:
                    result_title.value = 'Erro:'
                    file_path_text.value = 'Erro ao processar arquivo.'
            else:
                result_title.value = 'Erro:'
                file_path_text.value = 'Apenas arquivos de planilha (Excel) são permitidos.'

            page.update()

    file_picker = ft.FilePicker(on_result=on_result)
    file_name = ft.Text()
    result_title = ft.Text(size=16)
    file_path_text = ft.Text()
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
                    wrap=True,
                    expand=True,
                ),
                checkboxes_row,
                file_path_text,
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
