
# Health-Insurance-Cross-Sell-Prediction

## Tableau
![Alt text](https://raw.githubusercontent.com/raviatkumar/Health-Insurance-Cross-Sell-Prediction/main/Image/health_tableau.PNG)

## Link:https:https://public.tableau.com/views/ravikumarHealth-Insurance-Cross-Sell-Prediction/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link


## Problem statement

Our client is an Insurance company that has provided Health Insurance to its customers now they need your help in building a model to predict whether the policyholders (customers) from the past year will also be interested in Vehicle Insurance provided by the company. An insurance policy is an arrangement by which a company undertakes to provide a guarantee of compensation for specified loss, damage, illness, or death in return for the payment of a specified premium. A premium is a sum of money that the customer needs to pay regularly to an insurance company for this guarantee.

For example, you may pay a premium of Rs. 5000 each year for a health insurance cover of Rs. 200,000/- so that if God forbid, you fall ill and need to be hospitalised in that year, the insurance provider company will bear the cost of hospitalisation, etc. for up to Rs. 200,000. Now if you are wondering how can the company bear such high hospitalisation costs when it charges a premium of only Rs. 5000/-, that is where the concept of probabilities comes into the picture. For example, like you, there may be 100 customers who would be paying a premium of Rs. 5000 every year, but only a few of them (say 2-3) would get hospitalised that year, and not everyone. This way everyone shares the risk of everyone else.

Just like medical insurance, there is vehicle insurance where every year a customer needs to pay a premium of a certain amount to the insurance provider company so that in case of an unfortunate accident by the vehicle, the insurance provider company will provide compensation (called ‘sum assured’) to the customer.

Building a model to predict whether a customer would be interested in Vehicle Insurance is extremely helpful for the company because it can then accordingly plan its communication strategy to reach out to those customers and optimise its business model and revenue.

Now, in order to predict whether the customer would be interested in Vehicle insurance, you have information about demographics (gender, age, region code type), Vehicles (Vehicle Age, Damage), Policy (Premium, sourcing channel), etc.

![image](https://user-images.githubusercontent.com/125804537/226084035-86a72bdb-a64b-4cd4-b10b-81e56acdcc41.png)

## Data Description

id: Unique ID for customer

Age: Age of the customer

Driving_License 0 : Customer has DL or not

Region_Code: Unique code for the region of the customer

Previously_Insured 1 : Customer already has Vehicle Insurance or not

Vehicle_Age: Age of the Vehicle

Vehicle_Damage 1 : Past damages present or not

Annual_Premium: The amount customer needs to pay as premium

PolicySalesChannel: Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc.

Vintage: Number of Days, Customer has been associated with the company

Response :Customer is interested or not
## A small insights from the problem statement and data description

### What is an insurance firm?

If a loss occurred a guarantee of compensation for specified loss, damage, illness, or death in return for the payment of a specified premium.

### What is the probability of buying an insurance?

In insurance industry, it refers to a situation in which people only buy insurance when they expect high risks. Buying insurance is not appropriate for all levels and types of risks. In many cases, people are better off taking actions to avoid risk, retain (accept) risk or reduce risk. Buying insurance makes the most sense when the potential loss is great and there is a significant probability of loss.

### How can an insurance firm protect its customers?

Insurance company protects people and businesses against the risk of unforeseeable events. It is a risk transfer mechanism by which the losses of the few are paid for by the many, with the premiums based on the risk of each individual or entity
How many people are knowledgeable about insurance policy and how many of them claim insurance?
Lets say about four in 10 men describe themselves as being very knowledgeable about life insurance. As in the problem statement, about 2 or 3 get hospitalized out of 100, which means 2 to 3 percent claim the insurance. This way everyone shares the risk of everyone else.

So we need to building a model to predict whether a customer would be interested in Vehicle Insurance is extremely helpful for the company because it can then accordingly plan its communication strategy to reach out to those customers and optimise its business model and revenue. Now, we need to predict whether the customer would be interested in Vehicle insurance or not.
## Summary and Conclusion:

The gender variable in the dataset is evenly distributed, with 50.5% of vehicles having past damage and 12.0% of people who have had a damaged vehicle wanting to acquire vehicle insurance. 99.8% of customers have DL, while 0.2% do not have DL.

Vehicle age increases, making it more important to buy insurance to reduce risk.

Middle-aged individuals are more likely to purchase insurance, with 47% having a driver's licence and 21.9% having vehicle insurance.

Further, we applied Machine Learning Algorithms to determine whether a customer would be interested in Vehicle Insurance. Random Forest is the model that performs the best.
