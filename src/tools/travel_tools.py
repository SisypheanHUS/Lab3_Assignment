"""
Travel-related tools for the ReAct Agent.
These mock tools simulate real APIs for demonstration purposes.
"""

from typing import Dict, Any
from .base import BaseTool


class GoogleSearchTool(BaseTool):
    """Simulates Google search for tourist destinations."""

    # Mock database of Vietnam tourist attractions
    ATTRACTIONS_DB = {
        "ha noi": {
            "name": "Hà Nội",
            "attractions": [
                "Old Quarter (Phố Cổ)",
                "Hoan Kiem Lake (Hồ Hoàn Kiếm)",
                "Temple of Literature (Văn Miếu)",
                "Ho Chi Minh Mausoleum"
            ],
            "avg_temp_celsius": 26,
            "best_season": "October - April",
            "avg_hotel_price_usd": 50
        },
        "ho chi minh": {
            "name": "Thành Phố Hồ Chí Minh",
            "attractions": [
                "Saigon River",
                "War Remnants Museum",
                "Ben Thanh Market",
                "Reunification Palace"
            ],
            "avg_temp_celsius": 28,
            "best_season": "November - April",
            "avg_hotel_price_usd": 60
        },
        "da nang": {
            "name": "Đà Nẵng",
            "attractions": [
                "My Khe Beach",
                "Marble Mountains",
                "Dragon Bridge",
                "Hoi An Ancient Town (nearby)"
            ],
            "avg_temp_celsius": 27,
            "best_season": "May - September",
            "avg_hotel_price_usd": 45
        },
        "hoi an": {
            "name": "Hội An",
            "attractions": [
                "Ancient Town",
                "Lantern Light Festival",
                "An Bang Beach",
                "Cua Dai Beach"
            ],
            "avg_temp_celsius": 27,
            "best_season": "October - April",
            "avg_hotel_price_usd": 40
        },
        "sapa": {
            "name": "Sa Pa",
            "attractions": [
                "Fansipan Peak (Mount Fansipan)",
                "Muong Hoa Valley",
                "Silver Waterfall",
                "Local hill tribe villages"
            ],
            "avg_temp_celsius": 15,
            "best_season": "October - November, April - May",
            "avg_hotel_price_usd": 35
        }
    }

    def __init__(self):
        super().__init__(
            name="google_search",
            description="Search for information about tourist destinations and attractions in Vietnam. "
                       "Input: destination name (e.g., 'Ha Noi', 'Ho Chi Minh', 'Da Nang', 'Hoi An', 'Sa Pa'). "
                       "Returns: attractions, best season, and average hotel prices."
        )

    def run(self, location: str) -> str:
        """Search for attractions in a given location."""
        location_lower = location.lower().strip()
        
        if location_lower in self.ATTRACTIONS_DB:
            info = self.ATTRACTIONS_DB[location_lower]
            result = f"📍 {info['name']}\n"
            result += f"Attractions: {', '.join(info['attractions'])}\n"
            result += f"Average Temperature: {info['avg_temp_celsius']}°C\n"
            result += f"Best Season: {info['best_season']}\n"
            result += f"Average Hotel Price: ${info['avg_hotel_price_usd']}/night\n"
            return result
        else:
            return f"Location '{location}' not found in database. Available locations: " \
                   f"{', '.join([loc.title() for loc in self.ATTRACTIONS_DB.keys()])}"


class WeatherAPITool(BaseTool):
    """Simulates a weather API for checking current conditions."""

    WEATHER_DB = {
        "ha noi": {
            "condition": "Partly Cloudy",
            "temp_c": 26,
            "humidity": 65,
            "rain_chance": 30
        },
        "ho chi minh": {
            "condition": "Sunny",
            "temp_c": 32,
            "humidity": 70,
            "rain_chance": 20
        },
        "da nang": {
            "condition": "Cloudy",
            "temp_c": 28,
            "humidity": 75,
            "rain_chance": 40
        },
        "hoi an": {
            "condition": "Sunny",
            "temp_c": 27,
            "humidity": 68,
            "rain_chance": 25
        },
        "sapa": {
            "condition": "Misty",
            "temp_c": 16,
            "humidity": 85,
            "rain_chance": 50
        }
    }

    def __init__(self):
        super().__init__(
            name="weather_api",
            description="Check current weather conditions for a tourist destination. "
                       "Input: destination name (e.g., 'Ha Noi', 'Ho Chi Minh', 'Da Nang', 'Hoi An', 'Sa Pa'). "
                       "Returns: temperature, condition, humidity, and rain probability."
        )

    def run(self, location: str) -> str:
        """Fetch weather for a given location."""
        location_lower = location.lower().strip()
        
        if location_lower in self.WEATHER_DB:
            weather = self.WEATHER_DB[location_lower]
            result = f"🌤️  Weather for {location.title()}:\n"
            result += f"Condition: {weather['condition']}\n"
            result += f"Temperature: {weather['temp_c']}°C\n"
            result += f"Humidity: {weather['humidity']}%\n"
            result += f"Rain Chance: {weather['rain_chance']}%\n"
            return result
        else:
            return f"Weather data not available for '{location}'."


class BookingAPITool(BaseTool):
    """Simulates a booking API for checking hotel availability."""

    AVAILABILITY_DB = {
        "ha noi": {
            "available_rooms": 45,
            "avg_price_usd": 50,
            "rating": 4.5,
            "hotels": [
                "Hanoi Plaza Hotel",
                "Old Quarter View Boutique",
                "Luxury Downtown"
            ]
        },
        "ho chi minh": {
            "available_rooms": 60,
            "avg_price_usd": 60,
            "rating": 4.3,
            "hotels": [
                "Saigon Pearl Hotel",
                "Downtown Riverside Resort",
                "City Center Luxury"
            ]
        },
        "da nang": {
            "available_rooms": 35,
            "avg_price_usd": 45,
            "rating": 4.6,
            "hotels": [
                "Beach Resort & Spa",
                "Marble Mountain View",
                "Coastal Luxury"
            ]
        },
        "hoi an": {
            "available_rooms": 25,
            "avg_price_usd": 40,
            "rating": 4.7,
            "hotels": [
                "Ancient Town Boutique",
                "Lantern Hotel",
                "Riverside Paradise"
            ]
        },
        "sapa": {
            "available_rooms": 15,
            "avg_price_usd": 35,
            "rating": 4.4,
            "hotels": [
                "Mountain View Lodge",
                "Valley Resort",
                "Peak Adventure Hotel"
            ]
        }
    }

    def __init__(self):
        super().__init__(
            name="booking_api",
            description="Check hotel availability and pricing for a tourist destination. "
                       "Input: destination name (e.g., 'Ha Noi', 'Ho Chi Minh', 'Da Nang', 'Hoi An', 'Sa Pa'). "
                       "Returns: available rooms, average price, rating, and list of hotels."
        )

    def run(self, location: str) -> str:
        """Fetch hotel availability for a given location."""
        location_lower = location.lower().strip()
        
        if location_lower in self.AVAILABILITY_DB:
            availability = self.AVAILABILITY_DB[location_lower]
            result = f"🏨 Hotel Availability for {location.title()}:\n"
            result += f"Available Rooms: {availability['available_rooms']}\n"
            result += f"Average Price: ${availability['avg_price_usd']}/night\n"
            result += f"Average Rating: {availability['rating']}/5.0\n"
            result += f"Featured Hotels: {', '.join(availability['hotels'][:2])}\n"
            return result
        else:
            return f"Booking data not available for '{location}'."
