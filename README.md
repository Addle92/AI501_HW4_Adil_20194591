# AI501_HW4_Adil_20194591
This is my submission for HW4 for AI501 Spring 2021 at KAIST 

# M-step Equation derivations:

The detaiels are proveided in 
[M-step Equation derivations.pdf](https://github.com/Addle92/AI501_HW4_Adil_20194591/files/6546170/AI501_HW4_Adil_20194591.pdf)



# How to run the code
1) open the notebook in Colab
2) uplaod the files ( MoG.py, util.py , X.txt) in Colab folder( content)
3) run the code

# Results

<img width="309" alt="MoG results" src="https://user-images.githubusercontent.com/46476184/119647223-b0da5500-be28-11eb-8ee6-6fbae4b94845.PNG">

The figure shows the results of implementing EM algorithm for Mixture of Gaussian with 5 clusters ( k=5) on the provided data (X.txt).

It shows that the algorithm converges to proper clustring of the data, So it was able to find 5 different means and covariances which are represented on the figure as 'x' for the mean and the elipise for the covariance in different colors.  Also, based on the initail values, which are initiated randomly, the algorithm was able to converge in 35 iterations.


# Sensitivity Analysis

The algorithm is very sensetive to the intial values of the model.
In this code, the parameters of the model are initiated randomly, which sometimes reaults in bad clustering. 

the figure shows some cases obsesvred when implementing the code:
1) Due to the fact that there is a probabilty of having multiple means close to each other, this will result in for one cluster the data will be divided between these mean.
2) Another case, there is a probability to have very far mean from the other and on the same time it will be the mean for multiple clusters.

<img width="284" alt="bad results" src="https://user-images.githubusercontent.com/46476184/119653495-1251f200-be30-11eb-8912-3375b0de0e55.PNG">

Therefore, it is recommended to consider an algorithm to initialize proper values.   

