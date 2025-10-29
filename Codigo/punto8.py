class DFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def validate(self, string):
        state = self.q0
        for symbol in string:
            if symbol not in self.Sigma:
                return False
            state = self.delta[state].get(symbol)
            if state is None:
                return False
        return state in self.F
        Q = ["q0", "q1","q2"]
Sigma = ["0", "1"]
delta = {
    "q0": {"1": "q1", "0": "q2"},
    "q1": {"0": "q1", "1": "q1"},
    "q2": {"0": "q2", "1": "q2"}
}
q0 = "q0"
F = ["q1"]

dfa = DFA(Q, Sigma, delta, q0, F)

test_strings = ["01", "10", "11010101", "101010101"]
for s in test_strings:
    result = "ACCEPTED" if dfa.validate(s) else "REJECTED"
    print(f"{s}: {result}")