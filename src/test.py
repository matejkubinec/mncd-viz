import unittest
from test import EdgeListParserTests

suite = unittest.TestLoader().loadTestsFromTestCase(EdgeListParserTests)
unittest.TextTestRunner(verbosity=2).run(suite)

# import requests

# BASE_URL = "http://127.0.0.1:5000"

# #
# # BARPLOT
# #
# data_barplot = [1, 2, 3]
# data = {
#     "X": data_barplot,
#     "Y": data_barplot,
#     "labels": data_barplot,
#     "xlabel": "X Data",
#     "ylabel": "Y Data"
# }
# print(data)
# r = requests.post(BASE_URL + "/api/common-charts/barplot", json=data)

# assert r.status_code == requests.codes.ok
# assert r.headers["Content-Type"] == "image/svg+xml; charset=utf-8"

# #
# # TREEMAP
# #
# data_barplot = [1, 2, 3]
# data = {
#     "sizes": data_barplot,
#     "label": data_barplot,
# }
# r = requests.post(BASE_URL + "/api/common-charts/treemap", json=data)

# assert r.status_code == requests.codes.ok
# assert r.headers["Content-Type"] == "image/svg+xml; charset=utf-8"
