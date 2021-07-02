from searchplace import SearchPlace
from fillforms import FillForms

places = SearchPlace()
places.get_price()
places.get_address()
places.get_link()

forms = FillForms()
forms.fill(places.address, places.prices, places.links)
