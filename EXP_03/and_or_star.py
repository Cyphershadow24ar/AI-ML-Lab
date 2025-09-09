
# AO* algorithm for AND–OR graphs
# ----- Step 1: AND–OR graph from your slide (unit edge cost = 1) -----
graph = {
    "A": [("OR",  [("B",1)]),         ("AND", [("C",1), ("D",1)])],
    "B": [("OR",  [("E",1)]),         ("OR",  [("F",1)])],
    "C": [("OR",  [("G",1)]),         ("AND", [("H",1), ("I",1)])],
    "D": [("OR",  [("J",1)])]
}

# ----- Step 2: heuristics h(n) (from your example) -----
h = {"A":6,"A":8,"B":5,"C":2,"D":4,"E":7,"F":9,"G":3,"H":0,"I":0,"J":0}

# ----- Step 3: AO* core: compute best cost + remember best choice ("policy") -----
policy = {}  # node -> ('OR' or 'AND', [chosen children])

def solve(n):
    if n not in graph:                 # terminal node: return its h(n)
        return h[n]
    best, best_choice = float("inf"), None
    for typ, succs in graph[n]:
        if typ == "OR":                # OR: pick one child
            s, c = succs[0]
            val = c + solve(s)
            choice = (typ, [s])
        else:                          # AND: must solve all children
            val = sum(c + solve(s) for s, c in succs)
            choice = (typ, [s for s, _ in succs])
        if val < best:
            best, best_choice = val, choice
    policy[n] = best_choice            # store chosen hyper-arc
    h[n] = best                        # optional: refine heuristic
    return best

# ----- Step 4: pretty-print the chosen AND–OR solution graph -----
def show(n, indent=0):
    if n not in policy:                # terminal
        return "  "*indent + n
    typ, kids = policy[n]
    if typ == "OR":
        s = "  "*indent + f"{n} → {kids[0]}\n"
        return s + show(kids[0], indent+1)
    else:  # AND
        s = "  "*indent + f"{n} → "+"{"+", ".join(kids)+"}\n"
        for k in kids:
            s += show(k, indent+1) + "\n"
        return s.rstrip()

# ----- Step 5: run from A -----
min_cost = solve("A")
print("Minimum cost from A:", min_cost)
print("\nChosen solution graph:")
print(show("A"))