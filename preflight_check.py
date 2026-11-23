import asyncio

from mavsdk.asyncio import Mavsdk, Configuration, ComponentType
from mavsdk.asyncio.plugins.telemetry import TelemetryAsync


async def main():
    print("PX4 bağlantısı kuruluyor...")

    mavsdk = Mavsdk(
        Configuration.create_with_component_type(
            ComponentType.GROUND_STATION
        )
    )

    await mavsdk.add_any_connection("udpin://0.0.0.0:14540")

    print("İHA bekleniyor...")

    drone = await mavsdk.first_autopilot(10.0)

    if drone is None:
        print("Bağlantı kurulamadı!")
        return

    print("PX4 bağlantısı başarılı!")

    telemetry = TelemetryAsync(drone)

    print("Uçuş öncesi kontroller yapılıyor...")

    async for health in telemetry.subscribe_health():
        print("Global position:", health.is_global_position_ok)
        print("Home position:", health.is_home_position_ok)
        print("Armable:", health.is_armable)

        if (
            health.is_global_position_ok
            and health.is_home_position_ok
            and health.is_armable
        ):
            print("Bütün kontroller başarılı!")
            break

        print("Kontroller henüz tamamlanmadı, bekleniyor...")


if __name__ == "__main__":
    asyncio.run(main())
