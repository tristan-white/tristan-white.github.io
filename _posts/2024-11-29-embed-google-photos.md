---
title: How to Embed Google Photos in a Website
description: Free image hosting!
image: https://lh3.googleusercontent.com/pw/AP1GczMCiRJmXjcSJuLDsbjfGXjq0uCELeFYvK80khmmEHYlm_TJ7Ehthbv5U2xQ1UI75Tody0zTCAEYizetStVgiZH9Kr6J6moJxz8sczE6k8LDJLeYC8_L=w800
tags: [website]
---


It's easy to share google photos with others, but it's not simple to embed them in blogs or personal websites.

The website [labnol.org has a tool](https://www.labnol.org/embed/google/photos/) that allows you to easily embed google photos, but in my experiene it occasionally doesn't work. Additionally, sometimes you have to complete google captchas that can be pretty time consuming if you're trying to generate embed links for lots of photos.

An alternative to using the tool on labnol.org is to run code locally that does the same thing. The labnol.org tool works by using a the [puppeteer](https://pptr.dev/) library to open the share link google photos gives you when you hit the share button, then parsing that webpage and returning a link from an HTML `meta` tag on that page.

To do this locally, you need to download `nodejs`, install `puppeteer`, and paste some javascript into a file.

[nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating) is the "Node[JS] Version Manager". Install it like so:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```

You may need to close then reopen your terminal after installing `nvm`. Next, create a new directory. In that directory, install `puppeteer`.

```bash
node install puppeteer
```

Now, create a new file called `script.js` and add the following code:

```javascript
const puppeteer = require('puppeteer');

(async () => {
    // Launch a new browser instance
    const browser = await puppeteer.launch();
    
    // Open a new page
    const page = await browser.newPage();
    
    // Navigate to a website
    const share_link = process.argv[2]; // Get link from command line
    await page.goto(share_link);

    // Extract all meta tags from the page
    const tag = await page.evaluate(() => {
        const metaNodeList = document.querySelectorAll('head meta');
        const metaArray = Array.from(metaNodeList).map(meta => meta.outerHTML); // Convert NodeList to array and get outerHTML
        return metaArray[16];
    });

    const re = /(https.*)(=w)/;
    const match = tag.match(re);
    if (match) {
        embed_link = match[0]; // The captured URL
        console.log(embed_link + "2400");
    } else {
        console.log('No match found.');
    }

    await browser.close();
})();
```

Finally, get the share link from your google photo by clicking on your photo in google photos and hitting **Share > Create Link**. Add that link as a command line argument to the script we just created. Run it and enjoy the generated embed link.

```bash
node script.js https://photos.app.goo.gl/5w3mZ4PX1NfYNnmi8

# Output:
# https://lh3.googleusercontent.com/pw/AP1GczMCiRJmXjcSJuLDsbjfGXjq0uCELeFYvK80khmmEHYlm_TJ7Ehthbv5U2xQ1UI75Tody0zTCAEYizetStVgiZH9Kr6J6moJxz8sczE6k8LDJLeYC8_L=w2400
```
> Fun Fact: I took this photo on Thanksgiving in Spain while studying abroad in València. I submitted it to a random travel blog that was having a "scholarship photo contest" for anyone in college. Nine months later I was contacted and told I had won, and received $500.
{: .prompt-tip}