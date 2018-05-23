
***

## enhanced-stock-option
A simple stock-option-viewer for quick referencing option price at a certain time.
***
We can all go to the website of Charles-Schwab, Interactive Broker, TD Ameritrade, Merrill-Edge or any broker from any bank to get the option price. Robinhood even has its own option table. However, these tools show us the information, not what we really need: loss and profit at a given price. What if we need it on the go and be able to calculate the loss/profit percentage with a few clicks?

This program is intended to:

 - Get stock ticker and retrieve a JSON object of available options.
 - Put it in a CSV file so I can further manipulate it (add functions, charts, calculate loss/profit)
 - The file NXPI.xlsx a template of final result.

***
I chose Python because at this point, data science is a booming field and Python happens to be the language of choice for non-programmer data scientists. It means there are a lot of libraries to crunch numbers and convert it into csv, xlsx and to analyze the data. 

Note: 

 - Yahoo may end support for this link at any time, so this might not work in the future.
 - The Yahoo links behaves strangely during weekend and does not show all available options. This might be because maintenance is being performed. Therefore, the program is unreliable during weekends.
***



