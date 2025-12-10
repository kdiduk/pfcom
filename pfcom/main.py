from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import DataTable


class PFComApp(App):

    def compose(self) -> ComposeResult:
        yield DataTable(id="file_table")
    
    def on_mount(self) -> None:
        self.file_table = self.query_one("#file_table", DataTable)
        path = Path.cwd()
        self.file_table.add_column(f"Содержимое папки {path.name}")
        for item in path.iterdir():
            if item.is_dir():
                self.file_table.add_row(f"/{item.name}")
            else:
                self.file_table.add_row(item.name)    


if __name__ == "__main__":
    app = PFComApp()
    app.run()

# EOF
