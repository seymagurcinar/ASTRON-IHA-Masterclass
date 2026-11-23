# ASTRON İHA Masterclass – Yazılım ve Aviyonik Sistemler

## Proje Hakkında

Bu proje, PX4 Autopilot kullanılarak sabit kanatlı bir İHA'nın simülasyon ortamında otonom görev gerçekleştirmesini amaçlamaktadır.

Simülasyon PX4 SITL ve Gazebo üzerinde çalıştırılmış, görev rotası QGroundControl üzerinden oluşturulmuş ve Python MAVSDK kullanılarak uçuş başlatılmıştır.

## Kullanılan Teknolojiler

- Ubuntu 22.04
- PX4 Autopilot
- PX4 SITL
- Gazebo Sim
- QGroundControl
- Python 3
- MAVSDK
- ROS 2 Humble

## Proje Dosyaları

| Dosya | Açıklama |
|---|---|
| `mission_control.py` | PX4 bağlantısı ve telemetri bilgilerini görüntüleme |
| `preflight_check.py` | Uçuş öncesi sağlık ve hazırlık kontrolleri |
| `start_mission.py` | Arming, yüklenmiş görevi başlatma ve görev ilerlemesini izleme |
| `docs/theoretical_documentation.md` | Kullanılan sistemlerin teorik açıklamaları |
| `docs/technical_report.md` | Projenin teknik raporu |

## Kurulum

### 1. PX4 Autopilot

PX4 kaynak kodunu bilgisayarınıza indirin ve proje dizinine girin:

```bash
git clone https://github.com/PX4/PX4-Autopilot.git --recursive
cd PX4-Autopilot
```

PX4 geliştirme ortamı için resmi kurulum talimatlarını takip edin.

### 2. Python ve MAVSDK

Python 3 ve pip kurulu olmalıdır.

```bash
python3 -m pip install mavsdk==4.2.1
```

Proje klasörüne girin:

```bash
cd ~/ASTRON-IHA-Masterclass
```

## Simülasyonu Çalıştırma

PX4 SITL ve Gazebo simülasyonunu başlatmak için:

```bash
cd ~/PX4-Autopilot
make px4_sitl gz_rc_cessna
```

QGroundControl uygulamasını açın ve PX4 bağlantısının kurulmasını bekleyin.

## Otonom Görev Hazırlama

1. QGroundControl uygulamasında Plan ekranını açın.
2. Takeoff, Waypoint ve Landing görevlerini ekleyin.
3. Görev rotasını kontrol edin.
4. Görevi PX4'e yükleyin.
5. Uçuş öncesi kontrolleri gerçekleştirin.

## Python Kodlarını Çalıştırma

Proje klasöründe yeni bir terminal açın.

Uçuş öncesi kontroller:

```bash
python3 preflight_check.py
```

Telemetri bilgilerini görüntüleme:

```bash
python3 mission_control.py
```

QGroundControl üzerinden görev yüklendikten sonra otonom uçuşu başlatma:

```bash
python3 start_mission.py
```

Python uygulaması PX4'e bağlanır, uçuş öncesi kontrolleri yapar, aracı arm eder ve QGroundControl üzerinden yüklenmiş görevi başlatır.

## Simülasyon Videosu

Simülasyon uçuş kaydı:

`videos/Screencast from 11-23-2026 10:53:45 PM.webm`


