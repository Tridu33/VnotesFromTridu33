#谜语riddles

https://stackoverflow.com/questions/16493233/swi-prolog-puzzle


# 跟着这两个就行！！！！

https://math.stackexchange.com/questions/179968/what-is-the-name-of-the-logical-puzzle-where-one-always-lies-and-another-always/184907#184907

https://stackoverflow.com/questions/49323894/prolog-solution-of-a-riddle



 ```


coding









```





















# 谎言真话
https://sg.answers.yahoo.com/question/index?qid=20070503170827AA20Xk2&guccounter=1&guce_referrer=aHR0cHM6Ly9jbi5iaW5nLmNvbS8&guce_referrer_sig=AQAAAIZZSFBWOePHGvGjyTd-cXhDveHHYabHvLsu87HQnv6jKIeiyNMJYBl2PjPPO48hISTSLZsBXgLzUHRIHIn91Tf3QhwlWGOqbED4-X0O71bIMjEsbhjs2f5_7iWm8HRznU7yhtaO-A45gU4ZD7O776Uu6OuDDFhoDIRb5QZ7_Qoa

**Did the tour guide tell the truth or a lie?**
Jonny visits an island. There are two tribes on the island. One tribe always tells the truth, and the other always lies. Jonny saw a guy passing him and askes his tour guide to ask the guy where he lived. The tour guide asked the guy and came back with the answer: the guys lives over west (tribe that tells the truth). Did the tour guide tell the truth or a lie?



https://math.stackexchange.com/questions/179968/what-is-the-name-of-the-logical-puzzle-where-one-always-lies-and-another-always/184907#184907



https://stackoverflow.com/questions/55602609/prolog-tells-me-a-procedure-is-undefined-when-it-appears-to-be-defined

https://stackoverflow.com/questions/49323894/prolog-solution-of-a-riddle
解决办法Prolog


MPACC一道逻辑题求解.  
正题:某地住着甲,乙两个部落,甲部落的人总是说真话,乙部落的人总是说假话.一天,某旅行者来到这里,遇见一个当地人,旅行者就问他:“你是哪个部落的?”A回答他是甲部落的；这时候又过来一个当地人,旅行者就请A去问B相同的问题,B回答后,A告诉旅行者,B回答他是甲部落的.根据以上情况,我们可以确定:A.A和B都是甲部落的.B.A和B都是乙部落的.C.A是甲部落的,B是乙部落的.D.A是甲部落的,不清楚B的情况.E.A和B的情况都无法确定.




如果要用逻辑学方法解决,就要知道,本题共涉及到3组命题：  
（1）X是甲部落还是乙部落；（等同于“X是说真话还是说假话”,所以用一个命题表示）  
（2）当我们问X是哪个部落时,X回答自己是甲部落还是乙部落；  
（3）当我们请X向Y问上述问题时,X转达Y说自己是甲部落还是乙部落；  
　　因为上述3组命题的结果,不是甲部落就是乙部落,所以我们可以用一对矛盾命题表示.  
我们用符号表示命题：  
（1）P（X）：X是甲部落的；（也表示了X是说真话的）  
（2）Q（X）：X回答他是甲部落的；  
（3）R（X,Y）：X回答Y说自己是甲部落的；  
　　根据上述命题的逻辑关系,可以得出以下结论：  
①：P（X）→Q（X）；X是甲部落的,说真话,所以回答自己是甲部落的；  
②：￢P（X）→Q（X）；X是乙部落的,说假话,所以也回答自己是甲部落的；  
★①、②的一个直接结论就是：Q（X）恒为真；即：  
　　　　对于这两个部落的人,不论你问谁,他都会说自己是甲部落的人；  
　　所以,A的第一次回答“A回答他是甲部落的”对我们没有任何用处.不过我们可以推断：当旅行者请A向B问问题时,即使A没有回复,旅行者也知道B回答的是“我是甲部落的”.但至于A如何转述B的回答,就要看A是否诚实了.所以：  
③：P（X）→R（X,Y）；  
④：￢P（X）→￢R（X,Y）；  
　　即：X的转述与Y无关,只和他自己是否诚实有关；  
★利用③、④,我们可直接得出这样一个结论：P（X）↔R（X,Y）；即：  
　　X转述Y的回答时所说的部落,与他自己“实际”所属的部落是相同的；  
　　所以：当“A告诉旅行者,B回答他是甲部落的”时,我们就可以确定A就是甲部落的.而至于乙,我们就无法判断了.所以,答案是D.





# COQ
https://math.stackexchange.com/questions/179968/what-is-the-name-of-the-logical-puzzle-where-one-always-lies-and-another-always/184907#184907



https://stackoverflow.com/questions/49323894/prolog-solution-of-a-riddle



























































































































































