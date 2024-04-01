whether existing llms have stereotypical bias: race, gender, etc

create dataset (stereoset), 16k examples

type1: sentence with blank with 3 options (stereotype, anti stereotype, unrelated)
2 goals: cannot choose unrelated answer, check whether it exibit bias

questions
1. take new llm and test on the dataset and compare the icat scores. we expect them to do better
2. what other ideas can we do
3.


## Step 1
1. take a subset of original dataset
2. use a LLM to create 2 more prompts based on the original one (3 total)
3. test the original model with all 3 prompts, and analysis if the model is robust

## Step 2
1. Take a more recent LLM (llama2)
2. run all 3 prompts to the LLM
3. evaluate and compare the results

## evaluation
- which prompts was seen differently due to prompting


# Question
What is the ideal score of stereotype score (ss)?
- 0
- 25
- 50
- 75
- 100