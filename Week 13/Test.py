class oi:
    def display(self):
        print("1")
class ui(oi):
    def display(self):
        print("2")

ui.display(1)
oi.display(1)