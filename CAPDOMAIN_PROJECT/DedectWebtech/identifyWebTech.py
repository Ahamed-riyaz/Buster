from main import URL
import webtech ,builtwith
from Wappalyzer import Wappalyzer,WebPage
import json

print(URL)
# scan a single website
class TechnologyAnalyzer():

    def __init__(self,URL):
        self.URL=URL
        print(self.URL)
    def usingWebTech(self):

        wt = webtech.WebTech(options={'json': True})
        print("\nUsing WebTech.......................")
        try:
          report = wt.start_from_url(self.URL)
          report=json.dumps(report, indent=4)                   #convert json formate.
          report = json.loads(report)
          length = len(report)
          report = json.dumps(report, indent=4)
          print(f"Length of the json: {length}")
          return report

        except webtech.utils.ConnectionException:
          return "Connection error"

    def usingWapplyzer(self):

      print("\nUsing Wapplyzer..........................")
      try:
          wappalyzer = Wappalyzer.latest()
          webpage = WebPage.new_from_url(self.URL)
          report =  wappalyzer.analyze_with_categories(webpage)
          report = json.dumps(report, indent=4)
          report =json.loads(report)
          length = len(report)
          report = json.dumps(report, indent=4)
          print(f"Length of the json: {length}")
          return report
      except :
          return "Connection error"

    def usingbuilt(self):

        print("\nUsing Built..................")
        try:
            report=builtwith.parse(self.URL)
            report = json.dumps(report, indent=4)
            report = json.loads(report)
            length = len(report)
            report = json.dumps(report, indent=4)
            print(f"Length of the json: {length}")
            return report

        except:
            return "Connection error"


def tech():
    chooseProtocol =["https://","http://"]
    choice=int(input("Choose the protocol https(1) or http(2): "))
    TechAnalyz=TechnologyAnalyzer(chooseProtocol[choice -1]+URL)
    print("\n"+TechAnalyz.usingWebTech())
    print("\n"+TechAnalyz.usingWapplyzer())
    print("\n"+TechAnalyz.usingbuilt())

tech()
