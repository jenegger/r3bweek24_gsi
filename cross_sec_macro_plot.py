#!/bin/python3
import matplotlib.pyplot as plt
import pandas as pd
class cross_sec_block:
    def __init__(self):
        self.c_54 = pd.DataFrame()
        self.c_1086 = pd.DataFrame()
        self.c_2198 = pd.DataFrame()
        self.content = pd.DataFrame()
        self.eol_theory = pd.DataFrame()
        self.eol_corr_theory = pd.DataFrame()
    def read_file(self,filename):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.content = pd.read_csv(filename,sep='\t',header=None)
                print(self.content)
                self.content.columns = ["datatype","targettype","RunID","energy","cross_section","stat_error_cross_sec"]
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")

    def sort(self):
        self.c_54 = self.content.loc[(self.content["targettype"] == "c_54")]
        self.c_1086 = self.content.loc[(self.content["targettype"] == "c_1086")]
        #self.c_1086["energy"] = self.c_1086["energy"] -2;
        self.c_1086["energy"] = self.c_1086["energy"] - 2
        #self.c_1086["energy"] = self.c_1086["energy"] ;
        self.c_2198 = self.content.loc[(self.content["targettype"] == "c_2198")]
        self.c_2198["energy"] = self.c_2198["energy"] -4;
        self.eol_theory = self.content.loc[(self.content["targettype"] == "eol")]
        self.eol_corr_theory = self.content.loc[(self.content["targettype"] == "eol_corr")]
        #self.c_2198["energy"] = self.c_2198["energy"] ;


#cross_sec_tof_hit = cross_sec_block()
#cross_sec_tof_hit.read_file("out_wed_comb_with_tof.txt")
#cross_sec_tof_hit.sort()
#fig,ax = plt.subplots()
#cross_sec_tof_hit.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='green',label="c_54 SofTofWSingleTcalData events_only",marker="o")
#cross_sec_tof_hit.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='green',label="c_1086 SofTofWSingleTcalData events_only",marker="s")
#cross_sec_tof_hit.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='green',label="c_2198 SofTofWSingleTcalData events_only",marker="^")
#
#plt.show()

#the ones I don't touch:
#charge changing cross section
cross_sec_by_hand_no_tof = cross_sec_block()
cross_sec_by_hand_no_tof.read_file("/home/tobiasjenegger/r3bweek_2024_gsi/out_bgauss_combined_3_5sigma_with_lines_mixed_target_thickn_reduced.txt")
cross_sec_by_hand_no_tof.sort()

#my reaction cross section

#now as before with 12cuts and fixed on empty, but now new emtpy run (187)
cross_sec_mw12_cut_newempty400 = cross_sec_block()
cross_sec_mw12_cut_newempty400.read_file("/home/tobiasjenegger/r3bweek_2024_gsi/out_combined_reac_with_mw12_cut_other400empty_reduced.txt")
cross_sec_mw12_cut_newempty400.sort()


##reaction cross section from lukas ponnath
cross_sec_reac_lukas = cross_sec_block()
cross_sec_reac_lukas.read_file("/home/tobiasjenegger/r3bweek_2024_gsi/out_reaction_lukas_ponnath.txt")
cross_sec_reac_lukas.sort()

#eol theory
cross_sec_eol_theory = cross_sec_block()
cross_sec_eol_theory.read_file("/home/tobiasjenegger/r3bweek_2024_gsi/out_eol.txt")
cross_sec_eol_theory.sort()
print(cross_sec_eol_theory.eol_theory)
#eol theory corrected
cross_sec_eol_theory_corr = cross_sec_block()
cross_sec_eol_theory_corr.read_file("/home/tobiasjenegger/r3bweek_2024_gsi/out_eol_corr.txt")
cross_sec_eol_theory_corr.sort()

##---END of the important ones....----

