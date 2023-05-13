from src.app import App
import asyncio

if __name__ == '__main__':
    asyncio.run(App((960, 610), 'LiquiPy', 0).loop())