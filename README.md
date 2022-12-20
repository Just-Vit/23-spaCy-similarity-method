# 23-spaCy-similarity-method

>>> Step 3 — Creating the Chatbot. Use the spaCy similarity() method.

First, for the ease of debugging rename file w_1_api_good.py created in previous repo to w_2_similarity_good.py.

Add some code to w_2_similarity_good.py.

Step 3.1., import spaCy and load the English language model:

    import spacy
    import requests
    
    nlp = spacy.load("en_core_web_md")
    
    . . .

After the get_weather() function in your file, create a chatbot() function representing the chatbot that will accept a user’s statement and return a response.

Following your definition, add the highlighted code to create tokens for the two statements you’ll be comparing. Tokens are the different meaningful segments of a statement, like words and punctuation. This is necessary to allow spaCy to compute the semantic similarity:

    . . .
    def chatbot(statement):
      weather = nlp("Current weather in a city")
      statement = nlp(statement)
      
      
Here the weather and statement variables contain spaCy tokens as a result of passing each corresponding string to the nlp() function.

Save and close your file.

Next you’ll be introducing the spaCy similarity() method to your chatbot() function. The similarity() method computes the semantic similarity of two statements as a value between 0 and 1, where a higher number means a greater similarity. You need to specify a minimum value that the similarity must have in order to be confident the user wants to check the weather.

For example, if you check the similarity of statements 2 and 3 with statement 1 following, you get:

    Current weather in a city
    What is the weather in London? (similarity = 0.86)
    Peanut butter and jelly (similarity = 0.31)

********

To try this for yourself, open the Python interpreter:

    python

Next, import spaCy and load the English-language model:

>>> import spacy
>>> nlp = spacy.load("en_core_web_md")

Now let’s create tokens from statements 1 and 2:

>>> statement1 = nlp("Current weather in a city")
>>> statement2 = nlp("What is the weather in London?")

Finally, let’s obtain the semantic similarity of the two statements:

>>> print(statement1.similarity(statement2))

You will receive a result like this:

Output
0.8557684354027663

Setting a low minimum value (for example, 0.1) will cause the chatbot to misinterpret the user by taking statements (like statement 3) as similar to statement 1, which is incorrect. Setting a minimum value that’s too high (like 0.9) will exclude some statements that are actually similar to statement 1, such as statement 2.

We will arbitrarily choose 0.75 for the sake of this tutorial, but you may want to test different values when working on your project.

Let’s add this value to the script. First, open the file:

    nano w_2_similarity_good.py

Then add the following highlighted code to introduce the minimum value:

    import spacy
    
    . . .
    
    def chatbot(statement):
     weather = nlp("Current weather in a city")
     statement = nlp(statement)
     min_similarity = 0.75

Now check if the similarity of the user’s statement to the statement about the weather is greater than or equal to the minimum similarity value you specified. Add the following highlighted if statement to check this:

    import spacy
    
    . . .
    
    def chatbot(statement):
     weather = nlp("Current weather in a city")
     statement = nlp(statement)
     min_similarity = 0.75

    if weather.similarity(statement) >= min_similarity:
    pass


Run second test to check if it is working so far.
Add two lines of code to the botton of your file:

    #test_2
    #Add those two lines and run just to test the "similarity"code 
    #(output was "mist")	
	  
    similarity1 = chatbot("What is the weather in Kiev and Bundaberg")
    print(similarity1)

And run it 

    python w_2_similarity_good.py

the outcome be like that:

	┌──(my_weather)─(vit㉿acer)-[~]
	└─$ python w_2_similarity_good.py  
	scattered clouds
	0.8284746233849366



