# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
The R^2 coeffient in my model is .86. This means that the model is strongly accurate. Predictions within the data range could be taken as close to the predicted value as the prediction equaiton is strong.

2. Is your model accurate? Why or why not?
I would say the model isnt that accurate because there are only 56 data points. Allthough that miht sound like a lot by hand, I dont think that it is that much data when we have s muhc variation in infomration. 

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles? My predictions are 9208.81 for the 10 year old car and 10184.74 for the 20 year old car.

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
The regresion line is a completely linear relationship, where as the cars get older, the cost may be a different relationship, making the cars have a seeming negative value on the prediciton line whe they stil have value in the real world. 