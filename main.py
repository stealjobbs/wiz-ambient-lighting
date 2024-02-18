import asyncio

from pywizlight import wizlight, PilotBuilder, discovery
import average_color as averageclr 

print("wiz light")



async def main():
    """Sample code to work with bulbs."""
    # Discover all bulbs in the network via broadcast datagram (UDP)
    # function takes the discovery object and returns a list of wizlight objects.
    
    #bulbs = await discovery.discover_lights(broadcast_space="192.168.1.255")
    # Print the IP address of the bulb on index 0
    #print(f"Bulb IP address: {bulbs[0].ip}")
    light = wizlight("192.168.1.2")
    await light.turn_on(PilotBuilder(rgb=(0, 0, 255),brightness=100))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

