from datetime import datetime

from textual.widgets import Static

class DateWidget(Static):

    def on_mount(self):
            self.set_interval(1, self.update_clock)

    def update_clock(self):
        day = datetime.now().strftime("%A")
        date = datetime.now().strftime("%d %B %Y")
        self.update(f"[bold cyan]Day[/] : [bold white]{day}[/]\n[bold cyan]Date[/] : [bold white]{date}[/]")
