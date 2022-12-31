# MDP算法和FOND



```c++
algorithm=value-iteration(epsilon=<float>,max-number-iterations=<integer>,heuristic=<request>,seed=<integer>)
algorithm=improved-lao(epsilon=<float>,heuristic=<request>,seed=<integer)
algorithm=hdp(epsilon=<float>,heuristic=<request>,seed=<integer)
algorithm=ldfs(epsilon=<float>,heuristic=<request>,seed=<integer)
algorithm=ldfs-plus(epsilon=<float>,heuristic=<request>,seed=<integer)
algorithm=plain-check(epsilon=<float>,heuristic=<request>,seed=<integer)
algorithm=lrtdp(epsilon=<float>,heuristic=<request>,epsilon_greedy=<float>,seed=<integer)
algorithm=standard-lrtdp(epsilon=<float>,heuristic=<request>,epsilon_greedy=<float>,seed=<integer)
algorithm=uniform-lrtdp(epsilon=<float>,heuristic=<request>,epsilon_greedy=<float>,seed=<integer)
algorithm=bounded-lrtdp(epsilon=<float>,heuristic=<request>,bound=<integer>,epsilon_greedy=<float>,seed=<integer)
algorithm=simple-a*(heuristic=<request>,seed=<integer)
```

https://github.com/bonetblai/mdp-engine



Collection of algorithms for solving Markov Decision Processes. The collection contains Value Iteration, LAO`*`, LRTDP, LDFS, Anytime AO`*` and UCT.

The code in this project comes from different articles published in different years:

- B. Bonet and H. Geffner. *Action Selection for MDPs: Anytime AO`\*` vs. UCT*. Proc. 26th AAAI Conf. on Artificial Intelligence (AAAI). Canada. 2012. [(PDF)](http://ldc.usb.ve/~bonet/reports/AAAI12-anytime.pdf)
- B. Bonet and H. Geffner. *Learning Depth-First Search: A Unified Approach to Heuristic Search in Deterministic and Non-Deterministic Settings, and its application to MDPs*. Proc. 16th Int. Conf. on Automated Planning and Scheduling (ICAPS). UK. 2006. Pages 142-151. [(PDF)](http://ldc.usb.ve/~bonet/reports/ICAPS06-ldfs.pdf)
- B. Bonet and H. Geffner. *An Algorithm Better than AO`\*`?*. Proc. 20th Conf. on Artificial Intelligence (AAAI). USA. 2005. Pages 1343-1348. [(PDF)](http://ldc.usb.ve/~bonet/reports/AAAI05-ldfs.pdf)
- B. Bonet and H. Geffner. *Faster Heuristic Search Algorithms for Planning with Uncertainty and Full Feedback*. Proc. 18th Int. Joint Conf. on Artificial Intelligence (IJCAI). Mexico. 2003. Pages 1233-1238. [(PDF)](http://ldc.usb.ve/~bonet/reports/hdp.pdf)
- B. Bonet and H. Geffner. *Labeled RTDP: Improving the Convergence of Real-Time Dynamic Programming*. Proc. 13th Int. Conf. on Automated Planning and Scheduling (ICAPS). Italy. 2003. Pages 12-21. [(PDF)](http://ldc.usb.ve/~bonet/reports/lrtdp.pdf)











