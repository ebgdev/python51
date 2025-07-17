# ✅ Soru1:
# __new__ ve __repr__ dunder method'lari nedir ? 
# ne ise yararlar 

# -------------------------------------------------------------------------------

# ✅ Soru2:
# Akıllı Teslimat Robotları Sistemi

# Ödev Amacı:
# Öğrencilerin inheritance (kalıtım), encapsulation (kapsülleme) ve 
# polymorphism (çok biçimlilik) kavramlarını gerçekçi bir senaryo içinde uygulamaları.



# Bir lojistik firması farklı tipte otonom teslimat robotları kullanıyor:
# ------------
# WalkingRobot: Şehir merkezinde kısa mesafe yürüyerek teslimat yapar.
# DroneRobot: Hava yoluyla hızlı teslimat yapar, ama sadece küçük yük taşıyabilir.
# AutonomousCarRobot: Uzun mesafe ve ağır yük taşıyan araçtır.


# Her robotun:
# maksimum taşıma kapasitesi,
# hızı,
# enerji tüketim algoritması,
# ve teslimat yapma şekli farklıdır.

# ‼️ Yapılacaklar:
# 1. Ana Sınıf Hiyerarşisi:
        #          DeliveryRobot (abstract/base class)
        #            /        |         \
        # WalkingRobot   DroneRobot   AutonomousCarRobot
# DeliveryRobot soyut sınıf olacak.

# Ortak değişkenler: robot_id, current_location, load_capacity, battery_level, status

# Ortak metodlar: assign_delivery(destination, weight), charge_battery()

# Soyut metod: perform_delivery()

# 2. Inheritance (Kalıtım)
# Tüm robot sınıfları DeliveryRobot'dan kalıtım alacak.

# Her alt sınıf perform_delivery() metodunu kendine özgü şekilde uygulayacak.

# 3. Encapsulation (Kapsülleme)
# Robot bilgileri private/protected olacak.

# Getter ve setter metodları ile kontrollü erişim sağlanacak.

# 4. Polymorphism (Çok Biçimlilik)
# perform_delivery() tüm robotlarda farklı çalışacak:

# WalkingRobot: yavaş ama az enerji harcar.

# DroneRobot: hızlı, fakat batarya hızlı tükenir.

# AutonomousCarRobot: bataryayı daha verimli kullanır.

# 5. Teslimat Simülasyonu
# Kod içinde en az 3 farklı robot oluşturun.

# Her robota birkaç teslimat atayın.

# Tüm robotlar için perform_delivery() çağrın ve çıktılarını karşılaştırın.

# Örnek Çıktı:

# [Drone-01] Teslimat başlatıldı: 3 km – 1.2 kg
# [Drone-01] Uçuş tamamlandı. Kalan batarya: 70%
# [Car-03] Teslimat başlatıldı: 12 km – 15 kg
# [Car-03] Yolculuk tamamlandı. Kalan batarya: 85%
