import plotly.express as px
import pandas as pd
import chart_studio.tools as tls

# American Express Platinum Card
hotel_credit = 200
# digital_entertainment = 240
uber_cash_plat = 200
airline_fees = 200
saks_fifth_ave = 100
# walmart = 155
plat_sum = hotel_credit + uber_cash_plat + airline_fees + saks_fifth_ave

# American Express Gold Card
uber_cash_gold = 120
dining_credit = 120
gold_sum = uber_cash_gold + dining_credit

# Chase Sapphire Reserve
travel_credit = 300
reserve_sum = travel_credit

# Bonuses
plat_bonus = 1200
gold_bonus = 800
green_bonus = 250
plat2_bonus = 250
plat3_bonus = 500
sapphire_reserve_bonus = 900
bonus_sum = plat_bonus + gold_bonus + green_bonus + plat2_bonus + plat3_bonus + sapphire_reserve_bonus

def func(years: int):
    num_plats = years * 2
    print(f"plats: {num_plats * plat_sum}")
    return (num_plats * plat_sum) + gold_sum + reserve_sum


# create dataframe (list of dicts)
l = []
for i in range(1, 11):
    l.append(
        {
            "year": i,
            "card": "gold",
            "amt": gold_sum,
        }
    )
    l.append(
         {
            "year": i,
            "card": "reserve",
            "amt": reserve_sum,
         }
    )
    l.append(
         {
            "year": i,
            "card": "plat",
            "amt": plat_sum * i,
         }
    )
    df = pd.DataFrame(l)

fig = px.bar(df, x="year", y="amt", color="card")
graph_path = "./cards.html"
fig.write_html(graph_path, include_plotlyjs="cdn")

"""
Embed in an article like this:

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="/assets/path/to/graph.html" height="525" width="100%"></iframe>

see: https://plotly.com/python/embedding-plotly-graphs-in-HTML/
"""