import flet as ft
import openpyxl as op
import app.controllers.delete_file as delf
import app.controllers.file_treatment as ftm
from app.data.json_handler import ensure_documents_json_file
from app.utils.get_data_json import load_json_data
from app.utils.get_path_json import get_path_json

def main(page: ft.Page):
    initial_width = 550
    initial_height = 600
    page.window.width = initial_width
    page.window.height = initial_height
    page.window.always_on_top = True
    page.title = 'CleanSheets'
    page.scroll = 'always'
    page.horizontal_alignment = 'center'
    
    title_value = ft.Text(
        size=25,
        weight="bold",
        value='CleanSheets, XLS Minifier',
    )
    title = ft.Row(
        controls=[title_value],
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
    selected_sheet = None
    selected_file = None
    selected_treatment = "automatic"
    selected_columns_quantity = 0
    line_specified = 1
    value_line = 0

    def update_selected_columns():
        selected_columns = [cb.content.label for cb in checkboxes if cb.content.value]
        if selected_columns:
            selected_columns_text.value = f'Colunas selecionadas:\n' + '  |  '.join(selected_columns)
            selected_columns_container.visible = True
        else:
            selected_columns_container.visible = False

        page.update()

    def inputs_create(column_names):
        checkboxes.clear()
        for i, column_name in enumerate(column_names):
            checkbox = ft.Checkbox(
                label=f'{i+1} - {column_name}',
                value=False,
                width=130,
                height=30,
                on_change=lambda _: update_selected_columns()
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

    action_button_style = ft.ButtonStyle(color=ft.colors.BLUE)
    banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            value="Selecione uma planilha",
            color=ft.colors.BLACK,
        ),
        actions=[
            ft.TextButton(text="Retry", style=action_button_style, on_click=lambda _: page.close(banner))
        ],
    )

    def handle_close(e):
        nonlocal selected_sheet, selected_file, selected_treatment, line_specified
        
        if selected_sheet and selected_file:
            _, column_counts = ftm.file_treatment(selected_file)
            
            if selected_sheet in column_counts:
                line_specified = number_input.value

                selected_columns = ftm.get_columns_from_sheet(selected_file, selected_sheet, selected_treatment, line_specified)
                
                inputs_create(selected_columns)
                
                result_columns.value = f'Número de colunas: {len(selected_columns)}'
                
                dlg_modal.open = False
                page.update()
            else:
                print(f"Planilha '{selected_sheet}' não encontrada nos dados de contagem de colunas.")
        else:
            print("Selecione um arquivo e uma planilha antes de continuar.")
            page.open(banner)

    width_input = 190

    number_input = ft.TextField(
        keyboard_type=ft.KeyboardType.NUMBER,
        label="Exemplo: '1' ",
        visible=False,
        width=width_input,
    )
            
    def toggle_number_input(i):
        if i == 1:
            number_input.visible = True
        else:
            number_input.visible = False
        page.update()

    def on_dropdown_change(e):
        nonlocal selected_treatment, value_line
        selected_treatment = e.control.value
        value_line = number_input.value if selected_treatment == "manual" else 1

        toggle_number_input(1 if selected_treatment == "manual" else 0)

    dropdown_and_number_input_row = ft.Dropdown(
        label="Selecionar primeira linha",
        options=[
            ft.dropdown.Option(
                text="Automático",
                key="automatic",
            ),
            ft.dropdown.Option(
                text="Manual",
                key="manual",
            ),
        ],
        value="automatic",
        width=width_input,
        text_size=14,
        on_change=on_dropdown_change,
    )

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Row(
            controls=[ft.Text("Planilhas Disponíveis", size=20)],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            wrap=True,
        ),
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
        selected_columns_container.visible = False

        SUPPORTED_EXTENSIONS = ['xlsx', 'xls']
        nonlocal selected_file

        if e.files:
            selected_file = e.files[0]
            file_name_value = selected_file.name
            file_path = selected_file.path
            ext = file_name_value.split('.')[-1].lower()

            if ext in SUPPORTED_EXTENSIONS:
                sheetnames, columns_sheet = ftm.file_treatment(selected_file)
                
                def on_container_click(index):
                    page.update()
                    
                    nonlocal selected_sheet
                    selected_sheet = sheetnames[index]

                    for i, container in enumerate(radio_containers):
                        if i == index:
                            container.bgcolor = ft.colors.OUTLINE_VARIANT
                        else:
                            container.bgcolor = ft.colors.TRANSPARENT
                        
                    page.update()

                radio_containers = [
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    value=f"Planilha: {sheet}",
                                    size=14,
                                ),
                                ft.Text(
                                    value=f"Colunas: {columns_sheet.get(sheet, 0)}",
                                    size=11,
                                )
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        border=ft.border.all(1, ft.colors.OUTLINE_VARIANT),
                        border_radius=ft.border_radius.all(7),
                        padding=ft.padding.all(10),
                        width=initial_width,
                        on_click=lambda _, index=i: on_container_click(index),
                    )
                    for i, sheet in enumerate(sheetnames)
                ]

                radio_group = ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                dropdown_and_number_input_row,
                                number_input,
                            ],
                            wrap=True,
                            width=initial_width,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        *radio_containers,
                    ],
                    spacing=10,
                    width=initial_width,
                    expand=True,
                )

                dlg_modal.content = radio_group
                page.overlay.append(dlg_modal)
                dlg_modal.open = True
                
                file_path_text.value = f"Caminho: {file_path}"
                file_name.value = f"Arquivo: {file_name_value}"

                if sheetnames is None:
                    result_title.value = 'Erro:'
                    file_path_text.value = 'Erro ao processar arquivo.'
            else:
                result_title.value = 'Erro:'
                file_path_text.value = 'Apenas arquivos de planilha (Excel) são permitidos.'

            page.update()
    
    file_name = ft.Text()
    result_columns = ft.Text()
    
    result_title = ft.Text(size=16)
    file_path_text = ft.Text()

    file_picker = ft.FilePicker(on_result=on_result)
    page.overlay.append(file_picker)

    pick_file_button = ft.ElevatedButton(
        on_click=lambda _: file_picker.pick_files(),
        width=initial_width,
        text="Upload",
    )


    def on_radio_change(e):
        delete_button.disabled = False
        page.update()

    radio_group_columns = ft.RadioGroup(
        content=ft.Row(
            controls=[
                ft.Radio(value="delete", label="Excluir colunas"),
                ft.Radio(value="keep", label="Manter colunas"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        on_change=on_radio_change,
    )
    
    def get_action_message(action, column_count):
        if column_count > 1:
            return "mantidas" if action == "keep" else "deletadas"
        else:
            return "mantida" if action == "keep" else "deletada"
    
    def clear_page(action, selected_columns):
        action_trated = get_action_message(action, len(selected_columns))
        columns_text = 'Colunas' if len(selected_columns) > 1 else 'Coluna'
                
        home_area_route.content = ft.Column(
            controls=[
                ft.Text(f"{columns_text}: {selected_columns} {action_trated} com sucesso!", size=16, weight="bold"),
                ft.Text(f"Para fazer um novo upload, Reinicie o app."),
            ],
            width=initial_width,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
        
        page.update()

    def delete_columns():
        selected_columns = [cb.content.label.split(' - ')[0] for cb in checkboxes if cb.content.value]
        selected_columns = list(map(int, selected_columns))
        if selected_columns:
            action = radio_group_columns.value
            file_path = selected_file.path
            sheet_name = selected_sheet
            
            if action == "delete":
                delf.delete_columns(file_path, sheet_name, selected_columns)
            else:
                workbook = op.load_workbook(filename=file_path)
                sheet = workbook[sheet_name]
                all_columns = list(range(1, sheet.max_column + 1))
                columns_to_keep = [col for col in all_columns if col not in selected_columns]
                delf.delete_columns(file_path, sheet_name, columns_to_keep)
                workbook.close()

            clear_page(action, selected_columns)
        else:
            print("Nenhuma coluna selecionada")

    delete_button = ft.ElevatedButton(
        on_click=lambda _: delete_columns(),
        text="Deletar colunas",
        disabled=True,
    )

    selected_columns_text = ft.Text(text_align=ft.TextAlign.CENTER)
    selected_columns_container = ft.Container(
        content=ft.Column(
            width=initial_width,
            controls=[
                selected_columns_text,
                radio_group_columns,
                delete_button,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        visible=False,
        width=initial_width,
        padding=ft.padding.all(10),
        border=ft.border.all(1, ft.colors.OUTLINE_VARIANT),
        border_radius=ft.border_radius.all(7),
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
                file_path_text,
                checkboxes_row,
                result_title,
                selected_columns_container,
            ]
        )
    )

    home_area_route = ft.Container(
        visible=True,
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

    EQS_title_value = ft.Text(
        value='Presets area',
        size=20,
    )

    presets_row = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        width=initial_width,
        spacing=10,
        wrap=True,
    )
    edit_preset_checkbox = ft.Checkbox(
        label='Editar preset',
        value=False,
    )

    presets = []

    def presets_inputs_create(presets_value):
        presets.clear()
        for i, column in enumerate(presets_value):
            checkbox = ft.Checkbox(
                label=f'{i+1} - {column}',
                value=True,
                width=220,
                height=30,
                on_change=lambda _: update_selected_columns()
            )
            checkbox_container = ft.Container(
                content=checkbox,
                padding=ft.padding.all(5),
                border=ft.border.all(1, ft.colors.WHITE10),
                border_radius=ft.border_radius.all(7),
            )
            presets.append(checkbox_container)
        presets_row.controls = presets
        page.update()
        print('presets created')

    def preset_tratment(e: ft.FilePickerResultEvent):
        json_file_path = get_path_json()

        selected_file = e.files[0]
        file_name_value = selected_file.name
        file_path_value = selected_file.path

        preset = load_json_data(json_file_path)
        preset_columns = preset.get('Columns', [])

        presets_inputs_create(preset_columns)

        print(f'arquivo to preset:\n nome: {file_name_value}\n Local: {file_path_value}\n colunas: {preset_columns}')

    file_to_preset = ft.FilePicker(on_result=preset_tratment)
    page.overlay.append(file_to_preset)

    def start_preset(e):
        ensure_documents_json_file()
        file_to_preset.pick_files()

    EQS_area_route = ft.Container(
        visible=False,
        padding=ft.Padding(top=0, bottom=0, left=20, right=20),
        width=initial_width,
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[EQS_title_value]
                ),
                ft.ElevatedButton(
                    width=initial_width,
                    text="Iniciar",
                    on_click=start_preset,
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[edit_preset_checkbox],
                ),
                presets_row,
            ]
        )
    )

    def changed_tab(e):
        my_index = e.control.selected_index
        home_area_route.visible = True if my_index == 0 else False
        EQS_area_route.visible = True if my_index == 1 else False
        page.update()
    
    page.navigation_bar = ft.NavigationBar(
        border=ft.border.only(top=ft.border.BorderSide(1, "black")),
        on_change=changed_tab,
        selected_index=0,
        destinations= [
            ft.NavigationBarDestination(icon=ft.icons.HOME, label='Inicio'),
            ft.NavigationBarDestination(icon=ft.icons.WORK, label='Presets'),
        ]
    )

    page.add(
        title,
        home_area_route,
        dlg_modal,
        banner,
        EQS_area_route,
    )

    page.update()