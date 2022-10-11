"""
Constants used in the RESTful countries api tests.
"""

BASE_URL = "https://restcountries.com/v3.1"
ALL_COUNTRIES = f"{BASE_URL}/all"
BY_NAME = f"{BASE_URL}/name"
BY_FULL_NAME = "?fullText=true"

# SendGETRequest.to(ALL_COUNTRIES)
# response = BodyOfTheLastResponse().answered_by(the_actor)
# countries = []
# for item in range(len(response)):
#     current_name = response[item]["name"]["common"]
#     if  current_name in country_names: 
#         currencies_list = []
#         symbols_list = []
#         try:
#             codes = list(response[item]["currencies"].keys())
#             has_currency = response[item]["currencies"].values()
#             list_len = 0
#             for key in (has_currency):
#                 code_name = codes[list_len]
#                 currencies_list.append(code_name)
#                 currency_symbol = key["symbol"]
#                 symbols_list.append(currency_symbol)
#                 list_len +=1
#             countries.append((current_name, currencies_list, symbols_list))
#         except KeyError:
#             pass
#     else:
#         pass

countries = [
    ('Tuvalu', ['AUD', 'TVD'], ['$', '$']),
    ('Lebanon', ['LBP'], ['ل.ل']),
    ('Burkina Faso', ['XOF'], ['Fr']),
    ('British Virgin Islands', ['USD'], ['$']),
    ('El Salvador', ['USD'], ['$']),
    ('Timor-Leste', ['USD'], ['$']),
    ('Italy', ['EUR'], ['€']),
    ('Palestine', ['EGP', 'ILS', 'JOD'], ['E£', '₪', 'JD']),
    ('Guam', ['USD'], ['$']),
    ('Faroe Islands', ['DKK', 'FOK'], ['kr', 'kr']),
    ('Afghanistan', ['AFN'], ['؋']),
    ('São Tomé and Príncipe', ['STN'], ['Db']),
    ('China', ['CNY'], ['¥']),
    ('Panama', ['PAB', 'USD'], ['B/.', '$']),
    ('Venezuela', ['VES'], ['Bs.S.']),
    ('Micronesia', ['USD'], ['$']),
    ('French Southern and Antarctic Lands', ['EUR'], ['€']),
    ('Finland', ['EUR'], ['€']),
    ('Colombia', ['COP'], ['$']),
    ('Bhutan', ['BTN', 'INR'], ['Nu.', '₹']),
    ('Jersey', ['GBP', 'JEP'], ['£', '£']),
    ('Mexico', ['MXN'], ['$']),
    ('Denmark', ['DKK'], ['kr']),
    ('Isle of Man', ['GBP', 'IMP'], ['£', '£'])
]
