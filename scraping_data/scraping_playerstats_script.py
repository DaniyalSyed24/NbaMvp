## python script to scrape player list + stats for each year


from playwright.sync_api import sync_playwright

years = list(range(1981,2023))

url_start = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"

for year in years:
  url = url_start.format(year)
  
  with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    data = page.inner_html("*")
    with open("players/{}.html".format(year), "w+", encoding='utf-8') as f:
      f.write(data)
    browser.close()