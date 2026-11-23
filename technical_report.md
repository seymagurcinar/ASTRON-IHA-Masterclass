# ASTRON İHA Masterclass – Teknik Rapor

## 1. Projenin Amacı

Bu çalışmanın amacı, PX4 Autopilot kullanılarak sabit kanatlı bir insansız hava aracının simülasyon ortamında otonom görev gerçekleştirmesini sağlamaktır. Görev planlama, uçuş kontrolü ve telemetri takibi farklı yazılım bileşenleri kullanılarak gerçekleştirilmiştir.

## 2. Kullanılan Sistemler

- **PX4 Autopilot:** İHA'nın uçuş kontrol yazılımıdır.
- **SITL:** Gerçek uçuş kontrol donanımı kullanmadan PX4 yazılımının simülasyonda çalıştırılmasını sağlar.
- **Gazebo:** İHA'nın ve çevrenin fiziksel simülasyonunu gerçekleştirir.
- **QGroundControl:** Görev rotasının oluşturulması, araca yüklenmesi ve uçuşun izlenmesi için kullanılır.
- **MAVLink:** Yer kontrol istasyonu ile uçuş kontrol yazılımı arasındaki haberleşme protokolüdür.
- **MAVSDK:** Python üzerinden PX4 ile haberleşmeyi ve uçuş işlemlerini gerçekleştirmeyi sağlar.
- **ROS 2 Humble:** Robotik uygulamalar için kullanılan yazılım altyapısıdır. Bu projede kurulu ortamın bir parçasıdır; görev kontrol Python kodunun doğrudan bir ROS 2 düğümü olarak çalıştırılması hedeflenmemiştir.

## 3. Uygulama Aşamaları

### 3.1. Simülasyon Ortamının Hazırlanması

Ubuntu 22.04 üzerinde PX4 Autopilot, Gazebo Sim ve gerekli Python kütüphaneleri hazırlanmıştır. PX4 SITL kullanılarak sabit kanatlı Cessna modeli Gazebo ortamında çalıştırılmıştır.

### 3.2. Görev Planlama

QGroundControl üzerinden uçuş rotası oluşturulmuştur. Görev planına Takeoff, Waypoint ve Landing aşamaları eklenmiştir. Hazırlanan görev PX4'e yüklenmiştir.

### 3.3. Python ile Uçuş Kontrolü

MAVSDK kullanılarak Python uygulaması üzerinden PX4 bağlantısı kurulmuştur.

Projede üç Python dosyası kullanılmıştır:

- `mission_control.py`: PX4 bağlantısını kurar ve telemetri bilgilerini görüntüler.
- `preflight_check.py`: Global konum, home konumu ve arm edilebilirlik durumunu kontrol eder.
- `start_mission.py`: Uçuş öncesi kontrolleri gerçekleştirir, aracı arm eder ve PX4'e yüklenmiş görevi başlatır. Görev ilerlemesini izlemek için MAVSDK görev telemetrisi kullanılır.

### 3.4. Uçuşun Gerçekleştirilmesi

QGroundControl üzerinden yüklenen görev Python uygulaması aracılığıyla başlatılmıştır. Gazebo ortamındaki sabit kanatlı İHA kalkış yapmış, tanımlanan görev rotasını takip etmiş ve iniş aşamasını tamamlamıştır.

Simülasyon sonunda araç iniş yapmış ve arm durumu kaldırılmıştır.

## 4. Sonuç

Bu çalışma kapsamında PX4 SITL, Gazebo, QGroundControl ve MAVSDK bileşenleri birlikte kullanılarak sabit kanatlı bir İHA için otonom görev simülasyonu gerçekleştirilmiştir.

Görev rotası QGroundControl üzerinden hazırlanmış, Python ve MAVSDK aracılığıyla uçuş başlatılmıştır. Simülasyon uçuşu kalkış ve iniş aşamalarıyla başarıyla tamamlanmıştır.

