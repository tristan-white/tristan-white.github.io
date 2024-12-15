---
title: Javascript
description: An inevitable meeting.
image: https://www.infoworld.com/wp-content/uploads/2024/06/shutterstock_1361674454-100939444-orig.jpg?resize=1024%2C684&quality=50&strip=all
layout: post
tags: [coding]
---

I've managed to stay away from javascript trhoughout a whole computer science degree and two years as a software engineer but every once in a while something pops up that requires it and I'll wish I was more familiar with it. So I went and learned a bit of JS today.

To practice, I made a calculator to (roughly) calculate the annual salary of military members after taxes.

<input type="number" id="bah" placeholder="Monthly BAH"/><br>
<input type="number" id="base_pay" placeholder="Monthy Base Pay"/><br>
<button id="submit">Submit</button>

<p>Salary after taxes: <strong id="result"></strong></p>

<script>
    const rates = [0, 0.1, 0.12, 0.22, 0.32, 0.35, 0.37];
    const brackets = [0, 11600, 47150, 100525, 191950, 243726, 609351];

    document.getElementById("submit").addEventListener("click", function() {
        
        const bah = parseFloat(document.getElementById("bah").value);
        const annual_bah = bah * 12;

        const base_pay = parseFloat(document.getElementById("base_pay").value);
        const annual_base = base_pay * 12;

        const bas = 316 * 12;

        let tax = 0;
        for (let i = 0; i < brackets.length; i++) {
            if (i === 0) continue;
            if (brackets[i] < annual_base) {
                tax += (brackets[i] - brackets[i - 1]) * rates[i];
            } else {
                tax += (annual_base - brackets[i-1]) * rates[i];
                break;
            }
        }

        document.getElementById("result").textContent = (annual_base + bas + annual_bah - tax);
    });
</script>

### The Code
```javascript
<script>
    const rates = [0, 0.1, 0.12, 0.22, 0.32, 0.35, 0.37];
    const brackets = [0, 11600, 47150, 100525, 191950, 243726, 609351];

    document.getElementById("submit").addEventListener("click", function() {
        const bah = parseFloat(document.getElementById("bah").value);
        const annual_bah = bah * 12;

        const base_pay = parseFloat(document.getElementById("base_pay").value);
        const annual_base = base_pay * 12;

        const bas = 316 * 12;

        let tax = 0;
        for (let i = 0; i < brackets.length; i++) {
            if (i === 0) continue;
            if (brackets[i] < annual_base) {
                tax += (brackets[i] - brackets[i - 1]) * rates[i];
            } else {
                tax += (annual_base - brackets[i-1]) * rates[i];
                break;
            }
        }

        document.getElementById("result").textContent = "Annual salary after taxes: " + (annual_base + bas + annual_bah - tax);
    });

</script>
```