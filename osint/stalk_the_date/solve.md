# WriteUps Stalk the date

## 1. StackOverflow

The first idea is to go to **Stackoverflow** or sites in which web technologies are explained because he got a *gold HTML badge* long time ago. This website where you can find answers to a lot of questions and the experts are awarded with different badges. You can find a list of the users who fulfilled this task ordered by date of achievement.

![XXX](https://github.com/SecuritIIE/solves_ctf2024/raw/main/osint/stalk_the_date/Solution/1.png)

We find the users who achieved the *gold HTML badge in 2013*.

![XXX](https://github.com/SecuritIIE/solves_ctf2024/raw/main/osint/stalk_the_date/Solution/2.png)

We found out that the first and only one to won a gold HTML badge in July 2013 is **Spudley**. He came from **England**, let's take note and move on !

![XXX](https://github.com/SecuritIIE/solves_ctf2024/raw/main/osint/stalk_the_date/Solution/3.png)

## 2. Twitter account

His twitter name account is *F14sh_W1l50n* , we find many of the things that he likes in his life, 
but the most relevant posts are these ones:

- One strange post with a code :

![XXX](https://github.com/SecuritIIE/solves_ctf2024/raw/main/osint/stalk_the_date/Solution/4a.png)

- A photo of a restaurant, surely his favourite one because he went with his friend :

![XXX](https://github.com/SecuritIIE/solves_ctf2024/raw/main/osint/stalk_the_date/Solution/4c.png)

The secret message is encoded in military language code, with the first letter of each idea:

![XXX](https://github.com/SecuritIIE/solves_ctf2024/raw/main/osint/stalk_the_date/Solution/4b.png)

## 3. Tripadvisor

Next thing is to find his favourite restaurant among the best ones ("*he loves to eat in the best restaurants.*"), 
After few research you find a restaurant in London starting by *Chim* as in the previous image : The restaurant is **Chimichurris** 
and you one have a review from a certain F. Wilson (you can find his name in twitter) ! 

![XXX](https://github.com/SecuritIIE/solves_ctf2024/raw/main/osint/stalk_the_date/Solution/5.png)

![XXX](https://github.com/SecuritIIE/solves_ctf2024/raw/main/osint/stalk_the_date/Solution/6.png)

## 4. CyberChef

After obtaining the encrypted review, decode it using a rotational cipher. The rotation number increases by two every two words. By the end, you'll have the full list of ingredients.

![XXX](https://github.com/SecuritIIE/solves_ctf2024/raw/main/osint/stalk_the_date/Solution/7.png)

## 5. Recipe

Here’s the recipe, along with the fact that he loves Argentinian desserts. We need to identify which dessert matches the ingredients from this list: Chocotorta, Pastelitos, Helado, or Alfajores. Ultimately, the recipe corresponds to Alfajores (which is the same as the cookie recipe).

![XXX](https://github.com/SecuritIIE/solves_ctf2024/raw/main/osint/stalk_the_date/Solution/8.png)

## 6. Hash

Chimichurris_Alfajores -[HASHMD5]-> d797712b3bbefdd084aab2e43f235d36

FSIIECTF{d797712b3bbefdd084aab2e43f235d36}
