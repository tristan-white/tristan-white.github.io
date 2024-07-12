import plotly.express as px
import pandas as pd
from dataclasses import dataclass

@dataclass
class Card():
    name: str
    intro_bonus: int    # estimate in dollars; I use 1 cent/point
    # not necessary for the perks to be a dict instead of a list;
    # chose a dict for readibility
    annual_perks: dict

    def yearly_value(self):
        "Does not inlude intro bonus"
        return sum(self.annual_perks.values())

    def total_benefit_value(self, years: int) -> int:
        """Returns the value in dollars of holding the card for
        'years' number of years."""
        value = self.intro_bonus
        value = sum(self.annual_perks.values())
        return value * years

@dataclass
class Platinum(Card):

    """The platinum card has some perks that don't 'stack' well with 
    multiple cards. For example, Uber Cash stacks because if you three
    platinum cards, you receive 3x the amount of Uber Cash you would were
    you to only own one platinum card. However, the Walmart+ credit doesn't
    really stack because one person would probably not retain two Walmart+
    subscriptions."""
    is_first_plat: bool = False
    misc_perks = {
        "walmart_plus": 155,
        "digital_entertainment": 240,
    }

    def total_benefit_value(self, years: int) -> int:
        sum = super().total_benefit_value(years)
        for v in self.misc_perks.values():
            sum += v
        return sum

def value_to_now(cards: list[Card], years: int) -> int:
    value = 0
    for c in cards:
        value += c.total_benefit_value(years)
    return value

def get_bar_graph(cards: list[Card], years: int):
    plat_annual_perks = {
        "hotel_credit": 200,
        "uber_cash_plat": 200,
        "airline_fees": 200,
        "saks_fifth_ave": 100
    }
    # create dataframe (list of dicts)
    data = []
    plat_count = 0
    for i in range(years):
        # create 2 more platinum cards each year
        cards.append(Platinum(f"Plat{plat_count}", annual_perks=plat_annual_perks, intro_bonus=250))
        plat_count += 1
        cards.append(Platinum(f"Plat{plat_count}", annual_perks=plat_annual_perks, intro_bonus=250))
        plat_count += 1
        for c in cards:
            datum = {
                "Year": i,
                "Source": c.name,
                "Value from Card ($)": c.yearly_value(),
            }
            if i == 0:
                datum["Value from Card ($)"] += c.intro_bonus
            data.append(datum)
    df = pd.DataFrame(data)
    fig = px.bar(df, x="Year", y="Value from Card ($)", color="Source", title="Value Of Card Benefits Per Year")
    graph_path = "./cards.html"
    # fig.write_html(graph_path, include_plotlyjs="cdn")
    fig.show()

if __name__ == "__main__":

    # create object for each card
    plat_annual_perks = {
        "hotel_credit": 200,
        "uber_cash_plat": 200,
        "airline_fees": 200,
        "saks_fifth_ave": 100
    }
    plat1 = Platinum("Plat1", intro_bonus=1200, annual_perks=plat_annual_perks, is_first_plat=True)

    gold_annual_perks = {
        "uber_cash_gold": 120,
        "dining_credit": 120
    }
    gold = Card("Gold", intro_bonus=800, annual_perks=gold_annual_perks)

    reserve_annual_perks = {
        "travel_credit": 300
    }
    reserve = Card("Reserve", intro_bonus=600, annual_perks=reserve_annual_perks)

    get_bar_graph([plat1, gold, reserve], years=10)

"""
Embed in an article like this:

<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="/assets/path/to/graph.html" height="525" width="100%"></iframe>

see: https://plotly.com/python/embedding-plotly-graphs-in-HTML/
"""