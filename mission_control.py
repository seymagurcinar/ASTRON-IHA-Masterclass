
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

    async for position in telemetry.subscribe_position():
        print(f"Enlem: {position.latitude_deg:.6f}")
        print(f"Boylam: {position.longitude_deg:.6f}")
        print(f"İrtifa: {position.relative_altitude_m:.2f} m")
        break

if __name__ == "__main__":
    asyncio.run(main())