#setup cross section charge_changing (empty target runs)
#also uses new run for 400 amev empty run
charge_changing_empty_runs = cross_sec_block()
charge_changing_empty_runs.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_correct_empty.txt")
charge_changing_empty_runs.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0 cut
cross_sec_mw12_cut_newempty400_notpat = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_correct_comb_reac_no_tpat.txt")
cross_sec_mw12_cut_newempty400_notpat.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0 cut and all 16 anodes hit
cross_sec_mw12_cut_newempty400_notpat_all16anodes = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_all16anodes.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_charge_changing_all16anodes.txt")
cross_sec_mw12_cut_newempty400_notpat_all16anodes.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0 cut and more than 12 anodes hit
cross_sec_mw12_cut_newempty400_notpat_more12anodes = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_more12anodes.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_corr_reac_morethan12anodes.txt")
cross_sec_mw12_cut_newempty400_notpat_more12anodes.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0 cut and more than 4  anodes hit
cross_sec_mw12_cut_newempty400_notpat_more4anodes = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_more4anodes.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_corr_reac_more_than4anodes.txt")
cross_sec_mw12_cut_newempty400_notpat_more4anodes.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0 cut and all 16 anodes hit, only for empty runs
cross_sec_mw12_cut_newempty400_notpat_all16anodes_empty = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_all16anodes_empty.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_corr_charge_changing_all_anodes_empty.txt")
cross_sec_mw12_cut_newempty400_notpat_all16anodes_empty.sort()


#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0 cut and without 1 and 13 anode
cross_sec_mw12_cut_newempty400_notpat_no_anode1_13 = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_no_anode1_13.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_comb_corr_charge_changin_no_1_13_notpat.txt")
cross_sec_mw12_cut_newempty400_notpat_no_anode1_13.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0 cut and without 1 and 13 anode plot 1-9 and 10to 16
cross_sec_mw12_cut_newempty400_notpat_no_anode1_13_other_twim = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_no_anode1_13_other_twim.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_comb_corr_notpat_no1_16_otherup_down.txt")
cross_sec_mw12_cut_newempty400_notpat_no_anode1_13_other_twim.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0 cut and without 1 and 13 anode plot 1-9 and 10to 16 3.7 sigma
cross_sec_mw12_cut_newempty400_notpat_no_anode1_13_other_twim_37_sigma = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_no_anode1_13_other_twim_37_sigma.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_comb_corr_3_7_sigma_no1_13.txt")
cross_sec_mw12_cut_newempty400_notpat_no_anode1_13_other_twim_37_sigma.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0 cut and without 1 and 13 and 16 anode plot 1-9 and 10to 16 3.7 sigma
cross_sec_mw12_cut_newempty400_notpat_no_anode1_13_16_other_twim_37_sigma = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_no_anode1_13_16_other_twim_37_sigma.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_comb_reaction_threeless_anodes_3_7sigma.txt")
cross_sec_mw12_cut_newempty400_notpat_no_anode1_13_16_other_twim_37_sigma.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0  and events with multi hit in twim are discarted...
cross_sec_mw12_cut_newempty400_notpat_no_multihit_twim = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_no_multihit_twim.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_combined_no_multihit.txt")
cross_sec_mw12_cut_newempty400_notpat_no_multihit_twim.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0  and 0.8sigma cut on mw0 xy 
cross_sec_mw12_cut_newempty400_notpat_no_strict_mw0_cut = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_no_strict_mw0_cut.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_combined_xy_08_sigma_cut.txt")
cross_sec_mw12_cut_newempty400_notpat_no_strict_mw0_cut.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0  and 1.25sigma cut on mw0 xy 
cross_sec_mw12_cut_newempty400_notpat_125_sigma_mw0_cut = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_125_sigma_mw0_cut.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_combined_xy_08_sigma_cut.txt")
cross_sec_mw12_cut_newempty400_notpat_125_sigma_mw0_cut.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0  but with sqrt(E) instead of E for charge
cross_sec_mw12_cut_newempty400_notpat_sqrt_charge = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_sqrt_charge.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_combined_sqrt.txt")
cross_sec_mw12_cut_newempty400_notpat_sqrt_charge.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0  but without the lines wher UP or DOWN charge is 0
cross_sec_mw12_cut_newempty400_notpat_no_line = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_no_line.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_combined_no_line_3_5_sigma_check.txt")
cross_sec_mw12_cut_newempty400_notpat_no_line.sort()

