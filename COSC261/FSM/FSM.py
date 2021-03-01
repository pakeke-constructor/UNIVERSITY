

'''

FSM simulator.












'''


class FSM:
    def __init__(self, alphabet : set(), states : {str : {str : [str]}}, start_state):  
        self.states = states
        self.alphabet = alphabet
        self.current_state = start_state
        self.start_state = start_state
        
        assert type(alphabet) == set, "alphabet gotta be a set"

        for state, hasher in states.items():
            for alp, new_state in hasher.items():
                if alp not in alphabet:
                    raise ValueError("unexpected char in state:  " + str(alp))
            if state not in self.states:
                raise ValueError("unexpected state:  " + str(state))
        
    def get(self, char):
        return self.states[self.current_state][char]

    def run(self, string):
        if len(string) == 0:
            return self.current_state
        self.current_state = self.get(string[0])
        return self.run(string[1:])
    
    def prun(self, string):
        self.reset()
        result = self.run(string)
        print(result)
        return result
    
    def reset(self):
        self.current_state = self.start_state


def test():
    f = FSM(
        set(['0','1']),
        {
            'q0' : {'0':'q1', '1':'q3'},
            'q1' : {'0':'q2', '1':'q0'},
            'q2' : {'0':'q2', '1':'q2'},
            'q3' : {'0':'q0', '1':'q2'}
        },
        'q0'
    )
    ctr = 0
    for i in range(6):
        for e in all_strings(['0','1'], i):
            if f.prun(e) == 'q0':
                ctr += 1
    
    assert ctr == 7, "??"
    print(ctr)
    




