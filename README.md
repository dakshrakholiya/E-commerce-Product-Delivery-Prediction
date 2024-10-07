# E-commerce-Product-Delivery-Prediction

context : An international e-commerce company based wants to discover key insights from their customer database. They want to use some of the most advanced machine learning techniques to study their customers. The company sells electronic products.

Project Overview:
This project aims to enhance the understanding of product delivery patterns and customer behavior for an international e-commerce company specializing in electronic products. By leveraging machine learning, the project seeks to predict whether products will reach customers on time. The goal is to develop robust machine learning models to accurately predict product delivery timeliness, enabling the company to improve customer satisfaction, optimize logistics, and gain insights into factors affecting delivery performance.

Project Benefits: 
Delivery Optimization: The models will help identify factors influencing on-time delivery, allowing for more targeted logistics strategies. 
Customer Satisfaction: By predicting delivery timeliness accurately, the company can set realistic expectations and improve customer experience. 
Operational Insights: Understanding patterns in product properties, logistics, and customer behavior can assist in better resource allocation and decision-making. 
 
Deliverables: 
Documented machine learning models specifically designed for predicting product delivery timeliness. 
Comprehensive data visualizations illustrating relationships between various factors and delivery performance. 
A comparative analysis of different machine learning algorithms for this classification task.

Data Dictionary: The dataset used for model building contains 10,999 observations of 12 variables, including:

## **Exploratory Data Analysis**
| Variable | Type | Definition | Example |
| ----------- | ----------- | ----------- | ----------- |
| ID | Nominal | Customer ID Number | 10, 15, 10995, 10996
| Warehouse_block | Nominal | Warehouse to Store the Product | A, B, C, D, F
| Mode_of_Shipment | Nominal | Mode of Product Shipping | Flight, Road, Ship
| Customer_care_calls | Discrete | Number of Calls Made | 1, 2, 5, 6
| Customer_rating | Ordinal | Company Rating by Customers | 5: Best - 4: Better - 3: Neutral - 2: Bad - 1: Worst
| Cost_of_the_Product | Discrete | Cost of Product in US Dollars | 177, 216, 236, 182
| Prior_purchases | Discrete | Number of Prior Purchase | 3, 2, 6
| Product_importance | Ordinal | Product Importance Parameter | Low, Medium, High
| Gender | Nominal | Customer Gender | Male, Female
| Discount_offered | Discrete | Product Discount in US Dollars | 65, 10, 16
| Weight_in_gms | Continous | Product Weight in grams | 4953, 5676, 2171
| Reached.on.Time_Y.N | Nominal | Target Variable, 1: NOT reached on time - 0: REACHED on time | 1, 0


## **Conclusion:**
The aim of the project was to predict whether the product from an e-commerce company will reach on time or not. This project also analyzes various factors that affect the delivery of the product as well as studies the customer behavior. From the exploratory data analysis, I found that the product weight and cost has an impact on the product delivery. Where product that weighs between 2500 - 3500 grams and having cost less than 250 dollars had higher rate of being delivered on time. Most of the products were shipped from warehouse F though ship, so it is quite possible that warehouse F is close to a seaport.

The customer's behaviour also help in predicting the timely delivery of the product. The more the customer calls, higher the chances the product delivery is delayed. Interestingly, the customers who have done more prior purchases have higher count of products delivered on time and this is the reason that they are purchasing again from the company. The products that have 0-10% discount have higher count of products delivered late, whereas products that have discount more than 10% have higher count of products delivered on time.

The Random Forest classifier achieved the highest accuracy of 70%, outperforming other models such as the Decision Tree classifier (68%) and Logistic Regression (66%). The K-Nearest Neighbors (KNN) model showed the lowest performance with an accuracy of 65%





