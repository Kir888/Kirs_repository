obh_in_cl = ("camera","table","light","laptop","screen")
t1, *t2, t3 = obh_in_cl
print(f"value is{t1} and", type(t1))
print(f"value is{t2} and", type(t2))
print(f"value is{t3} and", type(t3))
print(obh_in_cl.index("camera"))