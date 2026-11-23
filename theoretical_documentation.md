# PX4 NEDİR?

PX4, insansız hava araçları (İHA), çok rotorlu araçlar ve sabit kanatlı uçaklar için geliştirilmiş açık kaynaklı bir uçuş kontrol yazılımıdır. Temel görevi, sensörlerden aldığı verileri işleyerek aracın uçuşunu yönetmek, dengede kalmasını sağlamak ve motor ile kontrol yüzeylerine gerekli komutları göndermektir.

PX4; GPS, IMU, barometre ve hava hızı sensörü gibi bileşenlerden gelen verileri kullanarak aracın konumunu, yönelimini, hızını ve irtifasını takip eder. Manuel kontrolün yanında önceden tanımlanmış otonom uçuş görevlerinin gerçekleştirilmesini de sağlar.

PX4, ROS 2 ile haberleşmek için uXRCE-DDS altyapısını destekler. Bu yapı sayesinde PX4 içerisindeki veriler harici görev bilgisayarına aktarılabilir ve ROS 2 üzerinden kontrol komutları gönderilebilir. MAVSDK ise Python ve C++ gibi programlama dilleri aracılığıyla PX4 ile haberleşmeyi ve araç kontrolünü kolaylaştıran bir yazılım kütüphanesidir.

PX4 genellikle QGroundControl gibi yer kontrol istasyonlarıyla birlikte kullanılır.

## PX4 Uçuş Modları

PX4 uçuş modları genel olarak manuel, destekli ve otonom modlar şeklinde incelenebilir. Modların davranışları kullanılan aracın türüne göre değişiklik gösterir. Sabit kanatlı İHA'larda kullanılan temel modlar şunlardır:

### Manuel ve Destekli Modlar

- **Manual Modu:** Kontrol büyük ölçüde pilottadır. Kumanda girdileri doğrudan aracın kontrol yüzeylerini ve motorunu yönetir.
- **Stabilized Modu:** Pilotun kontrolünü destekler. Ancak irtifayı ve uçuş rotasını otomatik olarak korumaz.
- **Altitude Modu:** Uçağın irtifasını korumaya yardımcı olur. Kumanda bırakıldığında düz uçuşa geçerek mevcut irtifasını sürdürmeye çalışır. Ancak rüzgara karşı uçuş rotasını otomatik olarak korumaz.
- **Position Modu:** GPS gibi konum bilgilerini kullanır. Pilot kumandayı bıraktığında uçağın irtifasını ve uçuş rotasını korumasına yardımcı olur.

### Akrobatik Modlar

- **Acro Modu:** Pilotun uçağın açısal hareketlerini daha doğrudan kontrol etmesini sağlar. Akrobatik manevralar için kullanılabilir. Diğer destekli modlardan farklı olarak uçağın yatay konuma dönmesini otomatik olarak sağlamaz.

### Otonom Modlar

- **Mission Modu:** QGroundControl üzerinden önceden oluşturulup uçuş kontrolcüsüne yüklenen görev planını gerçekleştirir. Kalkış, ara noktaların takibi ve iniş gibi görev adımlarını yürütür.
- **Hold Modu:** Uçağın mevcut GPS konumu çevresinde belirli bir yarıçapla daire çizerek beklemesini sağlar. Çok rotorlu araçlardan farklı olarak sabit kanatlı araçlar havada asılı kalamaz.
- **Return Modu:** Uçağın tanımlanmış güvenli dönüş noktasına veya yapılandırılmış dönüş ve iniş güzergahına yönelmesini sağlar.
- **Offboard Modu:** Uçağın harici bir bilgisayar tarafından gönderilen kontrol komutlarını takip etmesini sağlar. Bu komutlar MAVLink veya ROS 2 gibi haberleşme altyapıları üzerinden iletilebilir.

# SITL NEDİR?

SITL, gerçek bir uçuş kontrol kartı ve fiziksel İHA kullanmadan uçuş kontrol yazılımının sanal bir ortamda çalıştırılmasını sağlayan simülasyon yöntemidir.

Bu yöntem sayesinde geliştirilen kodlar, kontrol algoritmaları ve uçuş görevleri gerçek uçuş öncesinde test edilebilir. PX4 SITL ortamında motor çalıştırma, kalkış, belirlenen konuma ilerleme, görev takibi ve iniş gibi işlemler sanal olarak denenebilir.

SITL, yazılım hatalarının erken tespit edilmesini ve farklı uçuş senaryolarının güvenli bir şekilde test edilmesini sağlar.

# GAZEBO NEDİR?

Gazebo, robotların ve insansız hava araçlarının fiziksel davranışlarını sanal ortamda modellemek için kullanılan bir simülasyon yazılımıdır.

PX4 ile birlikte kullanıldığında İHA'nın sanal modelini oluşturur. Yer çekimi, hava direnci, çarpışmalar ve çevresel koşullar gibi fiziksel özellikleri simüle edebilir. Ayrıca GPS, IMU, kamera ve diğer sensörlerin sanal modellerini sağlayabilir.

