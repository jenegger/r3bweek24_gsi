
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

bool trefs_existent = true;
if (tref_time_up == 0 || tref_time_down == 0) trefs_existent = false;

bool clean_twim_event = true;
for (int i = 0; i < 16; i++){
	if (vec_time2d[i][1] != 0) clean_twim_event = false;
	if (vec_time2d[i][0] == 0) clean_twim_event = false;
	}

if (clean_twim_event && trefs_existent){
for (int i = 0; i < 16; i++){
	if (i < 8) h1_twim_sec0_time_anode[i]->Fill(vec_time2d[i][0]-tref_time_up);
	else h1_twim_sec0_time_anode[i]->Fill(vec_time2d[i][0]-tref_time_down);
	}
}





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
