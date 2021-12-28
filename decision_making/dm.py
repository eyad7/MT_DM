from scikitmcda.topsis import TOPSIS
from scikitmcda.wsm import WSM
from scikitmcda.wpm import WPM
from scikitmcda.waspas import WASPAS
from scikitmcda.promethee_ii import PROMETHEE_II
from scikitmcda.electre_i import ELECTRE_I
#from scikitmcda.electre_i import ELECTRE_II
from scikitmcda.vikor import VIKOR
from scikitmcda.constants import MAX, MIN, LinearMinMax_, LinearMax_, LinearSum_, Vector_, EnhancedAccuracy_, Logarithmic_ 
from scikitmcda.dmuu import DMUU
# Example for TOPSIS

def decision_making(values,alternatives,field_names, method):
    file=open('calculation.html','w')
    file2=open('result.html','w')
    if method == 'topsis':
        topsis = TOPSIS()
        topsis.dataframe(values,alternatives,field_names)
    elif method=='minimax_regret':
        dmuu = DMUU()
        dmuu.dataframe(values,alternatives,field_names)
        dmuu.minimax_regret()
        file.write(dmuu.pretty_calc(tablefmt='html'))
        file2.write(dmuu.pretty_decision(tablefmt='html'))
    elif method=='maximin':
        dmuu = DMUU()
        dmuu.dataframe(values,alternatives,field_names)
        dmuu.maximin()
        file.write(dmuu.pretty_calc(tablefmt='html'))
        file2.write(dmuu.pretty_decision(tablefmt='html'))
    elif method=='maximax':
        dmuu = DMUU()
        dmuu.dataframe(values,alternatives,field_names)
        dmuu.maximax()
        file.write(dmuu.pretty_calc(tablefmt='html'))
        file2.write(dmuu.pretty_decision(tablefmt='html'))
    file.close()
    file2.close()




#print(dmuu.pretty_calc())
#print(dmuu.pretty_decision())
# dmuu.decision_making([dmuu.maximax(), dmuu.maximin(), dmuu.hurwicz(0.8), dmuu.minimax_regret()])

# #print(dmuu.pretty_calc())
# #print(dmuu.pretty_decision())

# print(dmuu.pretty_calc(tablefmt='html'))