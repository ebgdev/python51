# -----------------------------# ✅ Soru1:-------------------------------

# import datetime

# now = datetime.datetime.now()
# print(str(now))   # '2025-07-21 15:42:00.123456' (human-readable)
# print(repr(now))  # 'datetime.datetime(2025, 7, 21, 15, 42, 0, 123456)' (detailed, reproducible,for developers)

# ---------------

# from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title

#     def __repr__(self):
#         return f"<Book id={self.id} title='{self.title}'>"

# ---------------

# class MyClass:
#     @classmethod
#     def from_name(cls, name):
#         obj = cls.__new__(cls)  # Bypass __init__
#         obj.name = name  # Set attributes directly
#         return obj

#     @classmethod
#     def from_age(cls, age):
#         obj = cls.__new__(cls)
#         obj.age = age
#         return obj

# # Creating objects using class methods
# obj1 = MyClass.from_name("Alice")
# obj2 = MyClass.from_age(30)

# print(obj1.name)  # Output: Alice
# print(obj2.age)   # Output: 30

# -----------------------------✅ Soru2:-------------------------------


# # Ana sınıf: DeliveryRobot
# class DeliveryRobot:
#     def __init__(self, robot_id, current_location, load_capacity):
#         self.__robot_id = robot_id
#         self.__current_location = current_location
#         self.__load_capacity = load_capacity
#         self.__battery_level = 100
#         self.__status = "Idle"

#     # Getter ve setter'lar (Encapsulation)
#     def get_robot_id(self):
#         return self.__robot_id

#     def get_current_location(self):
#         return self.__current_location

#     def set_current_location(self, location):
#         self.__current_location = location

#     def get_load_capacity(self):
#         return self.__load_capacity

#     def get_battery_level(self):
#         return self.__battery_level

#     def set_battery_level(self, level):
#         self.__battery_level = max(0, min(100, level))

#     def get_status(self):
#         return self.__status

#     def set_status(self, status):
#         self.__status = status

#     # Ortak metodlar
#     def assign_delivery(self, destination, weight):
#         if weight > self.__load_capacity:
#             print(f"[{self.__robot_id}] Yük kapasitesi aşıldı! Teslimat atanamadı.")
#             return False
#         self.__status = "Delivering"
#         self.__destination = destination
#         self.__weight = weight
#         return True

#     def charge_battery(self):
#         print(f"[{self.__robot_id}] Şarj ediliyor...")
#         self.__battery_level = 100
#         self.__status = "Idle"

#     # Soyut metod simülasyonu (Override zorunlu)
#     def perform_delivery(self):
#         raise NotImplementedError("Bu metod alt sınıf tarafından uygulanmalıdır.")


# # Alt sınıflar

# class WalkingRobot(DeliveryRobot):
#     def perform_delivery(self):
#         distance = 3  # sabit varsayım
#         weight = self._DeliveryRobot__weight
#         print(f"[{self.get_robot_id()}] Teslimat başlatıldı: {distance} km – {weight} kg")
#         # Enerji tüketimi: 1% per km
#         consumption = distance * 1
#         self.set_battery_level(self.get_battery_level() - consumption)
#         self.set_status("Idle")
#         print(f"[{self.get_robot_id()}] Yürüyüş tamamlandı. Kalan batarya: {self.get_battery_level()}%")


# class DroneRobot(DeliveryRobot):
#     def perform_delivery(self):
#         distance = 3  # sabit varsayım
#         weight = self._DeliveryRobot__weight
#         print(f"[{self.get_robot_id()}] Teslimat başlatıldı: {distance} km – {weight} kg")
#         # Enerji tüketimi: 5% per km
#         consumption = distance * 5
#         self.set_battery_level(self.get_battery_level() - consumption)
#         self.set_status("Idle")
#         print(f"[{self.get_robot_id()}] Uçuş tamamlandı. Kalan batarya: {self.get_battery_level()}%")


# class AutonomousCarRobot(DeliveryRobot):
#     def perform_delivery(self):
#         distance = 12  # sabit varsayım
#         weight = self._DeliveryRobot__weight
#         print(f"[{self.get_robot_id()}] Teslimat başlatıldı: {distance} km – {weight} kg")
#         # Enerji tüketimi: 1.25% per km
#         consumption = distance * 1.25
#         self.set_battery_level(self.get_battery_level() - consumption)
#         self.set_status("Idle")
#         print(f"[{self.get_robot_id()}] Yolculuk tamamlandı. Kalan batarya: {self.get_battery_level()}%")


# # Teslimat Simülasyonu

# # Robotları oluştur
# robot1 = WalkingRobot("Walk-01", "Depot A", 5)
# robot2 = DroneRobot("Drone-01", "Depot B", 2)
# robot3 = AutonomousCarRobot("Car-03", "Depot C", 50)

# # Teslimat ata ve gerçekleştir
# if robot1.assign_delivery("Cafe 123", 3):
#     robot1.perform_delivery()

# if robot2.assign_delivery("Office 456", 1.2):
#     robot2.perform_delivery()

# if robot3.assign_delivery("Warehouse Z", 15):
#     robot3.perform_delivery()
