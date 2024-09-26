
double ref_time_up = 0;
double ref_time_down = 0;
vector<vector<double> > vec_time2d(16,vector<double>(2,0.0)); 

for (int i = 0; i < entries_twim; i++){
	softwimmappeddata[i] = (R3BTwimMappedData*)TwimMappedData->At(i);
	Int_t twim_section = softwimmappeddata[i]->GetSecID();
	Int_t twim_anode = softwimmappeddata[i]->GetAnodeID();
	if (twim_section == 1 && twim_anode <= 16){
		if (vec_time2d[twim_anode-1][0] != 0 ){ //multihit event, fit second entry of vector
			vec_time2d[twim_anode-1][1] = softwimmappeddata[i]->GetTime();
			}
		else vec_time2d[twim_anode-1][0] = softwimmappeddata[i]->GetTime(); //first hit seen, but it to index 0
		
		}
	if (twim_anode == 17){
		if(twim_section == 1) tref_time_up = softwimmappeddata[i]->GetTime();
		if(twim_section == 2) tref_time_down = softwimmappeddata[i]->GetTime();
		}

	}








	first check that the anodeid is lower than 16	
	if lower
		if vec != 0:
			fill the second entry in the vector i 
		else fill the first entry in vector i
	if higher -> check section and fill then the trefs..
}

bool trefs_existent = false;
if (trefs exist) -> set to true

clean event = true
for (loop over vector)
	if second entry of vector != 0 -> clean event = false
	if first entry of vector == 0 -> clean event false

if (clean_event && trefs_existent)
	for loop:
		if i < 8
		h1_time_i = time_i - tref_up
		else:
		h1_time_i = time_i - tref_down
