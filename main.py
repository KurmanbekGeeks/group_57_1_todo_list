from db import main_db
import flet as ft 


def main(page: ft.Page):
    page.title = "ToDO App"
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=10)

    def create_task_row(task_id, task_text):
        task_field = ft.TextField(value=task_text, read_only=True, expand=True)

        def enable_edit(_):
            task_field.read_only = False
            task_field.update()



    task_input = ft.TextField(label='Введите задачу', read_only=False, expand=True)
    add_button = ft.ElevatedButton("ADD")

    # page.add(task_input, add_button)
    page.add(ft.Row([task_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN))




if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)

    