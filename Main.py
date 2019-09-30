import Recommend
import ReadFile
readFileObj = ReadFile.CSVtoDictConverter()
dictionaryUser = readFileObj.open("data.csv")
print(dictionaryUser)
username = input("Enter name of a user for recommend what he like.")
recommendObj = Recommend.Recommend()
recommendedList = recommendObj.recommend(username, dictionaryUser)
print(recommendedList)
