import flet as ft
import app.controllers.file_treatment as ftm
import app.controllers.delete_file as delf

def main(page: ft.Page):
    initial_width = 550
    initial_height = 600
    page.window.width = initial_width
    page.window.height = initial_height
    page.window.always_on_top = True
    page.title = 'CleanSheets'
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
    
    checkboxes_row = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=initial_width,
        spacing=10,
        wrap=True,
    )
    
    checkboxes = []

    def inputs_create(num_checkboxes, column_names):
        print(f'column_names: {column_names}')
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
        page.update()
        print('inputs created')
    
    selected_sheet = None
    selected_file = None
    
    def handle_close(e):
        if selected_sheet and selected_file:
            column_names = ftm.get_columns_from_sheet(selected_file, selected_sheet)
            inputs_create(len(column_names), column_names)
            
            result_columns.value = f'Número de colunas: {len(column_names)}'
            
            dlg_modal.open = False
            page.update()
            
        page.close(dlg_modal)
        
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Planilhas Disponíveis"),
        actions=[
            ft.Row(
                controls=[
                    ft.TextButton("Cancelar", on_click=lambda _: page.close(dlg_modal)),
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

            if ext in SUPPORTED_EXTENSIONS:
                data_file, sheetnames = ftm.file_treatment(selected_file)
                
                print(f'sheet: {sheetnames}')

                def on_container_click(index):
                    page.update()
                    
                    nonlocal selected_sheet
                    selected_sheet = sheetnames[index]

                    for i, container in enumerate(radio_containers):
                        if i == index:
                            container.bgcolor = ft.colors.WHITE10
                        else:
                            container.bgcolor = ft.colors.TRANSPARENT
                        print(f'clicked:  {index} / {i} / {container}')
                        
                    page.update()

                radio_containers = [
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    sheet,
                                    size=14,
                                ),
                                ft.Text(
                                    value=f"Colunas: {len(ftm.get_columns_from_sheet(selected_file, sheet))}",
                                    size=11,
                                )
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        border=ft.border.all(1, ft.colors.WHITE10),
                        border_radius=ft.border_radius.all(7),
                        padding=ft.padding.all(10),
                        width=initial_width,
                        on_click=lambda _, index=i: on_container_click(index),
                    )
                    for i, sheet in enumerate(sheetnames)
                ]
                
                radio_group = ft.Column(
                    controls=radio_containers,
                    spacing=10,
                    width=initial_width,
                    expand=True,
                )
                
                dlg_modal.content = radio_group
                
                page.overlay.append(dlg_modal)
                dlg_modal.open = True
                
                file_path_text.value = f"Caminho: {file_path}"
                file_name.value = f"Arquivo: {file_name_value}"

                if data_file is None:
                    result_title.value = 'Erro:'
                    file_path_text.value = 'Erro ao processar arquivo.'
            else:
                result_title.value = 'Erro:'
                file_path_text.value = 'Apenas arquivos de planilha (Excel) são permitidos.'

            page.update()

    file_picker = ft.FilePicker(on_result=on_result)
    page.overlay.append(file_picker)
    
    file_name = ft.Text()
    result_columns = ft.Text()
    
    result_title = ft.Text(size=16)
    file_path_text = ft.Text()

    pick_file_button = ft.ElevatedButton(
        on_click=lambda _: file_picker.pick_files(),
        width=initial_width,
        text="Upload",
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
                    width=initial_width,
                ),
                checkboxes_row,
                file_path_text,
                result_title,
            ]
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
    
    page.update()

    page.add(
        display,
        wrapper,
    )

    page.update()
