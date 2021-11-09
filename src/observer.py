from __future__ import annotations
from abc import ABC, abstractmethod
import random
from typing import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class WeatherData(Subject):

    def __init__(self):
        self._temperature = None
        self._humidity = None
        self._pressure = None
        self._observers = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        print("Subject: Detached an observer.")
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers..")
        for observer in self._observers:
            observer.update(self)

    def load_temperature(self):
        return self._temperature

    def load_humidity(self):
        return self._humidity

    def load_pressure(self):
        return self._pressure

    def load_changes(self):
        self.notify()

    def set_readings(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.load_changes()


class DisplayElement(ABC):

    @abstractmethod
    def display(self) -> None:
        pass


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, subject: Subject):
        self.subject = subject
        subject.attach(self)

    def update(self, subject: Subject) -> None:
        if isinstance(subject, WeatherData):
            self._temperature = subject.load_temperature()
            self._humidity = subject.load_humidity()
        self.display()

    def display(self):
        print(
            f"Current conditions: {self._temperature} Celsius degrees and {self._humidity}% humidity.")


class StatsDisplay(Observer, DisplayElement):

    def __init__(self, subject: Subject):
        self._temperatures = []
        self.subject = subject
        subject.attach(self)

    def update(self, subject: Subject) -> None:
        if isinstance(subject, WeatherData):
            self._temperatures.append(subject.load_temperature())
        self.display()

    def display(self):
        print(
            f"Average / Maximum / Minimum temperature = {self.average(self._temperatures)} / {max(self._temperatures)} / {min(self._temperatures)}")

    def average(self, list):
        return round(sum(list)/len(list), 2)


class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, subject: Subject):
        self.subject = subject
        self._current_pressure = 1010.1
        subject.attach(self)

    def update(self, subject: Subject) -> None:
        if isinstance(subject, WeatherData):
            self._last_pressure = self._current_pressure
            self._current_pressure = subject.load_pressure()
        self.display()

    def display(self):
        forecasts = ["Significant improvement in the weather soon!",
                     "Be ready for cold, rainy days to come",
                     "The current weather will hold on"]
        print(f"Forecast: {random.choice(forecasts)}")


if __name__ == "__main__":

    weatherData = WeatherData()
    currentConditions = CurrentConditionsDisplay(weatherData)
    statsDisplay = StatsDisplay(weatherData)
    forecastDisplay = ForecastDisplay(weatherData)
    weatherData.set_readings(26.6, 65, 1023.1)
    weatherData.set_readings(27.7, 70, 997.0)
    weatherData.set_readings(25.5, 90, 997.0)
