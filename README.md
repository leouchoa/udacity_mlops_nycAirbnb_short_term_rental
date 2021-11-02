# Build an ML Pipeline for Short-Term Rental Prices in NYC

You are working for a property management company renting rooms and properties for short periods of 
time on various rental platforms. You need to estimate the typical price for a given property based 
on the price of similar properties. Your company receives new data in bulk every week. The model needs 
to be retrained with the same cadence, necessitating an end-to-end pipeline that can be reused.

The goal of this project is to make the end-to-end machine learning pipeline in a production-ready manner, which means that the object to be deployed is ready to be consumed by customers.

## Setup

This pipeline can be almost entirely run on it's own, you'll just need to setup 3 things:

- [weights and biases](wandb.ai/)
- [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
- [python 3](https://www.python.org/downloads/)

## Pipeline Snapshot

The pipeline constructed will work in a similar fashion to the one describe in the picture bellow and it has 7 major steps:

1. Fetch data
2. Pre-processing
3. Data checks
4. Data segregation (train/validation/test split)
5. Model training and selection
6. Model testing
7. Deployment

![Pipeline snapshot](picture.here)


## How to Use

# Topics to be added to the README file

- Introduction
- How to use
  - dependencies
    - wandb login (API key)
    - conda
    - python
    - git
  - running
    - run whole pipeline
    - run parts of the pipeline
    - run from github
- mlflow errors in env
- deploying the model 
  - online
  - offline
  - docker image
- Next steps
  - cite optuna do hyperparam optimization
  - cite great expectations for testing
  - adding more models to the training scope
  - improve: model/eda/
