from pathlib import Path

from textual.widgets import DataTable


class FileTable(DataTable):
    BINDINGS = [
        ("enter", "open_file", "Открыть файл/папку"),
        ("backspace", "go_up", "На уровень выше"),
    ]

    def __init__(self, path: Path, **kwargs):
        super().__init__(**kwargs)
        self.current_path = path
        self.show_dir(self.current_path)

    def show_dir(self, path: Path) -> None:
        self.clear(columns=True)
        self.add_column(f"Содержимое папки {path}")
        for item in path.iterdir():
            if item.is_dir():
                self.add_row(f"/{item.name}")
            else:
                self.add_row(item.name)

    def action_open_file(self) -> None:
        row = self.get_row_at(self.cursor_row)
        if not row:
            return
        if len(row) == 0:
            return

        value = row[0]
        if value.startswith("/"):
            new_path = self.current_path / value[1:]
            if new_path.is_dir():
                self.current_path = new_path
                self.show_dir(self.current_path)

    def action_go_up(self) -> None:
        parent = self.current_path.parent
        if parent != self.current_path:
            self.current_path = parent
            self.show_dir(self.current_path)

# EOF