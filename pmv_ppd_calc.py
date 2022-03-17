from pythermalcomfort.models import pmv_ppd
from pythermalcomfort.utilities import v_relative, clo_dynamic
#from pythermalcomfort.utilities import met_typical_tasks
from pythermalcomfort.utilities import clo_individual_garments

#input variables 
tdb = -18 #dry-bulb air temp
tr =10  #mean radiant temperature 
v = 0.1 #average air speed
rh = 50 #relative humidity

met= 1

icl = 0.5 #clothing insulation (summer clothing ~0.5)

vr = v_relative(v=v, met=met)

clo = clo_dynamic(clo=icl, met=met)

#calculate PMV in accordance with AHRAE55
results = pmv_ppd(tdb=tdb, tr=tr, vr=vr,rh=rh,met=met, clo=clo,standard="ASHRAE")

print(results)

#print PMV values
print(f"pmv = {results['pmv']}, ppd={results['ppd']}%")
