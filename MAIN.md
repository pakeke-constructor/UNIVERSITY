

#  To create a new github repo:


git init -b origin
git remote add origin https://github.com/<github-username>/<repo-name>


# to commit to existing repo :: 

git add .
git commit -m "commit message"
git push origin main
```py

def top_sort(adj_list):
    T = []
    Z = []
    In = {}
    for v in RL(adj_list):
        In[v] = 0
    
    for v in RL(adj_list):
        for u, w in adj_list[v]:
            In[v] += 1

    for v in RL(adj_list):
        if In[v] == 0:
            Z.append(v)

    while len(Z) > 0:
        v = Z.pop()
        T.append(v)
        for u,w in adj_list[v]:
            In[u] -= 1
            if In[u] == 0:
                Z.append(u)
    return T



```
