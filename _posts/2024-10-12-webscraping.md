---
title: Webscraping
image: https://images.unsplash.com/photo-1489389944381-3471b5b30f04?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
tags: [data science, web scraping, travel hacking]
---

I've been wanting to learn how to get better at webscraping and javascript so today I wanted try to write a program to webscrape in javascript.

My goal was to do a simple thing: given a start location and date and end location and date, retrieve details (price, departure time, arrival time, duration of flight, airline, etc) about available flights for that date.

It wasn't as hard as I thought it would be. In this example, I scraped kayak.com for flights from Washington DC to Los Angeles, dearting on 2024-11-12 and returning on 2024-11-19. [^1]

## Code

```javascript
import puppeteer from "puppeteer";

async function get_flights(start, end, from, to) {
    const url = `https://www.kayak.com/flights/${start}-${end}/${from}/${to}?sort=bestflight_a`;
    const browser = await puppeteer.launch({
        headless: false,
        defaultViewport: null,
    });
    const page = await browser.newPage();
    await page.goto(url, {
        waitUntil: "domcontentloaded",
    });

    const filght_info = await page.evaluate(() => {
        let ret = [];
        document.querySelectorAll(".nrc6").forEach(trip => {
            let cur_trip = {};
            cur_trip.legs = [];
            trip.querySelectorAll(".hJSA-item").forEach(leg => {
                try {
                    const airline = leg.querySelector(".c_cgF").innerText;
                    const times = leg.querySelector(".VY2U").querySelectorAll("span");
                    const departure_time = times[0].innerText;
                    const arrival_time = times[2].innerText;
                    const airports = leg.querySelectorAll(".jLhY-airport-info");
                    const from_airport = airports[0].innerText;
                    const to_airport = airports[1].innerText;
                    const duration = leg.querySelector(".xdW8").querySelector(".vmXl").innerText;
                    cur_trip.legs.push({
                        airline: airline,
                        departure_time: departure_time,
                        arrival_time: arrival_time,
                        from_airport: from_airport,
                        to_airport: to_airport,
                        duration: duration,
                    });
                } catch (error) {
                    console.error("Error processing leg: ", error);
                }
            });
            ret.push(cur_trip);
        });
        return ret;
    });
    await browser.close();
    return filght_info;
}

