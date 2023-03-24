

from search import *


# ______________________________________________________________________________
class CannibaliMissionari(Problem):

    def __init__(self, initial, goal=(0,0,3,3,1)): 
        super().__init__(initial, goal)

    def findMissRP(self,state):
        return state[0]

    def findCanRP(self,state):
        return state[1]

    def findMissRA(self,state):
        return state[2]

    def findCanRA(self,state):
        return state[3]
    
    def posB(self,state):
        return state[4]
        
        

    

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['spostamissionarioDX','spostaduemissionariDX','spostacannibaleDX','spostaduecannibaliDX','spostamissionarioecannibaleDX','spostamissionarioSX','spostaduemissionariSX','spostacannibaleSX','spostaduecannibaliSX','spostamissionarioecannibaleSX']
        

        if self.findMissRP(state)==self.findCanRP(state):
    
            possible_actions.remove('spostamissionarioDX')
            possible_actions.remove('spostaduemissionariDX')
            possible_actions.remove('spostacannibaleSX')
            possible_actions.remove('spostaduecannibaliSX')


        if self.findMissRP(state)==self.findCanRP(state)-1:
            
            possible_actions.remove('spostaduemissionariDX')
            possible_actions.remove('spostaduecannibaliSX')



        if self.findMissRA(state)==self.findCanRA(state):
            possible_actions.remove('spostacannibaleDX')
            possible_actions.remove('spostaduecannibaliDX')
            possible_actions.remove('spostamissionarioSX')
            possible_actions.remove('spostaduemissionariSX')

        if self.findMissRP(state)==self.findCanRP(state)-1:
            possible_actions.remove('spostaduemissionariSX')
            possible_actions.remove('spostaduecannibaliDX')



        if not self.posB:
            possible_actions = possible_actions[:6]
        else:
            possible_actions = possible_actions[7:]
            


        return possible_actions


    



    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        #blank = self.find_blank_square(state)
        new_state = list(state)

        if action == "spostamissionarioDX" : 
             new_state[0]=new_state[0]-1
             new_state.inde[2]=new_state.index[2]+1
             new_state.index[4]=new_state.index[4]+1
            

        elif action == "spostaduemissionariDX" :
             new_state[0]=new_state[0]-2
             new_state[2]=new_state[2]+2
             new_state[4]=new_state[4]+1


        elif action == "spostacannibaleDX" :
             new_state[1]=new_state[1]-1
             new_state[3]=new_state[3]+1
             new_state[4]=new_state[4]+1

        elif action == "spostaduecannibaleDX" :
             new_state[1]=new_state[1]-2
             new_state[3]=new_state[3]+2
             new_state[4]=new_state[4]+1

        elif action == "spostamissionarioecannibaleDX" :
             new_state[0]=new_state[0]-1
             new_state[1]=new_state[1]-1
             new_state[2]=new_state[2]+1
             new_state[3]=new_state[3]+1
             new_state[4]=new_state[4]+1

        elif action == "spostamissionarioSX" : 
             new_state[0]=new_state[0]+1
             new_state[2]=new_state[2]-1
             new_state[4]=new_state[4]-1



        elif action == "spostaduemissionariSX" :
             new_state[0]=new_state[0]+2
             new_state[2]=new_state[2]-2
             new_state[4]=new_state[4]-1


        elif action == "spostacannibaleSX" :
            
             new_state[1]=new_state[1]+1
             new_state[3]=new_state[3]-1
             new_state[4]=new_state[4]+1
 
        elif action == "spostaduecannibaleSX" :
            
             new_state[1]=new_state[1]+2
             new_state[3]=new_state[3]-2
             new_state[4]=new_state[4]-1

        elif action == "spostamissionarioecannibaleSX" :
             new_state[0]=new_state[0]+1
             new_state[1]=new_state[1]+1
             new_state[2]=new_state[2]-1
             new_state[3]=new_state[3]-1
             new_state[4]=new_state[4]-1
            

        

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """

        return sum(self.state.index(0),self.state.index(1))/2
