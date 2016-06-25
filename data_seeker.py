import requests, zipfile, StringIO

zip_file_url = "http://eco2mix.rte-france.com/download/eco2mix/eCO2mix_RTE_En-cours-TR.zip"


r = requests.get(zip_file_url, stream=True)
z = zipfile.ZipFile(StringIO.StringIO(r.content))
z.extractall()

