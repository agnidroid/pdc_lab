from fetch_wiki import fetch_wiki
from fetchyahoo import fetchyahoo
import time

if __name__ == "__main__":

	
	fetchFromWikiObj = fetch_wiki()
	fetchFromYahooObj = fetchyahoo()

	table = fetchFromWikiObj.getTable()

	# Sequential Execution 
	print("----- Sequential Execution -----")
	startTime = time.time()

	symbols = fetchFromWikiObj.sequential(table)
	fetchFromYahooObj.sequential(symbols)
	print("Sequential Time of Execution: ",time.time()-startTime)

	# Multithreaded Execution
	print("----- Multithreaded Execution -----")
	startTime = time.time()
	symbols = fetchFromWikiObj.multithreaded(table)
	fetchFromYahooObj.multithreaded(symbols)
	print("Multithreaded Time of Execution: ",time.time()-startTime)