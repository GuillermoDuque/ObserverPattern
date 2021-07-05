from observer.observer import Observer


class Dashboard(Observer):
    """
        Class that must subscribe to each of the classes that will receive weather information
    """
    def __init__(self,name):
        Observer.__init__(self, name)

    def notify_change(self, change):
        print(f"{self.name} recived changes: {change.name} {change.data}")