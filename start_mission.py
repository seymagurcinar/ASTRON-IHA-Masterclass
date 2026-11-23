import asyncio

from mavsdk.asyncio import Mavsdk, Configuration, ComponentType
from mavsdk.asyncio.plugins.action import ActionAsync
from mavsdk.asyncio.plugins.mission import MissionAsync
from mavsdk.asyncio.plugins.telemetry import TelemetryAsync


async def main():
    mavsdk = Mavsdk(
        Configuration.create_with_component_type(
            ComponentType.GROUND_STATION
        )
    )

    await mavsdk.add_any_connection("udpin://0.0.0.0:14540")

    print("PX4 bağlantısı bekleniyor...")

    drone = await mavsdk.first_autopilot(10.0)

    if drone is None:
        print("PX4 bağlantısı kurulamadı!")
        return

    print("PX4 bağlantısı başarılı!")

    action = ActionAsync(drone)
    mission = MissionAsync(drone)
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
            break

    print("Kontroller başarılı!")

    print("Araç arm ediliyor...")
    await action.arm()
    print("Araç arm edildi!")

    print("Yüklenmiş mission başlatılıyor...")
    await mission.start_mission()
    print("Mission başlatıldı!")

    async for progress in mission.subscribe_mission_progress():
        print(
            f"Mission ilerlemesi: "
            f"{progress.current}/{progress.total}"
        )

        if progress.total > 0 and progress.current >= progress.total:
            print("Mission tamamlandı!")
            break


if __name__ == "__main__":
    asyncio.run(main())
