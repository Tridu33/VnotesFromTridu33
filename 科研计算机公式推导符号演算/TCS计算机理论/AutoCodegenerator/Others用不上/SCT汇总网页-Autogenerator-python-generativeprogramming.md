# generativeprogramming




generativeprogramming.com/concepts/references/








GP的目的是在生成器和目标程序应用程序的开发过程中提供更大的灵活性。例如，当我们可以使用完全适合要构建的应用程序的特定需求的多个生成器时，为什么在整个程序解决方案中仅使用一个生成器？发电机的可重用性又如何适应新的类似项目的需求？

尽管GP的原始概念提供了一些有趣的解决方案，甚至提供了整个开发框架，但由于OOP模型的刚性，它仍然遭受缺乏灵活性的困扰。而且，UML还没有被证明适合于设计生成器，特别是在与方面建模相关的部分中。

基于脚本语言的GP

脚本语言努力做到无类型，适合于粘合不同的组件，使用灵活的数据结构，并对其进行解释，从而能够从变量以及名为脚本的程序段中执行编程代码。为什么我们不使用脚本语言来构建代码生成器，或者甚至更好地同时开发生成器和目标应用程序？

从这些假设出发，克罗地亚萨格勒布大学的一群教师于2000年代初开始开发基于脚本语言的生成器。该概念首先被命名为**SGM（脚本生成器模型**）。SGM引入了专门用于生成器建模的图形图。**规范图**定义了要生成的目标应用程序的功能及其层次结构，而配置图定义了这些功能（即方面）在不同应用程序部分上的分散性。

该模型在00年代后期升级为the**SCT generator model**。SCT具有完整的可配置性，因此无需像以前那样对配置进行编程，而可以使用适当的语法进行指定。**基于SCT的Autogenerator**建于2010年代初期。Autogenerator利用脚本语言的可能性，不仅从程序脚本，还从变量评估程序代码。脚本语言（我们使用**Python**）中的程序代码按需生成并立即执行。此概念具有一些优点，例如，在运行程序时动态更改程序规范，一定程度的自省，因此程序员可以查看当前正在使用的规范，配置和模板的哪些部分，动态更改程序依赖项，例如添加/删除一些数据库列，最后使用动态规范。动态规范表示使用现有数据库结构内部的异构数据结构并自动生成代码来处理它们的可能性。

我们在这些页面中提供什么？

我们的目的是展示我们在构建发电机和相关系统方面的成就，以及来自世界各地的同事的成就。对我们来说，生成式编程是一个伟大的概念，近年来，它被无理地忽略了。此外，在信息学，机器学习和所有其他自动化领域的教学领域中，还有许多创新，因此让我们生成并生成东西吧！











# teaching



https://generativeprogramming.com/concepts/teaching/






# 引用

Radošević 整个网页专门做这个






Radošević, D.; Bernik, A.; Mrvac, N.:”Web Sites Internationalization using Domain Translator“, Tehnički vjesnik : znanstveno-stručni časopis tehničkih fakulteta Sveučilišta u Osijeku, 26 (2019), 3; 668-673 doi:10.17559/TV-20180702105206 Add to Citavi project by DOI

Radošević, D.; Bernik, A.; Dobša, J.; Kaniški, M.; Mrvac, N.:”Dynamic Machine Translation of Croatian Academic Web Sites“, Proceedings of 42nd International Convention – Mipro 2019 / Skala, Karolj (ur.).

Strmečki, D., Magdalenić, I., Radošević, D.:”A Systematic Literature Review on the Application of Ontologies in Automatic Programming“, International journal of software engineering and knowledge engineering (IJSEKE), ISSN 0218-1940, str. 559-591., 2018.

Dobša, J.; Mladenić, D.; Rupnik, J.; Radošević, D.; Magdalenić, I.”Cross-language information retrieval by reduced k- means“, International Journal of Computer Information Systems and Industrial Managerment Applications, 10 (2018), 1; 314-322

