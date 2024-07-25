import datetime
import sys
import TweetHandler
import TweetGeneratorAI
import random


today = str(datetime.date.today())


# As the model is not able to answer current affairs ask historical facts and known inveting knowledge
promptlist = [
              # on finance and economy
              (["Create a tweet that is funny on finance and economy.",
                "Create a tweet on less known historical fact and knowledge about finance and economy.",
                "Create a tweet on interesting fact and knowledge about finance and economy of a country or business from past.",], 1),
              
              # on  stock
              (["Create a tweet interesting fact and knowledge about a picked stock.",
                "Create a tweet interesting fact and knowledge one stock in India.",
                "Create a tweet on a less known stock stock wat it does as a company.",
                "Create a tweet on interseting story about a stock merger and acquision.",], 1),
              
              # on  taxation 
              (["Create a tweet on personal finance habits.",
                "Create a tweet on personal finance terms.",
                "Create a tweet on less known fact and knowledge about Taxation in investing.",
                "Create a tweet on legal way to save taxes.",
                "Create a tweet on importance of tax planning.",], 1),
              
              # on  investing
              (["Create a tweet on investing knowlegde.",
                "Create a tweet on less known fact and knowledge about Investing.",
                "Create a quick explainer tweet on a popular Investing termenalogy.",
                "Create a quick explainer tweet on a popular Investing ratios and terms with stock example.",], 1),
              

              # on trending startups
              (["Create a tweet on startups and entrepreneurship.",
                "Create a tweet on startups and entrepreneurship in India.",
                "Create a tweet on less known fact and knowledge about startups and entrepreneurship.",
                "Create a tweet on and knowledge about startups and entrepreneurship in India.",], 2),
              
              # on investing personalities 
              (["Create a amazing tweet on entrepreneur personality.",
                "Create a tweet on one investing personality.",
                "Create a tweet on one investing personality in India.",
                "Create a tweet on less known fact and knowledge about investing personalities.",
                "Create a tweet on one investing personality in India and their investing story or journey.",
                "Create a tweet on investing personality and their investing story or journey.",],  1),
              
              # on trending statisctics
              (["Pick one financial asset and Create a tweet expaining what to do and how to Invest.",
                "Pick one financial asset and Create a tweet expaining what to do and how to Invest in India.",
                "Pick one financial product and Create a tweet on what to do and how to Invest."
                "Pick one financial product and Create a tweet on how it works."
                "Pick one industry or business and Create a tweet on how it works." ], 3),

              (["Pick one career option and opportunity in india in finance field and Create a tweet on it.",
                "Pick one career option and opportunity in India in finance field and Create a tweet toexpain what they do."
                "Pick one one city in India and its main industry and Create a tweet on it."], 1),

              
            ]



def random_prompt(promptlist):
   
    # Separate the items and weights
    items, weights = zip(*promptlist)

    # Select one item based on the weights
    selected_item = random.choices(items, weights=weights, k=1)[0]

    return random.choice(selected_item)



aitweetprompt = (random_prompt(promptlist) +
                "Create only a single tweet that does not exceed the 280 character limit. "
                "Ensure that the information in created tweet is genuine, correct and valid on today's date - " + today + ". "
                "I am a finance content creator on Twitter who tweets about finance topics"
                "The result should be in plain text, without including any markdown elements. "
                "Does not include a call to action (e.g., 'Learn more,' 'Subscribe,' 'Read this'). "
                "Do not Add any visuals like images or GIFs. Do not ask to link to a blog or video. "
                "Use only one relevant hashtags to reach a wider audience."
                "Do not say like 'Did you know or Do you know', rather create a straightforward text.")




def main():
    try:
        print("INFO:This is the main method of the program")

        response = TweetGeneratorAI.generate_tweet(aitweetprompt)
        TweetHandler.post_tweet(response)
    except Exception as e:
        sys.exit("An error occurred: {}".format(str(e)))


if __name__ == "__main__":
    main()