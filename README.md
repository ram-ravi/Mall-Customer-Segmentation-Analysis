## Mall-Customer-Segmentation-Analysis
<img src="https://images.unsplash.com/photo-1519567241046-7f570eee3ce6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=80" width="650" height="350">

This is a Exploratory Data Analysis on the dataset givis us various nuances on different relationship between the feature variables.The dataset has details like Annual Income, Age, Customer Id, Spending Score (1-100).Lets start with Andrews curve. 

<img src="https://user-images.githubusercontent.com/64869288/90749071-d8900180-e287-11ea-8d79-c254a2df578e.png" width="800" height="350">
<br />

The andrews curve preserves the means, distance(up to a constant) and variances.<br>


<img src="https://user-images.githubusercontent.com/64869288/90749397-42a8a680-e288-11ea-8694-f42f480d0941.png" width="800" height="350">

We can infer one thing that There are few people who earn more than 100 US Dollars. Most of the people have an earning of around 50-75 US Dollars. Also, we can say that the least Income is around 20 US Dollars.
 
#### Taking inferences about the Customers.

The most regular customers for the Mall has age around 30-35 years of age. Whereas the the senior citizens age group is the least frequent visitor in the Mall. Youngsters are lesser in umber as compared to the Middle aged people.


<img src="https://user-images.githubusercontent.com/64869288/90749576-77b4f900-e288-11ea-87db-2c7a0666c86b.png" width="800" height="350">

If you can see the pie chart, it is clear that female gender leads the male count by atleast 56%
that is a huge gap specially when the population of Males is comparatively higher than females.


<img src="https://user-images.githubusercontent.com/64869288/90749659-961af480-e288-11ea-8842-1bea12af6b27.png" width="800" height="350">

This graph shows a more interactive chart about the distribution of each Age grou in the mall.
It is seen that the ages from 27 to 39 are very much frequent but there is no clear pattern. Interesting Fact, There are equal no. of Visitors in the Mall for the Agee 18 and 67. People of Age 55, 56, 69, 64 are very less frequent in the Malls. People at Age 32 are the Most Frequent Visitors in the Mall.



<img src="https://user-images.githubusercontent.com/64869288/90749839-cfebfb00-e288-11ea-8482-380102dd06e7.png" width="800" height="350">

Interesting Fact, There are equal no. of Visitors in the Mall for the Agee 18 and 67. People of Age 55, 56, 69, 64 are very less frequent in the Malls. People at Age 32 are the Most Frequent Visitors in the Mall.


<img src="https://user-images.githubusercontent.com/64869288/90749887-e42ff800-e288-11ea-84e5-3c34ac7fe1c4.png" width="800" height="350">

This is the most important chart of all. 
This shows that the mall has a variety of customers coming in since the chart here shows a spending score from 1 till 99. This shoes that the mall caters to the needs of different class of poeple. However, the most cutomers spending score lies between 35-60.


<img src="https://user-images.githubusercontent.com/64869288/90749943-fb6ee580-e288-11ea-840d-1d9a1297f61b.png" width="800" height="350">

This shows the relationship between each feature variable with itself and with the other variables in the table. This helps in finding the hidden relationship between the chosen variable(target) and the other important features selected.

<img src="https://user-images.githubusercontent.com/64869288/90750041-1a6d7780-e289-11ea-8472-51966ab8c3d9.png" width="800" height="350">

If you can see the matrix, the features does not have any good correlation, thus proceeding with all the features.


<img src="https://user-images.githubusercontent.com/64869288/90750116-38d37300-e289-11ea-9416-fcf7c0551ae9.png" width="800" height="350">

This shows the spending score of male is around 25k to 70k whearas the female gender has a spending score of 35k to 75k.This shows the clear domination of female gender in the shopping arena!


<img src="https://user-images.githubusercontent.com/64869288/90750160-4a1c7f80-e289-11ea-822a-9fbefc02906d.png" width="800" height="350">

This is that the male has higher average salary than the female gender, while if you compare lower income, both the gender is almost equal.


<img src="https://user-images.githubusercontent.com/64869288/90750295-71734c80-e289-11ea-870d-2d388e0e3860.png" width="800" height="350">

The above chart shows the relationship between age and annula income, also annual income and spending score.



<img src="https://user-images.githubusercontent.com/64869288/90750479-b4352480-e289-11ea-9a1c-ee9aa7445ab8.png" width="800" height="350">

Optimum elbow clustering - 5


<img src="https://user-images.githubusercontent.com/64869288/90750354-8cde5780-e289-11ea-85a4-5995141b1fef.png" width="800" height="350">

There are five segments in the mall and the label explains them in breifly.The mall authorities have to take care of the careul categories to avail some benefits so that they move to the general category.


<img src="https://user-images.githubusercontent.com/64869288/90750423-9ebffa80-e289-11ea-8433-444f8b781e09.png" width="800" height="350">

Dendrogram-Heirarchial Clustering

<img src="https://user-images.githubusercontent.com/64869288/90750710-0d9d5380-e28a-11ea-9f26-1e2f3c36c155.png" width="800" height="350">

Elbow method-optimum number of clusters -4 Age vs Spending Score (1-100)


<img src="https://user-images.githubusercontent.com/64869288/90750785-27d73180-e28a-11ea-83a8-2b49eddf4c8c.png" width="800" height="350">

KMeans-Age vs Spending Score- The age and spending score by looking at the above chart, we have the usual customer spread over all ages. And we also have the target customers with young and old ages.Then after getting the results we can accordingly make different marketing strategies and policies to optimize the spending scores of the customer in the Mall.
































































































