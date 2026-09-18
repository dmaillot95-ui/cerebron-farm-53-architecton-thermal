import json,math,pathlib
# 1-D steady conduction through a slab: Q=k*A*dT/L
k=10.0; A=2.0; dT=50.0; L=0.5
q=k*A*dT/L
R=L/(k*A)
passed=math.isclose(q,2000.0,rel_tol=1e-12) and math.isclose(R,0.025,rel_tol=1e-12)
out={"benchmark":"steady_1d_fourier_conduction","engine":"PY-THERMAL-MVP","heat_rate_w":q,"thermal_resistance_k_per_w":R,"passed":passed,"evidence_level":"E2","limitations":["closed-form benchmark","not numerical thermal field simulation","not physical test"]}
pathlib.Path("artifacts").mkdir(exist_ok=True)
pathlib.Path("artifacts/thermal_mvp.json").write_text(json.dumps(out,indent=2),encoding="utf-8")
print(json.dumps(out,indent=2)); raise SystemExit(0 if passed else 1)
