import numpy as np
import math

def soyuz_FG(hypergolic,kerosene):
    alumina_emission = (hypergolic*1*0.001)+(kerosene*1*0.05)
    sulphur_emission = (hypergolic*0.7*0.001)+(kerosene*0.7*0.001)
    carbon_emission = (hypergolic*0.252*1)+(kerosene*0.352*1)+(hypergolic*0.378*1.57)+(kerosene*0.528*1.57)
    cfc_gases = (hypergolic*0.016*0.7)+(kerosene*0.016*0.7)+(hypergolic*0.003*0.7)+(kerosene*0.003*0.7)+(hypergolic*0.001*0.7)+(kerosene*0.001*0.7)
    particulate_matter = (hypergolic*0.001*0.22)+(kerosene*0.001*0.22)+(hypergolic*0.001*1)+(kerosene*0.05*1)
    photo_oxidation = (hypergolic*0.378*0.0456)+(kerosene*0.528*0.0456)+(hypergolic*0.001*1)+(kerosene*0.001*1)
    return {'Aluminium Oxides': alumina_emission, 'Sulphur Oxides': sulphur_emission, 'Carbon Oxides': carbon_emission, 'Cfc Gases': cfc_gases, 'Particulate Matter': particulate_matter, 'Photochemical Oxidation': photo_oxidation}

def falcon_9(kerosene):
    alumina_emission = (kerosene*0.05)
    sulphur_emission = (kerosene*0.001*0.7)
    carbon_emission = (kerosene*0.352*1)+(0.528*kerosene*1.57)
    cfc_gases = (kerosene*0.016*0.7)+(kerosene*0.003*0.7)+(kerosene*0.001*0.7)
    particulate_matter = (kerosene*0.001*0.22)+(kerosene*0.05*1)
    photo_oxidation = (kerosene*0.0456*0.528)+(kerosene*0.001*1)
    return {'Aluminium Oxides': alumina_emission, 'Sulphur Oxides': sulphur_emission, 'Carbon Oxides': carbon_emission, 'Cfc Gases': cfc_gases, 'Particulate Matter': particulate_matter, 'Photochemical Oxidation': photo_oxidation}
def falcon_heavy(kerosene):
    alumina_emission = (kerosene*0.05)
    sulphur_emission = (kerosene*0.001*0.7)
    carbon_emission = (kerosene*0.352*1)+(0.528*kerosene*1.57)
    cfc_gases = (kerosene*0.016*0.7)+(kerosene*0.003*0.7)+(kerosene*0.001*0.7)
    particulate_matter = (kerosene*0.001*0.22)+(kerosene*0.05*1)
    photo_oxidation = (kerosene*0.0456*0.528)+(kerosene*0.001*1)
    return {'Aluminium Oxides': alumina_emission, 'Sulphur Oxides': sulphur_emission, 'Carbon Oxides': carbon_emission, 'Cfc Gases': cfc_gases, 'Particulate Matter': particulate_matter, 'Photochemical Oxidation': photo_oxidation}