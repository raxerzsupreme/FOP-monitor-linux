from textual.widgets import Static
import psutil

class MemWidget(Static):

    def on_mount(self):
        self.set_interval(1, self.self_mem)

    def self_mem(self):
        memory = psutil.virtual_memory()

        mem_total = memory.total / (1024 ** 3)
        mem_used = memory.used / (1024 ** 3)
        mem_avail = memory.available / (1024 ** 3)
        mem_inactive = memory.inactive / (1024 ** 3)
        mem_usepercent = memory.percent


        self.update("Memory\n\n"
            f"[bold cyan]Total Memory[/] : [bold white]{mem_total:.2f} GB[/]\n"
            f"[bold cyan]In-use Memory[/] : [bold white]{mem_used:.2f} GB[/]\n"
            f"[bold cyan]Available Memory[/] : [bold white]{mem_avail:.2f} GB[/]\n"
            f"[bold cyan]Inactive Memory[/] : [bold white]{mem_inactive:.2f} GB[/]\n"
            f"[bold cyan]Memory Usage (In Percent)[/] : [bold white]{mem_usepercent} %[/]"

            )