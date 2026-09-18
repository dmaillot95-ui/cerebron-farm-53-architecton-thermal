import subprocess,sys,json,pathlib
r=subprocess.run([sys.executable,"worker/thermal_mvp.py"],check=False); assert r.returncode==0
x=json.loads(pathlib.Path("artifacts/thermal_mvp.json").read_text()); assert x["passed"] is True
