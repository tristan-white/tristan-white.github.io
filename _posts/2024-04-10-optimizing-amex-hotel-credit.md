---
layout: post
title: Travel Hacking with Network and Data Analysis
description: Finding $$$ deals with Python.
image: https://images.unsplash.com/photo-1502920514313-52581002a659?q=80&w=2067&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
tag: [travel hacking]
---
American Express likes to flaunt the fact that Platinum Card members receive a $200 hotel credit annually. It certainly is a great perk, but does it actually help you save money while traveling, or just entice you to spend more?

Let's look at exactly what this [perk](https://www.americanexpress.com/en-us/travel/benefits/how-to-use-hotel-credit/) gets you:
- $200 towards Fine Hotels + Resorts (FHR) or The Hotel Collection (THC) [^1]
- $100 experience credit [^2]
- Late checkout
- Early check-in (if available)
- Room upgrade (if available)

If you're just looking to have a luxurious stay at an opulent hotel, you won't have trouble finding a place to use this credit card perk among the hundreds of options on amextravel.com.

However, deal seekers trying to use this credit to SAVE money on a stay may feel let down when they try to cash out on this offer because:

- THC hotels require you stay two nights to use the $200 credit. Most THC hotels are already 2x or 3x what other hotels cost nightly, so if you were looking to use this perk to simply upgrade your stay when you stay out of town, you wont be able to do it at a THC hotel without paying significantly more. That leaves the Fine Hotels + Resorts...
- FHR hotels are even more expensive, normally at least $400 and nicer options over $1k. [^3]

So is it possible to use stay at one of these hotels with the perk and pay less than you would at a typical hotel?

Yes, it just takes a lot of effort - until now.

The only way to use this credit without paying an excessive amount is to find a hotel with a nightly cost that is less than $200 above the price of any hotel you'd stay at otherwise. Therefore, THC hotels are out of the picture already because they require a two night stay minimum (with each night about $300). But could you find a FHR hotel that's a low price? [^4]

Unfortunately, Amex's travel website was just not built to help you find the best deals on FHR hotels:
- you can't sort by price
- there's no feature to allow you to find the cheapest date for a particular hotel [^5]
- searching with their filters is slow (takes about 10 seconds per search)

What this means is that if you want to find the cheapest date to visit a particular hotel, there's no option except to check every single date in your range of dates. Let's trace out that method: suppose you find a cool hotel in Nashville that you want to stay at, but the hotel price is $800/night for the specific day you check. Is there a cheaper night? What's the cheapest night this summer? To answer this question, you perform about 90 searches for each night of the summer. Let's say you're able to do a search in about 10 seconds, then scan the results with your eyes and remember relevant details in another 10 seconds. This whole process would then take 90 * (10 + 10) = 1800 seconds = 30 minutes. Finally, say you found the ideal night. Only $250 per night! Oh, but you have a wedding that day...maybe you can find a deal for a different day in a different city? Back to the drawing board and performing price queries for half an hour.

I searched online for ways to find the best deals, but I couldn't find any. Which got me thinking...why can't I just get the data I need and analyze it myself?

After I did a search on amextravel.com, I opened the firefox debugging tools in my browser. After looking around at the individual http requests my browser was sending, I found one that received all the data I desired in JSON via an http response.

![Sreenshot of Network Traffic Analysis](https://lh3.googleusercontent.com/pw/AP1GczN2irx-v5C9qIs4_zCQcjc8sFPg_O5HJssrzL2NLFzJrGh4nImJ5-aYHps2q6nQKZ4W0Ak21g9maKdDAdrwY-5az6XYtZShOzUU-MxkP59njeUsH2KE=w2400){: w="1034" h="705"}

I examined the packet in the firefox network debugger to determine how to craft http request queries to receive responses with the specific data I wanted. Next, [I wrote a python program](https://github.com/tristan-white/fhr_deal_finder) to iterate over all the dates for which I wanted to check nightly rates. Finally, I used [plotly](https://tristanwhite.me/plotly.html) to display the data with an interactive graph. I must say, [the results are pretty cool](https://tristanwhite.me/fhr.html).

![Example FHR Deal Graph](https://lh3.googleusercontent.com/pw/AP1GczO4WIFn1e2RrbVoHoRPAUCCc3_GFiJ9PSR5RQ7YY51SUcIXWinYpHqffwAPI51nlwkfJFvuINC80PzloL5Kfj_KFmeoCtqcEe5-KnSnrz7otXBaciJG=w2400)
*An example graph output from the FHR Deal Finder program*

If you'd like to use this command line tool to find your own deals, you can grab it here:
[https://github.com/tristan-white/fhr_deal_finder](https://github.com/tristan-white/fhr_deal_finder)

Hoping this can help other travel hackers snipe some great deals. Happy travel hacking :)

> 2024-04-16 Edit: A user on reddit [shared](https://www.reddit.com/r/AmexPlatinum/comments/1c4vwfz/how_to_actually_find_the_fine_hotels_resorts_with/) that you can use [maxfhr.com](https://www.maxfhr.com/) to essentially accomplish my goal with this project. I'd reccomend that tool to anyone looking for a good FHR rate. My tool is only better for 1) seeing prices that are always up to date, and 2) see taxes and fees, which can account for about a quarter of the total price.
{: .prompt-tip}

---
[^1]: The big asterisk for THC hotels is that you must stay at least two nights to use the $200 credit.
[^2]: From what I've seen, the vast majority of hotels give you $100 to use on the premises (at the bar, restaurant, spa, etc). However, occasionally a hotel will give you an experience instead of money.
[^3]: In fact the most expensive room I've found while playing around with the program I built in this article was the [Montage Palmetto Bluff](https://www.montage.com/palmettobluff/) hotel for $5865 the night of May 2nd (price current as of 2024-04-13). And that's before the $889 tax.
[^4]: There **are** FHR hotels as low as about $250, you just have to look hard for them. Or at least you did, before I wrote the program in this article.
[^5]: Recently I was able to find sort by price filter, but it only sorts from high to low, with the lowest priced FHR hotels on a different page that takes more time to load 🙄