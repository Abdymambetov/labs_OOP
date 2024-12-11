from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import time
import threading


class SmartDevice(ABC):
    def __init__(self, name, battery_level=100):
        self.name = name
        self.is_on = False
        self.battery_level = battery_level

    def turn_on(self):
        if self.battery_level > 0:
            self.is_on = True
            print(f"{self.name} включено.")
        else:
            print(f"{self.name} не может быть включено. Низкий заряд батареи.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} выключено.")

    @abstractmethod
    def perform_action(self):
        pass




class Light(SmartDevice):
    def __init__(self, name, brightness=50, color="White"):
        super().__init__(name)
        self.brightness = brightness
        self.color = color

    def perform_action(self):
        print(f"{self.name} настроено: яркость {self.brightness}%, цвет {self.color}.")

class Thermostat(SmartDevice):
    def __init__(self, name, battery_level=100, temperature=22):
        super().__init__(name, battery_level)
        self.temperature = temperature

    def set_temperature(self, temperature):
        if self.is_on:
            self.temperature = temperature
            print(f"{self.name} установлено на {temperature}°C.")
        else:
            print(f"{self.name} выключено, невозможно изменить температуру.")

    def perform_action(self):
        print(f"{self.name} поддерживает температуру {self.temperature}°C.")

class Camera(SmartDevice):
    def perform_action(self):
        if self.is_on:
            print(f"{self.name} записывает видео.")
        else:
            print(f"{self.name} выключено.")




class NotificationCenter:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, message):
        for subscriber in self.subscribers:
            print(f"Уведомление для {subscriber}: {message}")




class SmartHome:
    def __init__(self):
        self.devices = []
        self.schedule = []
        self.notification_center = NotificationCenter()

    def add_device(self, device):
        self.devices.append(device)
        print(f"Устройство {device.name} добавлено.")

    def remove_device(self, name):
        self.devices = [d for d in self.devices if d.name != name]
        print(f"Устройство {name} удалено.")

    def control_device(self, name, command, *args):
        for device in self.devices:
            if device.name == name:
                if command == "turn_on":
                    device.turn_on()
                elif command == "turn_off":
                    device.turn_off()
                elif command == "set_temperature" and isinstance(device, Thermostat):
                    device.set_temperature(*args)
                elif command == "perform_action":
                    device.perform_action()
                return
        print(f"Устройство {name} не найдено.")

    def status_report(self):
        print("Статус устройств:")
        for device in self.devices:
            print(f"{device.name}: {'Включено' if device.is_on else 'Выключено'}, Заряд: {device.battery_level}%.")

    def schedule_device(self, name, command, time_str):
        schedule_time = datetime.strptime(time_str, "%H:%M").time()
        self.schedule.append((name, command, schedule_time))
        print(f"Запланировано: {command} для {name} на {time_str}.")

    def run(self):
        def process_schedule():
            while True:
                now = datetime.now().time()
                for name, command, schedule_time in self.schedule[:]:
                    if now >= schedule_time:
                        self.control_device(name, command)
                        self.schedule.remove((name, command, schedule_time))
                time.sleep(1)

        threading.Thread(target=process_schedule, daemon=True).start()





# Создание умного дома
home = SmartHome()

# Подписчик уведомлений
home.notification_center.subscribe("User")

# Добавление устройств
home.add_device(Light(name="Living Room Light", brightness=70))
home.add_device(Thermostat(name="Bedroom Thermostat", battery_level=100))

# Управление устройствами
home.control_device("Living Room Light", "turn_on")
home.control_device("Bedroom Thermostat", "set_temperature", 20)

# Получение отчета
home.status_report()

# Планирование работы
home.schedule_device("Living Room Light", "turn_off", "18:00")
home.schedule_device("Bedroom Thermostat", "turn_on", "20:00")

# Запуск системы
try:
    home.run()
    while True:  # Имитируем долгую работу системы
        time.sleep(1)
except KeyboardInterrupt:
    print("Система остановлена.")
