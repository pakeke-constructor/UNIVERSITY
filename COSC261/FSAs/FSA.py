

'''

FSA simulator.
What are FSA's?
(see DFSA.md)

'''

RL = lambda x: range(len(x))


class FSA:
    def __init__(self, alphabet : set(), states : {str : {str : str}}, start_state, accept_states):  
        self.states = states
        self.alphabet = alphabet
        self.current_state = start_state
        self.start_state = start_state
        self.accept_states = accept_states
        
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

    def show(self):
        print("\n")
        for statename, dic in self.states.items():
            st = ''
            for k,v in dic.items():
                st += f'     {k} : {v}\n' 
            print(f"{statename}  =>  \n{st}\n")
        print()

    @staticmethod
    def gen_ar(states, accept_states):
        ar = []
        state_ar = []
        length = len(states)
        for i in range(length):
            ar.append( [True] * length )
        
        state_ar = list(states.keys())
        state_hash = dict()
        for i,e in enumerate(state_ar):
            state_hash[e] = i

        max_ = 0
        for x in range(len(ar)):
            for y in range(max_):
                if state_ar[x] in accept_states or state_ar[y] in accept_states:
                    ar[x][y] = 0  # This pair has a final state
                else:
                    ar[x][y] = (state_ar[x], state_ar[y])
            max_ += 1
        
        return ar, state_hash, state_ar

    def check_m(self, ar, hsh, a,b):
        '''
        checks if a,b should be marked
        '''
        aar = []
        bar = []

        for alp in self.alphabet:
            aar.append(self.states[a][alp])
            bar.append(self.states[b][alp])
        
        tups = zip(aar, bar)

        for q,w in tups:
            i1 = hsh[q]
            i2 = hsh[w]
            if (not ar[i1][i2]):
                return True # yup should be marked
        return False

    def minimize(self):
        enum = enumerate
        ar, hsh, st_ar = self.gen_ar(self.states, self.accept_states)
        rep = True
        while rep:
            rep = False
            for x,nest in enum(ar):
                for y,v in enum(nest):
                    if type(v) == tuple:
                        a, b = v
                        if self.check_m(ar, hsh, a,b):
                            # then mark as checked
                            rep = True
                            ar[x][y] = 0

        for x in RL(ar):
            for y in RL(ar[x]):
                if ar[x][y] and (ar[x][y] is not True):
                    rep = True
                    print(f"({st_ar[x], st_ar[y]}) should be minimized.")
                    ar[x][y] = True


def test():
    f = FSA(
        set(['0','1']),
        {
            '0' : {'0':'1','1':'2'},
            '1' : {'0':'2','1':'3'},
            '2' : {'0':'4','1':'0'},
            '3' : {'0':'1','1':'4'},
            '4' : {'0':'3','1':'5'},
            '5' : {'0':'3','1':'4'}
        },
        '0',
        '1'

    )
    #f.show()
    f.minimize()


test()

