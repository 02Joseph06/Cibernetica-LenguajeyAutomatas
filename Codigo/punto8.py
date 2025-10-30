class DFA:
    def _init_(self, Q, Sigma, delta, q0, F):
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

Q = ["q0", "q1", "q2", "q3"]
Sigma = ["a", "b"]
delta = {
    "q0": {"a": "q1", "b": "q1"},
    "q1": {"a": "q2", "b": "q2"},
    "q2": {"a": "q3", "b": "q3"},
    "q3": {"a": "q0", "b": "q0"}
}
q0 = "q0"
F = ["q3"]

dfa = DFA(Q, Sigma, delta, q0, F)

test_strings = ["aabab", "bab", "bba", "aaa","bbb"]
for s in test_strings:
    result = "ACCEPTED" if dfa.validate(s) else "REJECTED"
    print(f"{s}: {result}")