#now same conditions as in cross_sec_mw12_cut_newempty400, but without tpat > 0 and 4*sigma cut 
cross_sec_mw12_cut_newempty400_notpat_4sigma_cut = cross_sec_block()
cross_sec_mw12_cut_newempty400_notpat_4sigma_cut.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_combined_4sigma_with_lines.txt")
cross_sec_mw12_cut_newempty400_notpat_4sigma_cut.sort()

#charge changing cross section, but now with geometric correction,first try
cross_sec_charge_geom_corr = cross_sec_block();
cross_sec_charge_geom_corr.read_file("/home/tobiasjenegger/jupy/python_macros/cross_sections_sophisticated/reaction_cross_sec_dir/out_charge_changin_with_geo_corr.txt")
cross_sec_charge_geom_corr.sort();

#by hand calculated reaction cross section, but now with geometric correction, first try
reac_cross_sec_charge_geom_corr = cross_sec_block();
reac_cross_sec_charge_geom_corr.read_file("/home/tobiasjenegger/r3bweek_2024_gsi/out_example_corr.txt")
reac_cross_sec_charge_geom_corr.sort();

fig,ax = plt.subplots()
#BEGIN OF GOOD PLOTS ------------------------------
cross_sec_by_hand_no_tof.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_54 charge changing",marker="o",alpha=1)
cross_sec_by_hand_no_tof.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_1086 charge changing",marker="s",alpha=1)
cross_sec_by_hand_no_tof.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_2198 charge changing",marker="^",alpha=1)


cross_sec_mw12_cut_newempty400.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='forestgreen',label="c_54 reaction",marker="o",alpha=1)
cross_sec_mw12_cut_newempty400.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='forestgreen',label="c_1086 reaction",marker="s",alpha=1)
cross_sec_mw12_cut_newempty400.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='forestgreen',label="c_2198 reaction",marker="^",alpha=1)


cross_sec_reac_lukas.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='limegreen',label="c_54 reaction L. Ponnath",marker="o",alpha=1)
cross_sec_reac_lukas.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='limegreen',label="c_1086 reaction L. Ponnath",marker="s",alpha=1)
cross_sec_reac_lukas.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='limegreen',label="c_2198 reaction L. Ponnath",marker="^",alpha=1)


cross_sec_eol_theory.eol_theory.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='black',label="Glauber",marker="o",alpha=1)
cross_sec_eol_theory_corr.eol_corr_theory.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='red',label="Glauber (Coulomb,Pauli)",marker="d",alpha=1)

#END OF GOOD PLOTS--------------------------

#cross_sec_mw12_cut_newempty400_notpat.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='pink',label="c_54 notpat",marker="o",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='pink',label="c_1086 notpat",marker="s",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='pink',label="c_2198 notpat",marker="^",alpha=1)

#cross_sec_mw12_cut_newempty400_notpat_all16anodes.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='olive',label="c_54 all 16 anodes",marker="o",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_all16anodes.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='olive',label="c_1086 all 16 anodes",marker="s",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_all16anodes.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='olive',label="c_2198 all 16 anodes",marker="^",alpha=1)

#cross_sec_mw12_cut_newempty400_notpat_more12anodes.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='orange',label="c_54 all >12 anodes",marker="o",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_more12anodes.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='orange',label="c_1086 >12 anodes",marker="s",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_more12anodes.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='orange',label="c_2198 >12 anodes",marker="^",alpha=1)

#cross_sec_mw12_cut_newempty400_notpat_more4anodes.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_54 all >4 anodes",marker="o",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_more4anodes.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_1086 >4 anodes",marker="s",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_more4anodes.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_2198 >4 anodes",marker="^",alpha=1)

