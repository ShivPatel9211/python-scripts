#!/usr/bin/python
# We can solve this problem either is declearing "betty_botter" as global varibale and commenting the local varible "betty_botter" in botter_betty() function or by simply returing local vaibale betty_botter from botter_betty() function.
import sys
betty_botter ='Betty Botter bought a bit of butter But the bit of butter Betty Botter bought was bitter So Betty ' \
'Botter bought a better bit of butter '
expected_output ='botter betty bought a bit of butter But the bit of butter botter betty bought was bitter So botter ' \
'betty bought a better bit of butter '
def botter_betty():
    # global betty_botter # global variable
    betty_botter = 'Betty Botter bought a bit of butter But the bit of butter Betty Botter bought was bitter So Betty ' \
    'Botter bought a better bit of butter '
    betty_botter = betty_botter.replace('Botter', 'betty')
    betty_botter = betty_botter.replace('Betty', 'botter')
    return betty_botter
def main(args):
    betty_botter=botter_betty()
    assert betty_botter== expected_output, "Failed"
    print ("Success")
if __name__ == '__main__':
    main(sys.argv)