Radošević, D., Magdalenić, I., Andročec, D., Bernik, A., Kaniški, M.:”**A machine translation model inspired by code generation**“, Proceedings of the 28th Central European Conference on Information and Intelligent Systems (Ceciis 2017), , ISSN 1847-2001, Varaždin, 27-29.09.2017., str. 187-192., 2017.

Novak, M., Magdalenić, I., Radošević, D.:”Common Metamodel of **Component Diagram and Feature Diagram in Generative Programming**“, Journal of Computer Science, ISSN:1549-3636, 12 (10), 517-526, 2016.

Mlakar, J., Radošević, D., Magdalenić, I.:”Generating Web Applications Using **CodeWorker**“, Proceedings of the 26th Central European Conference on Information and Intelligent Systems (Ceciis 2015), ISSN 1847-2001, Varaždin, 23.-25.09.2015. ,pp. 233-238, 2015.

Strmečki, D., Radošević, D., Magdalenić, I.:”Web form generators design model“, Proceedings of the 26th Central European Conference on Information and Intelligent Systems (Ceciis 2015), ISSN 1847-2001, Varaždin, 23.-25.09.2015. ,pp. 255-260, 2015.

Bernik, A., Bubaš, G., Radošević, D.:”A Pilot Study of the Influence of Gamification on the Effectiveness of an e-Learning Course“, Proceedings of the 26th Central European Conference on Information and Intelligent Systems (Ceciis 2015), ISSN 1847-2001, Varaždin, 23.-25.09.2015. ,pp. 73-79, 2015.

Kvesić, A., Radošević, D., Orehovački, T.:”Dynamic Frames Based Generation of 3D Scenes and Applications“, Acta Graphica, ISSN: 0353-4707, 26(1-2), 11-19., 2015.

Orehovački, T., Magdalenić, I., Radošević, D.:”Dynamic Frames-Based Generation of Web 2.0 Applications“, Proceedings of the 7th International Conference on Information Technology (ICIT), str. 90-95, ISSN 2306-6105, Amman, Jordan, 12-15.05.2015.

Kvesić, A., Radošević, D., Orehovački, T.:”Using SCT Generator and Unity in Automatic Generation of 3D Scenes and Applications“, Proceedings of the 25rd Central European Conference on Information and Intelligent Systems (Ceciis 2014), Varaždin, 17.-19.09.2014., 2014.

Fabac, R., Radošević, D., Magdalenić, I.:”Autogenerator-Based Modelling Framework for Development of Strategic Games Simulations: Rational Pigs Game Extended“, The Scientific World Journal, Hindawi, ISSN: 2356-6140 (Print) 1537-744X (Online), Volume 2014, Article ID 158679, 31 August 2014.

Kozina, M., Radošević, D., Magdalenić, I.:”Customizing of the Software Organization Maturity Level Assessments Using **SCT Based Generator**“, Proceedings of the 24rd Central European Conference on Information and Intelligent Systems (Ceciis 2013), Varaždin, 18.-20.09.2013., 2013.

Radošević, D., Magdalenić, I., Orehovački, T.:”Building Process of **SCT Generators**“, Proceedings of Mipro 2013, Opatija, May 20-24 2013.

Magdalenić, I., Radošević, D., Orehovački, T.:”Autogenerator: Generation and Execution of Programming **Code on Demand**“, Expert Systems with Applications (ESWA), Elsevier, ISSN: 0957-4174, Volume 40, Issue 8, 15 June 2013, Pages 2845-2857.

Ivković, N., Radošević, D., Magdalenić, I.:”Towards Automatic Generation of Parallel Programs“, Central European Conference on Information and Intelligent Systems (Ceciis 2012), Varaždin, 19.-21. September 2012.

Radošević, D., Orehovački, D.,Magdalenić, I.:”Towards the Software Autogeneration“, Proceedings of Mipro 2012, Opatija, May 21-25 2012.

