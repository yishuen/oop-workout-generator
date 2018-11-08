# Object Oriented Programming Workout Generator

hi!! to use the workout generator:
1. clone this repository
2. in your command line, run: python -i seed.py

the function to call is GET_RIPPED, which takes 4 arguments
1. what
* which part of your body do you want to work out?
* input this as a LIST
* preloaded options are [abs, arms, upperbod, lowerbod]

2. how_long
* how long do you want your workout to last?
* input duration (in minutes) as and INTEGER

3. equipment
* do you have equipment available to you?
* input BOOLEAN True if you do, and False if you don't

4. who
* this defaults to none
* however, preloaded are 4 people! these 4 people have several exercises they never want to do
* to try it out, you can input (as variables): me, kimmy, titus and lillian (to see these preferences, check out the seed.py file!)

example inputs:
* GET_RIPPED([arms, upperbod], 15, False)
* GET_RIPPED([abs, lowerbod], 10, True, kimmy)
