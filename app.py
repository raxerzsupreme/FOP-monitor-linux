from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Header, Footer, Static
from widgets.clock_widget import ClockWidget


class Dashboard(App):
    CSS = """
    Grid {
        grid-size: 2 2;
        grid-columns: 1fr 1fr;
        grid-rows: 1fr 1fr;
        padding: 1;
    }

    Static {
        border: solid cyan;
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        with Grid():
            yield Static("CPU", id="cpu")
            yield Static("Memory", id="memory")
            yield Static("Network", id="network")
            yield Static("Processes", id="processes")

        yield ClockWidget("Loading...")

        yield Footer()


if __name__ == "__main__":
    Dashboard().run()