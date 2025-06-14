from playwright.sync_api import sync_playwright

def crawl_shop_products(shop_id):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        url = f"https://haohuo.jinritemai.com/views/shop/index?id={shop_id}"
        page.goto(url, timeout=20000)
        page.wait_for_timeout(3000)  # Đợi trang tải

        html = page.content()
        browser.close()

        return {
            "shop_id": shop_id,
            "html": html[:1000] + "..."  # Cắt ngắn nội dung cho nhẹ
        }
