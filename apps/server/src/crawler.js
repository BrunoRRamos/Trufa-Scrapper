import puppeteer from "puppeteer";
import path from "path";
import fs from "fs";

const config = { headless: true, setTimeout: 10000 };
const dirPath = path.join(process.cwd(), "results");
const filePath = path.join(dirPath, "scraped.txt");

const browser = await puppeteer.launch(config);
const page = await browser.newPage();

// Navigate the page to a URL.
await page.goto(
  "https://www.thekingofparfums.com.br/?gad_source=1&gclid=Cj0KCQiAhvK8BhDfARIsABsPy4itE30QWUsiKaopB4IOkOkP4pmxrbjoikc5JbPfxvmYxX1xIhDl1EgaAp16EALw_wcB"
);

const pages = await page.$$eval("a", (anchors) => {
  return anchors.map((a) => a.href);
});

browser.close();

const regex = /\/lacrado\//;
const dataSet = new Set(pages.filter((link) => regex.test(link)));

if (!fs.existsSync(dirPath)) {
  fs.mkdirSync(dirPath, { recursive: true });
}

dataSet.forEach((link) => {
  fs.writeFile(filePath, link + "\n", { flag: "a" }, (err) => {});
});
