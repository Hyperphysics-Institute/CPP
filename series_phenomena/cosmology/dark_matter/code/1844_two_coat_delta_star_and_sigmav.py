import numpy as np
a=2.0; E_ee=0.9
q1=np.array([+1,-1,+1,-1]); p1=np.array([[0,0,0],[a,0,0],[a,a,0],[0,a,0]],float)
def Esum(delta, shift):
    # second face: same alternating pattern, laterally shifted by 'shift'=(sx,sy), at height delta
    q2=q1.copy(); p2=p1.copy()+np.array([shift[0],shift[1],delta])
    E=0.0
    for i in range(4):
        for j in range(4):
            E+=q1[i]*q2[j]/np.linalg.norm(p1[i]-p2[j])
    return E*E_ee*a   # MeV
print("PART B (fixed) -- registry-AVERAGED two-coat interaction over continuous lateral offset:")
grid=np.linspace(0,a,9)
print(f"{'delta(fm)':>10}{'<E> reg-avg':>13}{'min(attract)':>14}{'max(barrier)':>14}")
for d in (1.0,1.5,2.0,3.0):
    vals=[Esum(d,(sx,sy)) for sx in grid for sy in grid]
    print(f"{d:>10.1f}{np.mean(vals):>13.3f}{np.min(vals):>14.3f}{np.max(vals):>14.3f}")
# operative barrier: registry-averaged, contact vs far
bar_avg=np.mean([Esum(1.0,(sx,sy)) for sx in grid for sy in grid]) - np.mean([Esum(4.0,(sx,sy)) for sx in grid for sy in grid])
print(f"\nregistry-averaged barrier (1->4 fm): {bar_avg:.3f} MeV   vs single-coat scale E_ee={E_ee:.2f} MeV")
print(f"  ratio to single-coat: {bar_avg/E_ee:.2f}  -> operative v_thr shift ~ sqrt = {np.sqrt(abs(bar_avg)/E_ee):.2f}x")
print("  Plus: coats can RELAX toward the attractive registry as they approach (min row above is")
print("  strongly attractive), which would AID penetration -> v_thr <= single-coat, not higher.")
print("  CONCLUSION: two-coat barrier is a NEAR-CANCELLATION residual, ~<= single-coat, NOT ~2x.")
print("  The earlier sqrt(2) 'doubling' estimate is RETRACTED; v_thr is comparable-or-lower, so")
print("  penetration/catch is at least as easy as the single-coat model assumed (favorable).")

print("\n"+"="*64)
print("PART C -- sigma/m(v): the two competing velocity effects, reported straight")
print("="*64)
# Two effects:
#  (i) accumulated self-limiting: high-v environments -> more catches over time -> shorter N -> lower sigma_geo/m.
# (ii) per-encounter transport eps(v): higher v -> more catches now -> more momentum transfer -> higher eps.
# They OPPOSE. Net sign = which dominates. Model both simply and report.
K=0.013  # cm^2/g per element (1842)
def Nbar(v, Nform=200, floor=0.25):  # accumulated fusion: N falls toward a self-limiting floor with v
    # more catches at high v -> more shortening; crude: N/Nform = floor + (1-floor)/(1+(v/vc)^2)
    vc=800.0
    return Nform*(floor+(1-floor)/(1+(v/vc)**2))
def eps(v, vthr=1200.0):  # per-encounter transport: rises from bounce-floor to 1 across vthr
    bounce_floor=0.35
    return bounce_floor+(1-bounce_floor)/(1+(vthr/max(v,1))**2)
print(f"{'v(km/s)':>9}{'Nbar':>8}{'sigma_geo/m=K*N':>16}{'eps(v)':>8}{'sigma/m=K*N*eps':>16}")
for v in (50,150,500,1000,2000,3600):
    N=Nbar(v); sg=K*N; e=eps(v); sm=sg*e
    print(f"{v:>9}{N:>8.0f}{sg:>16.2f}{e:>8.2f}{sm:>16.2f}")
print("\nHONEST FINDING: the two effects OPPOSE. Self-limiting (N falls with v) pushes sigma/m DOWN")
print("with v (observed direction); per-encounter eps (more catches at high v) pushes it UP. In this")
print("crude model the self-limiting wins at low v (dwarf high) but eps flattens/reverses the high-v")
print("tail -- so the curve can be non-monotonic unless self-limiting dominates. The DIRECTION is NOT")
print("guaranteed falling by the mechanism alone; it depends on the self-limiting floor vs the bounce")
print("transfer fraction. This is a real tension the two-coat/transport refinement SURFACES, not hides.")