PX4'ün Gazebo entegrasyonu sayesinde farklı İHA modelleri simülasyonda çalıştırılabilir. Böylece uçuş kontrol yazılımının farklı araç tiplerindeki davranışları test edilebilir.

# QGROUNDCONTROL NE İŞE YARAR?

QGroundControl, İHA'ları yönetmek ve takip etmek için kullanılan bir yer kontrol istasyonu yazılımıdır. Uçuş kontrolcüsü değildir; uçuş kontrolünü PX4 gerçekleştirirken QGroundControl kullanıcı ile uçuş kontrolcüsü arasındaki arayüz görevini üstlenir.

QGroundControl üzerinden uçuş görevleri oluşturulabilir, uçuş kontrolcüsünün parametreleri düzenlenebilir ve uçuş sırasında telemetri verileri takip edilebilir.

İrtifa, hız, konum, batarya voltajı, uçuş modu ve görev durumu gibi bilgiler arayüzde görüntülenebilir. Ayrıca kullanıcı QGroundControl üzerinden uçuş kontrolcüsüne komut gönderebilir.

PX4 ile QGroundControl arasındaki haberleşme genellikle MAVLink protokolü üzerinden gerçekleştirilir.

Kısacası QGroundControl; İHA'nın uçuş görevini planlamak, sistem ayarlarını yapmak, telemetri verilerini izlemek ve uçuşu yönetmek için kullanılır.

# MAVLink NEDİR?

MAVLink, İHA sistemlerinde kullanılan hafif ve verimli bir haberleşme protokolüdür.

PX4, QGroundControl ve görev bilgisayarı gibi farklı bileşenlerin birbiriyle iletişim kurmasını sağlar. Konum, hız, irtifa, batarya durumu ve uçuş modu gibi telemetri verilerinin aktarılmasında; ayrıca uçuş komutlarının gönderilmesinde kullanılır.

MAVLink, ikili mesaj yapısı sayesinde düşük bant genişliğiyle çalışabilir. Bu özelliği, özellikle sınırlı iletişim kapasitesine sahip İHA sistemlerinde avantaj sağlar.

Mesaj yapısında sistem kimliği, bileşen kimliği ve hata kontrolü için checksum gibi alanlar bulunur. Ayrıca uygun şekilde yapılandırıldığında mesaj imzalama mekanizmasıyla iletişimin güvenliği artırılabilir.

# MAVSDK NEDİR?

MAVSDK, İHA sistemleriyle programatik olarak haberleşmeyi ve araç kontrolünü kolaylaştıran açık kaynaklı bir yazılım kütüphanesidir.

PX4 ile kullanımına odaklanılarak geliştirilmiştir; bununla birlikte ArduPilot ile de belirli ölçüde kullanılabilir.

MAVSDK; C++, Python, Java ve Swift gibi programlama dilleri için API desteği sunar. Bu sayede geliştiriciler MAVLink mesajlarının ayrıntılarıyla doğrudan uğraşmadan araçla bağlantı kurabilir, telemetri verilerini okuyabilir ve uçuş komutları gönderebilir.

Python için sunulan MAVSDK kütüphanesi sayesinde bağlantı kurma, uçuş durumunu kontrol etme, aracı arm etme, önceden yüklenmiş görevi başlatma ve uçuş verilerini takip etme gibi işlemler gerçekleştirilebilir.

# ROS 2 VE PX4 NASIL BİRLİKTE ÇALIŞIR?

PX4, uçuş kontrol kartı üzerinde çalışan ve aracın temel uçuş kontrolünü gerçekleştiren yazılımdır. ROS 2 ise robotik uygulamaların geliştirilmesi, sensör verilerinin işlenmesi ve otonom karar mekanizmalarının oluşturulması için kullanılan bir yazılım altyapısıdır.

Bu iki sistem birlikte kullanıldığında ROS 2, İHA üzerinde bulunan Raspberry Pi veya NVIDIA Jetson gibi harici bir görev bilgisayarında çalışabilir.

Görev bilgisayarı üzerinde çalışan ROS 2 düğümleri, PX4'ten gelen sensör ve uçuş verilerini alabilir. Bu verileri işleyerek PX4'e yeni kontrol komutları gönderebilir.

PX4 ile ROS 2 arasındaki doğrudan haberleşme için uXRCE-DDS altyapısı kullanılabilir. Bu sistemde PX4 tarafında Micro XRCE-DDS Client, görev bilgisayarı tarafında ise Micro XRCE-DDS Agent çalışır.

PX4 içerisinde kullanılan uORB mesajlaşma altyapısındaki veriler, uXRCE-DDS aracılığıyla ROS 2 topic'lerine aktarılabilir. Böylece ROS 2 düğümleri PX4'ün yayınladığı verileri okuyabilir ve uygun topic'lere mesaj göndererek PX4 ile etkileşim kurabilir.

Bu yapı sayesinde ROS 2, daha karmaşık otonom görevlerin, algılama algoritmalarının ve karar mekanizmalarının geliştirilmesinde kullanılabilir.
