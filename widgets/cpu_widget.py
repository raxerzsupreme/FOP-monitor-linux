from textual.widgets import Static
import psutil

class CpuWidget(Static):

    def on_mount(self):
        self.set_interval(1, self.update_cpu)

    def update_cpu(self):
        usage = psutil.cpu_percent()

        physical = psutil.cpu_count(logical=False)
        logical = psutil.cpu_count()
        
        freq = psutil.cpu_freq().current / 1000

        self.update("CPU\n\n"
                    f"[bold cyan]Usage[/] : [bold white]{usage}%[/]\n"
                    f"[bold cyan]Cores[/] : [bold white]{physical} Physical[/] / [bold white]{logical} Logical[/]\n"
                    f"[bold cyan]Frequency[/] : [bold white]{freq:.2f}[/]")
        