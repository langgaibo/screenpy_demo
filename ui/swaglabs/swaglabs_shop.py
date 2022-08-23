"""
Elements on the Swaglabs Storefront
"""

from screenpy_selenium import Target

PRODUCTS_HEADER = Target.the('"PRODUCTS" header').located_by(
    '//span[contains(text(), "Products")]'
)
URL = "https://www.saucedemo.com/inventory.html"
