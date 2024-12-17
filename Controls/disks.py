
import shutil


class Disk:
    def __init__(self, threshold=10, used=None, total=None, percent=None):
        self.threshold = threshold
        self.used = used if used is not None else self.set_used()
        self.total = total if total is not None else self.set_total()
        self.percent = percent if percent is not None else self.set_percent()

    def to_dict(self):
        return {
            "used": self.used,
            "total": self.total,
            "percent": self.percent,
            "get_priority": self.get_priority()
        }

    def set_threshold(self, value):
        self.threshold = value


    def set_used(self):
        disks = shutil.disk_usage("/")

        self.used = round(disks.used / (1024**3),2)  # da byte a gigabyte
        return self.used 


    def set_total(self):
        disks = shutil.disk_usage("/")
        self.total = round(disks.total * 10**(-9), 2) #da byte a gigabyte
        return self.total

    def set_percent(self):
        disks = shutil.disk_usage("/")
        self.percent = round(disks.used / disks.total * 100, 1)
        return self.percent


    def get_priority(self):
        free = self.total-self.used
        if free <= self.threshold:
            return "🟠"
        else:
            return ""
