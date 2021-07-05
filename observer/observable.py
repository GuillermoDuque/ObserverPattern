from observer.observabledata import ObservableData


class Observable:
    def __init__(self, name):
        self.name = name
        self.observers = []

    def attach_observer(self, observer):
        """
        add observer to observers
        :param observer:
        :return:
        """
        self.observers.append(observer)

    def remove_observer(self, observer):
        """
        remove observer to observers
        :param observer:
        :return:
        """
        self.observers.remove(observer)

    def notify_change(self, value):
        """
        method that will notify each observable
        :param value:
        :return:
        """
        for observer in self.observers:
            observer.notify_change(ObservableData(self.name, value))
