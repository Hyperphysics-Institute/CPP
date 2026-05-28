import sympy as sp
phi = (1+sp.sqrt(5))/2
# Verified inner products (from registered primitives):
#   first shell:  V_i . v_host = phi/2     (G1)
#   second shell: W_j . v_host = 1/2       (G2, Patch 0587)
#   third shell:  v' . v_host = 1/(2 phi)  (G3, Coxeter)
# edge length 1/phi  => e_hat = phi*(endpoint2 - endpoint1); n_edge = phi*(V_1 - v_host)
# Additive constant = phi^2 * (start.v_host - end.v_host)

def constant(start_dot_host, end_dot_host):
    return sp.simplify(phi**2 * (start_dot_host - end_dot_host))

c_S1S2 = constant(phi/2, sp.Rational(1,2))      # S1->S2 cross-shell
c_S1S3 = constant(phi/2, 1/(2*phi))             # S1->S3 third-shell
print("S1->S2 additive constant:", sp.nsimplify(c_S1S2,[phi]), " (registered G2_E.3 says phi/2 =", float(phi/2),")  match:", sp.simplify(c_S1S2 - phi/2)==0)
print("S1->S3 additive constant:", sp.nsimplify(c_S1S3,[phi]), " (reverted P0605 used phi^2/2 =", float(phi**2/2),")  match:", sp.simplify(c_S1S3 - phi**2/2)==0)
