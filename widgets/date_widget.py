from datetime import datetime

from textual.widgets import Static

class DateWidget(Static):

    def on_mount(self):
            self.set_interval(1, self.update_clock)

    def update_clock(self):
        current_date = datetime.now().strftime("%A")
        self.update(f"[bold cyan]Day[/] : [bold white]{current_date}[/]")
