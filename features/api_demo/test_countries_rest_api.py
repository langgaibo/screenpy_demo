"""
Tests derived from Boris J's tutorial on dealing with complex JSON dicts found here:
https://towardsdatascience.com/how-do-i-extract-nested-data-in-python-4e7bed37566a
"""

import pytest

from screenpy import Actor, given, then, when
from screenpy.actions import Pause, See, SeeAllOf
from screenpy.pacing import the_narrator
from screenpy.resolutions import Equals, IsEqualTo, ContainsTheItem
from screenpy_requests.actions import SendGETRequest
from screenpy_requests.questions import BodyOfTheLastResponse

from test_data.rest_countries_constants import (
    ALL_COUNTRIES,
    BY_NAME,
    countries,
    BY_FULL_NAME,
)

# who's that Qatarmon?
def test_qatar_ltd_field(Arlong: Actor) -> None:
    """It's uh"""
    target_value = "قطر."
    given(Arlong).was_able_to(SendGETRequest.to(f"{BY_NAME}/Qatar/{BY_FULL_NAME}"))
    with the_narrator.off_the_air():
        response = BodyOfTheLastResponse().answered_by(Arlong).pop()
    target_field = response["tld"][1]
    then(Arlong).should(
        See.the(target_field, Equals(target_value))
    )

# can you bike between these countries?
def test_how_many_netherlands(Arlong: Actor) -> None:
    """searching for Netherlands should return 2 countries."""
    given(Arlong).was_able_to(SendGETRequest.to(f"{BY_NAME}/Netherlands"))
    with the_narrator.off_the_air():
        response = BodyOfTheLastResponse().answered_by(Arlong)
    
    nether_lands = []
    for item in range(len(response)):
        nether_lands.append(response[item]["name"]["official"])

    then(Arlong).should(
        See.the(len(nether_lands), Equals(2)),
        See.the(nether_lands, ContainsTheItem("Bonaire, Sint Eustatius and Saba")),
    )


# Is America among the countries recognized by the UN?
def test_is_america_recognized(Arlong: Actor) -> None:
    """Has the empire fallen?"""
    given(Arlong).was_able_to(SendGETRequest.to(ALL_COUNTRIES))
    with the_narrator.off_the_air():
        response = BodyOfTheLastResponse().answered_by(Arlong)
    
    un_members = []
    for country in range(len(response)):
        if response[country]["unMember"]:
            un_members.append(response[country]["name"]["common"])
        else:
            pass
    
    then(Arlong).should(
        See.the(un_members, ContainsTheItem("United States"))
    )

# use parametrize to pit one test function against multiple inputs and assertions
@pytest.mark.parametrize("country_name,codes,symbols", countries)
def test_currency_codes(Arlong: Actor, country_name, codes, symbols) -> None:
    """ensure each country's currency matches the code on file"""
    given(Arlong).was_able_to(
        SendGETRequest.to(f"{BY_NAME}/{country_name}{BY_FULL_NAME}"),
    )
    with the_narrator.off_the_air():
        response = BodyOfTheLastResponse().answered_by(Arlong).pop()
    when(Arlong).attempts_to(
        Pause.for_(1).second_because("we don't want to spam the API.")
    )
    currency_keys = list(response["currencies"].keys())
    currency_values = response["currencies"].values()
    response_symbols = []
    for key in (currency_values):
        currency_symbol = key["symbol"]
        response_symbols.append(currency_symbol)
    

    then(Arlong).should(
        See.the(currency_keys, IsEqualTo(codes)),
        See.the(response_symbols, IsEqualTo(symbols))
    )

# actually, building the params for the prior test was a much bigger flex
def test_build_currency_param_list(Arlong: Actor) -> None:
    """We go way out of our way here to do something stupidly complex. The point is to
    deal with a lot of bullshit traversing in a big nasty dict."""

    country_names = [
        'Tuvalu', 'Lebanon', 'Burkina Faso', 'British Virgin Islands', 'El Salvador',
        'Timor-Leste', 'Italy', 'Palestine', 'Guam', 'Faroe Islands', 'Afghanistan',
        'São Tomé and Príncipe', 'China', 'Panama', 'Venezuela', 'Micronesia',
        'French Southern and Antarctic Lands', 'Finland', 'Colombia', 'Bhutan',
        'Jersey', 'Mexico', 'Denmark', 'Isle of Man'
    ]

    given(Arlong).was_able_to(SendGETRequest.to(ALL_COUNTRIES))
    with the_narrator.off_the_air():
        response = BodyOfTheLastResponse().answered_by(Arlong)

    fuckers_trick = []
    for item in range(len(response)):
        current_name = response[item]["name"]["common"]
        if  current_name in country_names: 
            currencies_list = []
            symbols_list = []
            try:
                codes = list(response[item]["currencies"].keys())
                has_currency = response[item]["currencies"].values()
                list_len = 0
                for key in (has_currency):
                    code_name = codes[list_len]
                    currencies_list.append(code_name)
                    currency_symbol = key["symbol"]
                    symbols_list.append(currency_symbol)
                    list_len +=1
                fuckers_trick.append((current_name, currencies_list, symbols_list))
            except KeyError:
                pass
        else:
            pass
    then(Arlong).should(
        SeeAllOf(
            (fuckers_trick, ContainsTheItem(('Guam', ['USD'], ['$']))),
            (fuckers_trick, ContainsTheItem(('Palestine', ['EGP', 'ILS', 'JOD'], ['E£', '₪', 'JD']))),
            (fuckers_trick, ContainsTheItem(('Bhutan', ['BTN', 'INR'], ['Nu.', '₹']))),
        )
    )
