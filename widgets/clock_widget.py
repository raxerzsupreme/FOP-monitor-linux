from datetime import datetime

from textual.widgets import Static


class ClockWidget(Static):

    def on_mount(self):
        self.set_interval(1, self.update_clock)

    def update_clock(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.update(f"[bold cyan]Current Time[/] : [bold white]{current_time}[/]")