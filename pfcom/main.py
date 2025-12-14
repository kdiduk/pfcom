from pathlib import Path

from textual.app import App, ComposeResult

from pfcom.file_table import FileTable
from textual.widgets import Footer

class PFComApp(App):

        def compose(self) -> ComposeResult:
            yield FileTable(Path.cwd(), id="file_table")
            yield Footer()


if __name__ == "__main__":
    app = PFComApp()
    app.run()

# EOF
