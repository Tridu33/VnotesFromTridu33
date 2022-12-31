

# 1. PDDL

en.wikipedia.org/wiki/Planning_Domain_Definition_Language







https://dblp.uni-trier.de/search?q=pddl


[Writing Planning Domains and Problems in PDDL](http://users.cecs.anu.edu.au/~patrik/pddlman/writing.html)



en.wikipedia.org/wiki/Planning_Domain_Definition_Language

古典计划使用从STRIPS建模语言[Richard E Fikes and Nils J Nilsson.  Strips: A new approach to the application of theorem proving to problemsolving.Artificial intelligence, 2(3-4):189–208, 1971]派生而来的正式描述语言，称为计划领域定义语言（PDDL）[Drew McDermott, Malik Ghallab, Adele Howe, Craig Knoblock, Ashwin Ram, Manuela Veloso, Daniel Weld,and David Wilkins. Pddl-the planning domain definition language, 1998.]


我们关注的是令人满意的计划任务，它可以由集合（F，O，I，G）定义，其中F是一组命题（或谓词），它们描述任务实例中存在的对象的属性及其关系，O是一组运算符（或操作类型），ICF是初始状态，而GCF是目标状态的集合。每个动作类型GO都由三元组（Pre（o），Add（o），Del（o））定义，其中前提为Pre（o）是一组谓词，这些谓词必须具有正确的值才能适用于该操作，Add（o）是一组谓词，在应用后该行为将变为真，而Del（o）是一组谓词，该行为将变为false根据申请。我们试图找到一个计划或一系列行动，这些行动或行动序列一旦应用，就会在一定时限或预定数量的步骤内导致状态为G C的状态。查找计划任务的计划通常是通过启发式搜索方法来完成的，但是，在这项工作中，我们专注于学习反应式计划策略，这些策略可以在特定领域的实例上进行训练，然后推广到同一领域中新的看不见的实例。























