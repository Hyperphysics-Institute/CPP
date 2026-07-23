#!/usr/bin/env python3
"""Machine-check of the 2786 prereg's internal consistency at freeze
(the 2785 D1 lesson: never assert a frozen constraint without checking it)."""
# 1. sliding-window cells: r_min >= 2*a_s per rung
rmins=[0.04,0.06,0.08,0.12,0.16,0.24]; rmaxs=[0.40,0.546,0.70,0.88]
for a_s in (0.04,0.02,0.01,0.005):
    valid=[rm for rm in rmins if rm>=2*a_s-1e-12]
    assert len(valid)>=3, (a_s,valid)
    print(f"a_s={a_s}: {len(valid)} valid r_min cells x {len(rmaxs)} r_max = {len(valid)*len(rmaxs)} map cells (all r_min>=2a_s)")
# 2. rung requirements at a_s <= 0.01: >=2 sizes AND >=2 independent chains
matrix={0.04:[(686,'A'),(686,'B'),(432,'S'),(1024,'L')],
        0.02:[(432,'CORE'),(686,20260805),(1024,20260806)],
        0.01:[(432,20260807),(432,20260808),(686,20260809),(1024,20260810)],
        0.005:[(432,20260811),(432,20260812),(686,20260813),(1024,20260814)]}
for a_s,ch in matrix.items():
    sizes=set(n for n,_ in ch)
    ok = (len(sizes)>=2 and len(ch)>=2) if a_s<=0.01 else True
    print(f"a_s={a_s}: {len(ch)} chains, sizes {sorted(sizes)} -> {'OK' if ok else 'VIOLATION'}")
    assert ok
# 3. seed collisions
new=[s for ch in matrix.values() for _,s in ch if isinstance(s,int)]+[20260803,20260804,20260815,20260816]
old=set(range(20260798,20260803))|{20260722,20260723}
assert len(new)==len(set(new)), "duplicate new seed"
assert not (set(new)&old), "collision with reserved block"
print(f"seeds: {len(new)} new, all unique, no collision with 20260798-802 / 20260722-3")
# 4. PR2 minimum ladder present
assert set(matrix.keys())>={0.04,0.02,0.01,0.005}
print("PR2 minimum ladder {0.04,0.02,0.01,0.005}: present")
print("FREEZE CONSISTENCY: ALL CHECKS PASS")
