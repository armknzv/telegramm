import requests
import json

from config import exchanges
class APIException(Exception):
    pass
class Converter:

    @staticmethod

    def get_price (quote , base , amount):
        try:
            quote_key = exchanges[quote.lower()]
        except KeyError:
            raise APIException(f"Валюта {quote} не найдена")

        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена")

        if quote_key == base_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {quote}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')
        r = requests.get(f"https://v6.exchangerate-api.com/v6/87850a5d0e8b35c0d0c2fd4a/pair/{quote_key}/{base_key}/{amount}")
        resp =json.loads(r.content)
        new = resp['conversion_rate']* float(amount)
        new = float(round(new, 2))
        m =f'цена {amount}  {quote} в {base} = {new}'
        return m

