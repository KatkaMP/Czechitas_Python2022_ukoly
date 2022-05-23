import pandas

teplota_seznam = pandas.read_csv("seznam_1.csv",",")
# print(templota_seznam)

print(teplota_seznam[teplota_seznam["City"].isin(["Prague"])])
print(teplota_seznam[teplota_seznam["AvgTemperature"] > 80])
print(teplota_seznam[(teplota_seznam["AvgTemperature"] > 60) & (teplota_seznam["Region"].isin(["Europe"]))])
print(teplota_seznam[(teplota_seznam["AvgTemperature"] > 80)|(teplota_seznam["AvgTemperature"] < -20)])
