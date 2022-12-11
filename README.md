# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
The company wants to automate the loan approval based on customer detail provided when filling out online application.

## Hypothesis
Salary: Applicants with high income should have more chances of getting approval.

Credit history: Applicants who have credit history have more chances of getting approval.

Loan amount: Less the amount higher the chances of getting approval.

Loan term: Less the time period has higher chances of approval.


## EDA 
1. We have 12 independent variables and 1 target variable,Loan_Status in the training dataset. Let’s look at the columns of the test dataset.

2. Loan Status: Y: 422, N: 192 - 69% people out of 614 got the approval.

3. Datatype png is attached. dtypes.png


4.  80% of applicants in the dataset are male.
   
    Around 65% of the applicants in the dataset are married.
   
    About 15% of applicants in the dataset are self-employed.
   
    About 85% of applicants have repaid their debts.

5.   Most of the applicants don’t have dependents.
    
    About 80% of the applicants are graduates.
    
    Most of the applicants are from semi-urban areas.

6.  The proportion of married applicants is higher for the approved loans.
   
    The distribution of applicants with 1 or 3+ dependents is similar across both the categories of Loan_Status.
   
    There is nothing significant we can infer from Self_Employed vs Loan_Status plot.

7. It seems people with a credit history of 1 are more likely to get their loans approved    

    The proportion of loans getting approved in semi-urban areas is higher as compared to that in rural or urban areas.




## Process

Step 1: Missing Value 
            
            There are missing values in Gender, Married, Dependents, Self_Employed, LoanAmount, Loan_Amount_Term, and Credit_History features.
               
                For numerical variables: imputation using mean
               
                For categorical variables: imputation using mode

Step 2: Outlier Treatment
                 
                 log transformation

Step 3: Logistic Regression

Step 4: Pipelines

Step 5: Grid Search

Step 6: Deployment using Flask

Step 7: Testing


## Results/Demo


ogistic Regression: Accuracy: 80.945%

XGBoost in pipelines:
       
        f1-score: 0.81 , Class 1 recall: 0.96

Grid Search
        f1-score: 0.81, Class 1 recall: 0.98

## Challanges 

I had a very difficult time on the deployment.  got it worked with help.


## Future Goals

1. I will spend more time on Feature Engineering to come up with new features that might affect the target variable

2. Will try Decision Tree and Random Forest 
