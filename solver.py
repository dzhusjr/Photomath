import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.geogebra.org/solver?i=x%5E(3%20)%2B7x%5E(2)-8x')
    await page.waitForSelector('#ggw > div > div > table > tbody > tr:nth-child(4) > td > table')
    solution = await page.evaluate('() => document.querySelector("#ggw > div > div > table > tbody > tr:nth-child(4) > td > table").textContent')
    print(solution.replace("Show Steps","\n"))
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())