const flights = await get_flights("WAS", "LAX", "2024-11-12", "2024-11-19");
console.log(JSON.stringify(flights));
```

## Output
```json
[
  {
    "legs": [
      {
        "airline": "Spirit Airlines",
        "departure_time": "6:30 am",
        "arrival_time": "9:27 am",
        "from_airport": "BWI",
        "to_airport": "LAX",
        "duration": "5h 57m"
      },
      {
        "airline": "Spirit Airlines",
        "departure_time": "12:55 am",
        "arrival_time": "8:43 am",
        "from_airport": "LAX",
        "to_airport": "BWI",
        "duration": "4h 48m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "Spirit Airlines",
        "departure_time": "6:30 am",
        "arrival_time": "9:27 am",
        "from_airport": "BWI",
        "to_airport": "LAX",
        "duration": "5h 57m"
      },
      {
        "airline": "Spirit Airlines",
        "departure_time": "12:55 am",
        "arrival_time": "8:43 am",
        "from_airport": "LAX",
        "to_airport": "BWI",
        "duration": "4h 48m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "Alaska Airlines",
        "departure_time": "5:28 pm",
        "arrival_time": "8:10 pm",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 42m"
      },
      {
        "airline": "Spirit Airlines",
        "departure_time": "12:55 am",
        "arrival_time": "8:43 am",
        "from_airport": "LAX",
        "to_airport": "BWI",
        "duration": "4h 48m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "United Airlines",
        "departure_time": "9:00 am",
        "arrival_time": "11:49 am",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 49m"
      },
      {
        "airline": "United Airlines",
        "departure_time": "10:45 pm",
        "arrival_time": "6:32 am+1",
        "from_airport": "LAX",
        "to_airport": "IAD",
        "duration": "4h 47m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "United Airlines",
        "departure_time": "6:00 am",
        "arrival_time": "8:49 am",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 49m"
      },
      {
        "airline": "United Airlines",
        "departure_time": "10:45 pm",
        "arrival_time": "6:32 am+1",
        "from_airport": "LAX",
        "to_airport": "IAD",
        "duration": "4h 47m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "United Airlines",
        "departure_time": "6:00 am",
        "arrival_time": "8:49 am",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 49m"
      },
      {
        "airline": "United Airlines",
        "departure_time": "11:15 pm",
        "arrival_time": "7:03 am+1",
        "from_airport": "LAX",
        "to_airport": "IAD",
        "duration": "4h 48m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "United Airlines",
        "departure_time": "9:00 am",
        "arrival_time": "11:49 am",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 49m"
      },
      {
        "airline": "United Airlines",
        "departure_time": "4:55 pm",
        "arrival_time": "12:43 am+1",
        "from_airport": "LAX",
        "to_airport": "IAD",
        "duration": "4h 48m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "United Airlines",
        "departure_time": "6:00 am",
        "arrival_time": "8:49 am",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 49m"
      },
      {
        "airline": "United Airlines",
        "departure_time": "4:55 pm",
        "arrival_time": "12:43 am+1",
        "from_airport": "LAX",
        "to_airport": "IAD",
        "duration": "4h 48m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "United Airlines",
        "departure_time": "9:00 am",
        "arrival_time": "11:49 am",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 49m"
      },
      {
        "airline": "United Airlines",
        "departure_time": "11:15 pm",
        "arrival_time": "7:03 am+1",
        "from_airport": "LAX",
        "to_airport": "IAD",
        "duration": "4h 48m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "United Airlines",
        "departure_time": "9:00 am",
        "arrival_time": "11:49 am",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 49m"
      },
      {
        "airline": "United Airlines",
        "departure_time": "9:15 pm",
        "arrival_time": "5:03 am+1",
        "from_airport": "LAX",
        "to_airport": "IAD",
        "duration": "4h 48m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "United Airlines",
        "departure_time": "6:00 am",
        "arrival_time": "8:49 am",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 49m"
      },
      {
        "airline": "United Airlines",
        "departure_time": "9:15 pm",
        "arrival_time": "5:03 am+1",
        "from_airport": "LAX",
        "to_airport": "IAD",
        "duration": "4h 48m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "United Airlines",
        "departure_time": "10:10 pm",
        "arrival_time": "12:59 am+1",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 49m"
      },
      {
        "airline": "United Airlines",
        "departure_time": "4:55 pm",
        "arrival_time": "12:43 am+1",
        "from_airport": "LAX",
        "to_airport": "IAD",
        "duration": "4h 48m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "United Airlines",
        "departure_time": "7:05 pm",
        "arrival_time": "9:55 pm",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 50m"
      },
      {
        "airline": "United Airlines",
        "departure_time": "10:45 pm",
        "arrival_time": "6:32 am+1",
        "from_airport": "LAX",
        "to_airport": "IAD",
        "duration": "4h 47m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "United Airlines",
        "departure_time": "8:15 am",
        "arrival_time": "11:05 am",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 50m"
      },
      {
        "airline": "United Airlines",
        "departure_time": "10:45 pm",
        "arrival_time": "6:32 am+1",
        "from_airport": "LAX",
        "to_airport": "IAD",
        "duration": "4h 47m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "United Airlines",
        "departure_time": "7:05 pm",
        "arrival_time": "9:55 pm",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 50m"
      },
      {
        "airline": "United Airlines",
        "departure_time": "9:15 pm",
        "arrival_time": "5:03 am+1",
        "from_airport": "LAX",
        "to_airport": "IAD",
        "duration": "4h 48m"
      }
    ]
  },
  {
    "legs": [
      {
        "airline": "United Airlines",
        "departure_time": "7:05 pm",
        "arrival_time": "9:55 pm",
        "from_airport": "IAD",
        "to_airport": "LAX",
        "duration": "5h 50m"
      },
      {
        "airline": "United Airlines",
        "departure_time": "11:15 pm",
        "arrival_time": "7:03 am+1",
        "from_airport": "LAX",
        "to_airport": "IAD",
        "duration": "4h 48m"
      }
    ]
  }
]
```

---

[^1]: This [article](https://www.freecodecamp.org/news/web-scraping-in-javascript-with-puppeteer/) was a helpful guide.