Radošević, D., Bračun, D.,Magdalenić:”Generating Graphic User Interface of Web Applications Using **Source Code Generator** Based on Dynamic Frames“, Computer Technology and Application (CTA), ISSN 1934-7332, volume 2, number 11, pp. 843-848., 2011.

Radošević, D., Magdalenić, I., Orehovački, T.:”Error Messaging in Generative Programming“, Central European Conference on Information and Intelligent Systems, CECIIS 2010, Varaždin, 21-23, September 2011.

Radošević, D., Magdalenić, I.:”**Source Code Generator Based on Dynamic Frames**“, Journal of Information and Organizational Sciences (JIOS), ISSN 1846-3312, 35 (2011), 1, 2011.

Radošević, D., Magdalenić, I.:”Python Implementation of **Source Code Generator Based on Dynamic Frames**“, Proceedings of “Mipro 2011”, Opatija, 23.05.-27.05.2011.

Magdalenić, I., Radošević, D., Kermek, D.:”Implementation Model of Source Code Generator“, Journal of Communications Software and Systems (JCOMSS), 7 (2011), 2; 1-9, ISSN: 1845-6421, 2011.

Radošević, D., Magdalenić, I.:”Introducing Polymorphic Features into a Scripting Model of Generator“, Journal of computing and information technology (CIT), ISSN 1330-1136, 19 (2011), 1; str. 57-67, 2011.

Radošević, D., Orehovački, T., Stapić, Z:”**Automatic On-line Generation of Student´s Exercise**s in Teaching Programming“, Central European Conference on Information and Intelligent Systems, CECIIS 2010, Varaždin, 22-24 September 2010.

Magdalenić, I., Radošević, D., Skočir, Z.:”Dynamic Generation of Web Services for Data Retrieval Using Ontology“, INFORMATICA, 2009, Vol. 20, No. 3, pg. 397–416, ISSN 0868-4952, Institute of Mathematics and Informatics, Vilnius, Lithuania, 2009.

Radošević, D., Kliček, B., Kozina, M.:”Upgrading Generator Scripting Model by Object Model Properties“, The IPSI BgD Transactions on Internet Research, Volume 5 Number 1 (ISSN 1820-4503), IPSI Bgd Internet Research Society, Belgrade, January 2009.

Radošević, D., Konecki, M., Orehovački, T.:”Java Applications Development Based on Component and Metacomponent Approach“, Journal of Information and Organizational Sciences (JIOS), Faculty of Organization and Informatics, Varaždin, 2008.

Radošević, D., Orehovački, T., Konecki, M.:”WEB oriented applications generator development through reingineering process“, DAAAM International Scientific Book 2007, DAAAM International, Vienna, Austria 2007.

Radošević, D., Orehovački, T., Konecki, M.:”PHP Scripts Generator for Remote Database Administration based on C++ Generative Objects“, Proceedings of “Mipro 2007” conference, Opatija, 21.05.-25.05.2007.

Radošević, D., Kliček, B., Kozina, M.:”Conceptual Similarities and Differences Between Object Model and Generator Application Scripting Model“, DAAAM International Scientific Book 2006, DAAAM International, Vienna, Austria 2006.

Radošević, D., Kliček, B., Dobša, J.:”Generative Development Using Scripting Model of Application Generator“, DAAAM International Scientific Book 2006, DAAAM International, Vienna, Austria 2006.

Radošević, D.: “Integration of Generative Programming and Scripting Languages” Doctorate thesis, Faculty of Organization and Informatics, Varaždin, 2005. (abstract)

Dumičić K, Sajko M, Radošević D.: “Designing a Web-Survey Questionnaire Using Automatic Process and a Script Language“, Journal of Information and Organizational Sciences (JIOS),Vol. 26, NO. 1-2, Faculty of Organization and Informatics, Varaždin, 2002.










