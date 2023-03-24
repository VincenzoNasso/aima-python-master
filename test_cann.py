

from CannibaliProblem import *

import matplotlib.pyplot as plt
import random
import heapq
import math
import sys
from collections import defaultdict, deque, Counter
from itertools import combinations
from search import *

p = CannibaliMissionari(initial=(3,3,0,0,0))

nodo = breadth_first_tree_search(p)


print(nodo)
#solution(nodo)


#for s in path_states(breadth_first_graph_search(p)):
 #   print(board8(s))