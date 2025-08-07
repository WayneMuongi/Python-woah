def sum(*args):
    ans=0
    for w in args:
        print(f"{ans} = {ans} + {w}")
        ans=ans+w
    
    print("ANS IS",ans)
    return ans

sum(200,3000,40000,9000)