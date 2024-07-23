import pandas as pd

# Mettre le chemin de son fichier .csv Lazer
chemin_fichier = "Lazer-2024-07-23.csv"

#Chargement des données
data = pd.read_csv(chemin_fichier, low_memory=False)

#data cleaning:
#Supprimer les NaN
data = data.dropna()
# Supprimer les colonnes non utiles
colonnes_a_supprimer = [
    "03.deriv_adcs_and1_g", "03.deriv_adcs_and2_g", 
    "03.deriv_acc_Ayx_mdeg", "03.deriv_acc_Azx_mdeg",
    "04.deriv_adcs_and1_g", "04.deriv_adcs_and2_g",
    "04.deriv_acc_Ayx_mdeg", "04.deriv_acc_Azx_mdeg"
]

data = data.drop(columns=colonnes_a_supprimer)

#Convertir les valeurs avec K dasn les colonnes concernées:
def convert_k_to_value(s):
    if 'K' in s:
        return float(s.replace('K', '').strip()) * 1000
    return float(s)

cols_to_convert = ["01.sam_spd_mms","03.adcs_and1_g","03.adcs_and2_g","03.acc_Ayx_mdeg","03.acc_Azx_mdeg","04.adcs_and1_g","04.adcs_and2_g","04.acc_Ayx_mdeg","04.acc_Azx_mdeg"]
for col in cols_to_convert:
    data[col] = data[col].apply(convert_k_to_value)


# Renommer les colonnes avec des noms plus lisibles
noms_colonnes = {
    "01.sam_temp_degC": "temp_vent",
    "01.sam_dir_deg": "vent_direction",
    "01.sam_spd_mms": "vitesse_vent",
    "03.adcs_and1_g": "force_11",
    "03.adcs_and2_g": "force_12",
    "03.acc_T1_degC": "temp_1",
    "03.acc_Ayx_mdeg": "axe_y_1",
    "03.acc_Azx_mdeg": "axe_x_1",
    "04.adcs_and1_g": "force_21",
    "04.adcs_and2_g": "force_22",
    "04.acc_T1_degC": "temp_2",
    "04.acc_Ayx_mdeg": "axe_y_2",
    "04.acc_Azx_mdeg": "axe_x_2"
}

data.rename(columns=noms_colonnes, inplace=True)

#Exportez son nouveau fichier csv, Mettre le chemin où l'on souhaite le déposer.
chemin_fichier = r"C:\Users\hadri\Documents\MLE\projet hélioslite\lazer_bi.csv"
data.to_csv(chemin_fichier, index=False)
