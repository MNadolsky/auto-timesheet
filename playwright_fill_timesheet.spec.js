const { test, expect } = require('@playwright/test');

test('test', async ({ page }) => {

  test.setTimeout(0);

  const delay = ms => new Promise(resolve => setTimeout(resolve, ms))
  await delay(0);

  const username = process.env.TIMESHEET_USERNAME
  const password = process.env.TIMESHEET_PASSWORD
  const url = process.env.TIMESHEET_URL

  await page.goto(url);
  await page.locator('input[name="pf\\.username"]').click();
  await page.locator('input[name="pf\\.username"]').fill(username);
  await page.locator('input[name="pf\\.pass"]').click();
  await page.locator('input[name="pf\\.pass"]').fill(password);
  await page.locator('text=Submit').click();
  await expect(page).toHaveURL(url);

  const [page1] = await Promise.all([
    page.waitForEvent('popup'),
    page.locator('text=My Timesheet - Modern').click()
  ]);

  today = new Date()
  let date = await page1.locator('.timesheet-carousel > li:nth-of-type(2) > div > div.carousel-date').innerText();
  start = date.split('-')[0].trim() + ', ' + today.getFullYear()
  end = date.split('-')[1].trim() + ', ' + today.getFullYear()
  week_start = Date.parse(start)
  week_end = Date.parse(end)

  while (week_start > new Date()) {
    await delay(1000);
    await page1.locator('.control-left > svg').click();
    date = await page1.locator('.timesheet-carousel > li:nth-of-type(2) > div > div.carousel-date').innerText();
    start = date.split('-')[0].trim() + ', ' + today.getFullYear();
    week_start = Date.parse(start);
  }

  while (week_end < new Date()) {
    await delay(1000);
    await page1.locator('.control-right > svg').click();
    date = await page1.locator('.timesheet-carousel > li:nth-of-type(2) > div > div.carousel-date').innerText();
    end = date.split('-')[1].trim() + ', ' + today.getFullYear();
    week_end = Date.parse(end);
  }

// used for testing so dev can cycle dates to an open one    
//  await delay(10000)
    
  await page1.locator('.timesheet-carousel > li:nth-of-type(2)').click()
  let status = await page1.locator('.timesheet-carousel > li:nth-of-type(2) > div > div.status').innerText();
  if (status === 'Open') {

    await page1.locator('text=No Tasks Add tasks to work on your timesheet. Add Tasks >> [aria-label="Add Tasks"]').click();
    await page1.locator('li[role="option"]:has-text("Copy Previous Timesheet (with time)")').click();

  }

  await delay(15000)

});
