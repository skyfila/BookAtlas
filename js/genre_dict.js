NYT_BESTSELLERS_URL = "https://www.nytimes.com/books/best-sellers/"

const parser = new DOMParser();
const parsed = parser.parseFromString(NYT_BESTSELLERS_URL, "text/html");

console.log(parsed.firstChild.innerText);
