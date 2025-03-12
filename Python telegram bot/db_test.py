



import asyncio
import asyncpg

# Database credentials
DB_HOST = "localhost"
DB_NAME = "telegram_bot"
DB_USER = "bot_user"
DB_PASS = "Ben123!!"

async def test_db_connection():
    try:
        conn = await asyncpg.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        print("✅ Database connection successful!")
        await conn.close()
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

# Run the test function
asyncio.run(test_db_connection())