#charge_changing_empty_runs.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='black',label="empty charge changing",marker="X",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_all16anodes_empty.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='black',label="empty charge changing,all anodes",marker="X",alpha=1)
#cross_sec_setup.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='black',label="c_1086 no tpat",marker="s",alpha=1)
#cross_sec_setup.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='black',label="c_2198 no tpat",marker="^",alpha=1)

#cross_sec_mw12_cut_newempty400_notpat_no_anode1_13_16_other_twim_37_sigma.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_54 charge changing no1/13/16 other corr 3.7sigma",marker="o",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_no_anode1_13_16_other_twim_37_sigma.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_1086 charge changing no1/13/16 other corr 3.7sigma",marker="s",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_no_anode1_13_16_other_twim_37_sigma.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_2198 charge changing no1/13/16other corr 3.7sigma",marker="^",alpha=1)

#cross_sec_mw12_cut_newempty400_notpat_no_multihit_twim.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_54 charge changing no twim multihit",marker="o",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_no_multihit_twim.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_1086 charge changing no twim multihit",marker="s",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_no_multihit_twim.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_2198 charge changing no twim multihit",marker="^",alpha=1)


#cross_sec_charge_geom_corr.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_54 latest charge changing",marker="o",alpha=1)
#cross_sec_charge_geom_corr.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_1086 latest charge changing",marker="s",alpha=1)
#cross_sec_charge_geom_corr.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_2198 latest charge changing",marker="^",alpha=1)


reac_cross_sec_charge_geom_corr.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='orange',label="c_54 geom. corr",marker="o",alpha=1)
reac_cross_sec_charge_geom_corr.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='orange',label="c_1086 geom. corr.",marker="s",alpha=1)
reac_cross_sec_charge_geom_corr.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='orange',label="c_2198 geom. corr.",marker="^",alpha=1)



#cross_sec_mw12_cut_newempty400_notpat_no_strict_mw0_cut.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_54 charge changing strict mw0 cut",marker="o",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_no_strict_mw0_cut.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_1086 charge changing strict mw0 cut",marker="s",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_no_strict_mw0_cut.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_2198 charge changing strict mw0 cut",marker="^",alpha=1)


#cross_sec_mw12_cut_newempty400_notpat_125_sigma_mw0_cut.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_54 charge changing 1.25sigma mw0 cut",marker="o",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_125_sigma_mw0_cut.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_1086 charge changing 1.25sigma mw0 cut",marker="s",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_125_sigma_mw0_cut.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_2198 charge changing 1.25sigma mw0 cut",marker="^",alpha=1)


#cross_sec_mw12_cut_newempty400_notpat_sqrt_charge.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_54 charge changing sqrt charge",marker="o",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_sqrt_charge.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_1086 charge changing sqrt charge",marker="s",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_sqrt_charge.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_2198 charge changing sqrt charge",marker="^",alpha=1)


#cross_sec_mw12_cut_newempty400_notpat_no_line.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_54 charge changing no line",marker="o",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_no_line.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_1086 charge changing no line",marker="s",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_no_line.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_2198 charge changing no line",marker="^",alpha=1)


#cross_sec_mw12_cut_newempty400_notpat_4sigma_cut.c_54.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_54 charge changing 4sigma",marker="o",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_4sigma_cut.c_1086.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_1086 charge changing 4sigma",marker="s",alpha=1)
#cross_sec_mw12_cut_newempty400_notpat_4sigma_cut.c_2198.plot(kind='scatter',ax=ax,x= 'energy',y='cross_section',yerr="stat_error_cross_sec",color='blue',label="c_2198 charge changing 4sigma",marker="^",alpha=1)

plt.xlabel("Beam Energy [AMeV]", fontsize=16)
plt.ylabel("Cross Section [mbarn]", fontsize=16)
plt.legend(fontsize=6)
plt.grid(True,color = 'black', linestyle = '--', linewidth = 0.5,which="both")
plt.ylim(720,880)
#plt.show()
plt.savefig("charge_changing_cross_section_no_multihit_twim.png",dpi=300)
