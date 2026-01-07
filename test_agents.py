"""
Test script to verify the 4-agent system works correctly
Tests forecast generation without actually sending to Telegram
"""

import asyncio
from datetime import datetime, timedelta
from agents.agent_1_data_collector import DataCollectorAgent
from agents.agent_2_metaphysical import MetaphysicalAnalystAgent
from agents.agent_3_dev_strategist import DevStrategistAgent
from agents.agent_4_telegram_notifier import TelegramNotifierAgent
from config.settings import settings
from core.lunar_calendar import get_vietnam_datetime


async def test_forecast(target_date: datetime):
    """Test the 4-agent chain"""
    print("=" * 80)
    print(f"TESTING FORECAST FOR: {target_date.strftime('%d/%m/%Y')}")
    print("=" * 80)
    
    # Initialize agents
    agent1 = DataCollectorAgent(
        user_birth_day=settings.USER_BIRTH_DAY,
        user_birth_month=settings.USER_BIRTH_MONTH
    )
    
    agent2 = MetaphysicalAnalystAgent(
        user_element=settings.USER_ELEMENT,
        user_branch=settings.USER_BRANCH,
        user_life_path=settings.get_life_path_number()
    )
    
    agent3 = DevStrategistAgent()
    agent4 = TelegramNotifierAgent()
    
    # Run the chain
    print("\n🔍 AGENT 1: Data Collector")
    print("-" * 80)
    data_result = agent1.analyze(target_date)
    print(agent1.get_summary(data_result))
    
    print("\n🔮 AGENT 2: Metaphysical Analyst")
    print("-" * 80)
    meta_result = agent2.analyze(data_result)
    print(agent2.get_summary(meta_result))
    
    print("\n💻 AGENT 3: Dev Strategist")
    print("-" * 80)
    dev_result = agent3.analyze(data_result, meta_result)
    print(agent3.get_summary(dev_result))
    
    print("\n📱 AGENT 4: Telegram Notifier")
    print("-" * 80)
    telegram_result = agent4.analyze(data_result, meta_result, dev_result)
    
    print("\n" + "=" * 80)
    print("FINAL TELEGRAM MESSAGE:")
    print("=" * 80)
    print(telegram_result["message"])
    print("=" * 80)
    
    return telegram_result


async def main():
    """Main test function"""
    print("\n🔮 Thiên Cơ Đại Tướng Quân - Test Suite\n")
    
    # Test 1: Tomorrow
    print("\n📅 TEST 1: Forecast for TOMORROW")
    now = get_vietnam_datetime()
    tomorrow = now + timedelta(days=1)
    await test_forecast(tomorrow)
    
    # Test 2: Specific date
    print("\n\n📅 TEST 2: Forecast for 08/01/2026")
    test_date = datetime(2026, 1, 8)
    await test_forecast(test_date)
    
    # Test 3: Another specific date
    print("\n\n📅 TEST 3: Forecast for 14/04/2026 (Birthday!)")
    birthday = datetime(2026, 4, 14)
    await test_forecast(birthday)
    
    print("\n\n✅ ALL TESTS COMPLETED!\n")


if __name__ == "__main__":
    asyncio.run(main())
