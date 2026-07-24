from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Header, Footer, Static
from widgets.clock_widget import ClockWidget
from widgets.date_widget import DateWidget
from textual.containers import Horizontal


class Dashboard(App):
    CSS = """
    Grid {
        grid-size: 2 2;
        grid-columns: 1fr 1fr;
        grid-rows: 1fr 1fr;
        padding: 1;
    }

    Static {
        border: solid red;
        padding: 1;
    }

    #clock {
        width: 1fr;
    }

    #date {
        width: 30;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        with Grid():
            yield Static("CPU", id="cpu")
            yield Static("Memory", id="memory")
            yield Static("Network", id="network")
            yield Static("Processes", id="processes")

        with Horizontal(id="status_bar"):
            yield ClockWidget(id="clock")
            yield DateWidget(id="date")

        yield Footer()


if __name__ == "__main__":
    Dashboard().run()