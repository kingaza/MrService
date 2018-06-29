## story_001
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heating"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "RF Amplifier"}
 - slot{"error": "RF Amplifier"}
 - utter_ask_patientheight
* inform{"patient_height": 1.8}
 - slot{"patient_height": 1.8}  
 - utter_ask_patientweight
* inform{"patient_weight": 75} 
 - slot{"patient_weight": 75} 
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_002
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heat"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "RF Meter"}
 - slot{"error": "RF Meter"}
 - utter_ask_patientweight
* inform
 - slot{"patient_weight": 75} 
 - utter_ask_patientheight
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7}
 - utter_ask_examtime
* inform{"exam_time": 800} 
 - slot{"exam_time": 800} 
 - utter_ask_examsed
* inform{"exam_sed": 1200} 
 - slot{"exam_sed": 1200}
 - utter_ask_moreupdates
* inform{"patient_height": 1.75} 
 - slot{"patient_height": 1.75} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_003
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heating"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_patientheight
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7}
 - utter_ask_patientweight
* inform{"patient_weight": 70} 
 - slot{"patient_weight": 70}
 - utter_ask_examtime
* inform{"exam_time": 1200} 
 - slot{"exam_time": 1200}
 - utter_ask_examsed
* inform{"exam_sed": 2000} 
 - slot{"exam_sed": 2000}
 - utter_ask_moreupdates
* inform{"patient_weight": 80}  
 - slot{"patient_weight": 80}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_004
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heating"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye 

## story_005
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye  

## story_006
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heating"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "RF Amplifier"}
 - slot{"error": "RF Amplifier"}
 - utter_ask_examsed
* inform{"exam_sed": 2500} 
 - slot{"exam_sed": 2500} 
 - utter_ask_examtime
* inform{"exam_time": 1200} 
 - slot{"exam_time": 1200}
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8}
 - utter_ask_moreupdates
* inform{"patient_weight": 120}  
 - slot{"patient_weight": 120}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye   

## story_007
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"burning"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_haserror
* inform{"error": "RF Meter"}
 - slot{"error": "RF Meter"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye   

## story_008
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heating"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_haserror
* inform{"error": "RF Amplifier"}
 - slot{"error": "RF Amplifier"}
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8}
 - utter_ask_patientweight
* inform{"patient_weight": 80} 
 - slot{"patient_weight": 80} 
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_009
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heating"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_haserror
* inform{"error": "RF Meter"}
 - slot{"error": "RF Meter"}
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_patientweight
* inform{"patient_weight": 75} 
 - slot{"patient_weight": 75}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_examtime
* inform{"exam_time": 800} 
 - slot{"exam_time": 800} 
 - utter_ask_examsed
* inform{"exam_sed": 1200} 
 - slot{"exam_sed": 1200}
 - utter_ask_moreupdates
* inform{"patient_height": 1.75} 
 - slot{"patient_height": 1.75} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_010
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heat"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_patientheight
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7}
 - utter_ask_patientweight
* inform
 - slot{"patient_weight": 70} 
 - utter_ask_examtime
* inform{"exam_time": 1200} 
 - slot{"exam_time": 1200} 
 - utter_ask_examsed
* inform{"exam_sed": 2000} 
 - slot{"exam_sed": 2000} 
 - utter_ask_moreupdates
* inform{"patient_weight": 80}  
 - slot{"patient_weight": 80}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_011
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heat"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900}
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye 

## story_012
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heating"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900}
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye  

## story_013
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heating"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_haserror
* inform{"error": "RF Amplifier"}
 - slot{"error": "RF Amplifier"}
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_examsed
* inform{"exam_sed": 2500} 
 - slot{"exam_sed": 2500}
 - utter_ask_examtime
* inform{"exam_time": 1000} 
 - slot{"exam_time": 1000} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8}
 - utter_ask_moreupdates
* inform{"patient_weight": 120}  
 - slot{"patient_weight": 120}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye   

## story_014
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"burn"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 110} 
 - slot{"patient_weight": 110} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye    

## story_015
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"burning"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 75} 
 - slot{"patient_weight": 75} 
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_016
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"burning"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "RF Meter"}
 - slot{"error": "RF Meter"}
 - utter_ask_patientweight
* inform{"patient_weight": 80} 
 - slot{"patient_weight": 80} 
 - utter_ask_patientheight
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7}
 - utter_ask_examtime
* inform{"exam_time": 800} 
 - slot{"exam_time": 800} 
 - utter_ask_examsed
* inform{"exam_sed": 1200} 
 - slot{"exam_sed": 1200}
 - utter_ask_moreupdates
* inform{"patient_height": 1.75} 
 - slot{"patient_height": 1.75} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_017
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"burning"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_patientheight
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7} 
 - utter_ask_patientweight
* inform{"patient_weight": 70} 
 - slot{"patient_weight": 70} 
 - utter_ask_examtime
* inform{"exam_time": 1200} 
 - slot{"exam_time": 1200} 
 - utter_ask_examsed
* inform{"exam_sed": 2000} 
 - slot{"exam_sed": 2000} 
 - utter_ask_moreupdates
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_018
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"burn"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientheight
* inform{"patient_height": 2.0} 
 - slot{"patient_height": 2.0} 
 - utter_ask_patientweight
* inform{"patient_weight": 120} 
 - slot{"patient_weight": 120}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye 

## story_019
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heat"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 2000} 
 - slot{"exam_sed": 2000} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye  

## story_020
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "RF Amplifier"}
 - slot{"error": "RF Amplifier"}
 - utter_ask_examsed
* inform{"exam_sed": 2500} 
 - slot{"exam_sed": 2500} 
 - utter_ask_examtime
* inform{"exam_time": 1200} 
 - slot{"exam_time": 1200}
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8}
 - utter_ask_moreupdates
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye   

## story_021
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"warm"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "RF Meter"}
 - slot{"error": "RF Meter"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye   

## story_022
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"error": "RF Amplifier"}
 - slot{"error": "RF Amplifier"}
 - utter_ask_patientheight
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror 
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 80} 
 - slot{"patient_weight": 80} 
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_moreupdates
* inform{"patient_height": 1.7}  
 - slot{"patient_height": 1.7}  
 - utter_ask_moreupdates 
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_023
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_haserror
* inform{"error": "RF Meter"}
 - slot{"error": "RF Meter"}
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_patientweight
* inform{"patient_weight": 75} 
 - slot{"patient_weight": 75} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_examtime
* inform{"exam_time": 800} 
 - slot{"exam_time": 800} 
 - utter_ask_examsed
* inform{"exam_sed": 1200} 
 - slot{"exam_sed": 1200}
 - utter_ask_moreupdates
* inform{"patient_height": 1.75} 
 - slot{"patient_height": 1.75} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_024
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_patientheight
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7} 
 - utter_ask_patientweight
* inform{"patient_weight": 70} 
 - slot{"patient_weight": 70} 
 - utter_ask_examtime
* inform{"exam_time": 1200} 
 - slot{"exam_time": 1200} 
 - utter_ask_examsed
* inform{"exam_sed": 2000} 
 - slot{"exam_sed": 2000} 
 - utter_ask_moreupdates
* inform{"patient_weight": 80}  
 - slot{"patient_weight": 80}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_025
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye 

## story_026
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"warm"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900}
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye  

## story_027
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heating"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - utter_ask_haserror
* inform{"error": "RF Amplifier"}
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_examsed
* inform{"exam_sed": 2500} 
 - slot{"exam_sed": 2500}
 - utter_ask_examtime
* inform{"exam_time": 1000} 
 - slot{"exam_time": 1000} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8}
 - utter_ask_moreupdates
* inform{"patient_weight": 120}  
 - slot{"patient_weight": 120}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye   

## story_028
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"warm"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 110} 
 - slot{"patient_weight": 110} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye     

 ## story_029
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heating"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "RF Amplifier"}
 - slot{"error": "RF Amplifier"}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 75} 
 - slot{"patient_weight": 75} 
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_moreupdates
* inform{"patient_height": 1.75}  
 - slot{"patient_height": 1.75}  
 - utter_ask_moreupdates 
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_030
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heating"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "RF Meter"}
 - slot{"error": "RF Meter"}
 - utter_ask_patientweight
* inform{"patient_weight": 75} 
 - slot{"patient_weight": 75} 
 - utter_ask_patientheight
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7} 
 - utter_ask_examtime
* inform{"exam_time": 800} 
 - slot{"exam_time": 800} 
 - utter_ask_examsed
* inform{"exam_sed": 1200} 
 - slot{"exam_sed": 1200}
 - utter_ask_moreupdates
* inform{"patient_height": 1.75} 
 - slot{"patient_height": 1.75} 
 - utter_ask_moreupdates
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_031
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heating"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_patientheight
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7}
 - utter_ask_patientweight
* inform{"patient_weight": 70} 
 - slot{"patient_weight": 70}
 - utter_ask_examtime
* inform{"exam_time": 1200} 
 - slot{"exam_time": 1200} 
 - utter_ask_examsed
* inform{"exam_sed": 2000} 
 - slot{"exam_sed": 2000} 
 - utter_ask_moreupdates
* inform{"patient_weight": 80}  
 - slot{"patient_weight": 80}  
 - utter_ask_moreupdates
* inform{"exam_time": 1300}  
 - slot{"exam_time": 1300}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_032
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100}
 - utter_ask_moreupdates
* inform{"patient_height": 1.9}  
 - slot{"patient_height": 1.9}  
 - utter_ask_moreupdates 
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye 

## story_033
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8}
 - utter_ask_moreupdates
* inform{"error": "Unknown"} 
 - slot{"error": "Unknown"} 
 - utter_ask_moreupdates 
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye  

## story_034
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "RF Amplifier"}
 - slot{"error": "RF Amplifier"}
 - utter_ask_examsed
* inform{"exam_sed": 2500} 
 - slot{"exam_sed": 2500} 
 - utter_ask_examtime
* inform{"exam_time": 1200} 
 - slot{"exam_time": 1200} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_moreupdates
* inform{"patient_weight": 120}  
 - slot{"patient_weight": 120}  
 - utter_ask_moreupdates
* inform{"system": "3.0T"} 
 - slot{"system": "3.0T"} 
 - utter_ask_moreupdates 
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye   

## story_035
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_haserror
* inform{"error": "RF Meter"}
 - slot{"error": "RF Meter"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100}
 - utter_ask_moreupdates
* inform{"exam_time": 800}  
 - slot{"exam_time": 800}  
 - utter_ask_moreupdates 
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye   

## story_036
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_haserror
* inform{"error": "RF Amplifier"}
 - slot{"error": "RF Amplifier"}
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_patientheight 
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 80} 
 - slot{"patient_weight": 80} 
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500} 
 - utter_ask_moreupdates
* inform{"system": "3.0T"} 
 - slot{"system": "3.0T"} 
 - utter_ask_moreupdates 
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_037
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"burn"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_haserror
* inform{"error": "RF Meter"}
 - slot{"error": "RF Meter"}
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_patientweight
* inform{"patient_weight": 75} 
 - slot{"patient_weight": 75} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8}
 - utter_ask_examtime
* inform{"exam_time": 800} 
 - slot{"exam_time": 800} 
 - utter_ask_examsed
* inform{"exam_sed": 1200} 
 - slot{"exam_sed": 1200}
 - utter_ask_moreupdates
* inform{"patient_height": 1.75} 
 - slot{"patient_height": 1.75} 
 - utter_ask_moreupdates
* inform{"patient_height": 1.7}  
 - slot{"patient_height": 1.7} 
 - utter_ask_moreupdates 
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_038
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_patientheight
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7} 
 - utter_ask_patientweight
* inform{"patient_weight": 70} 
 - slot{"patient_weight": 70} 
 - utter_ask_examtime
* inform{"exam_time": 1200} 
 - slot{"exam_time": 1200} 
 - utter_ask_examsed
* inform{"exam_sed": 2000} 
 - slot{"exam_sed": 2000} 
 - utter_ask_moreupdates
* inform{"patient_weight": 80}  
 - slot{"patient_weight": 80}  
 - utter_ask_moreupdates
* inform{"exam_time": 1500}  
 - slot{"exam_time": 1500}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_039
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"burn"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900}
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100}
 - utter_ask_moreupdates
* inform{"patient_height": 1.7}  
 - slot{"patient_height": 1.7}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye 

## story_040
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"burn"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_moreupdates
* inform{"system": "1.5T"} 
 - slot{"system": "1.5T"} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye  

## story_041
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"burning"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_haserror
* inform{"error": "RF Amplifier"}
 - slot{"error": "RF Amplifier"}
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_examsed
* inform{"exam_sed": 2500} 
 - slot{"exam_sed": 2500}
 - utter_ask_examtime
* inform{"exam_time": 1000} 
 - slot{"exam_time": 1000} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_moreupdates
* inform{"patient_weight": 120}  
 - slot{"patient_weight": 120}
 - utter_ask_moreupdates
* inform{"exam_time": 1250}  
 - slot{"exam_time": 1250}  
 - utter_ask_moreupdates 
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye   

## story_042
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900}
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 110} 
 - slot{"patient_weight": 110} 
 - utter_ask_moreupdates
* inform{"exam_time": 780}  
 - slot{"exam_time": 780}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye    

## story_043
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"burn"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 75} 
 - slot{"patient_weight": 75} 
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_moreupdates
* inform{"damage_degree": "2nd_degree"}  
 - slot{"damage_degree": "2nd_degree"}  
 - utter_ask_moreupdates 
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_044
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "RF Meter"}
 - slot{"error": "RF Meter"}
 - utter_ask_patientweight
* inform{"patient_weight": 80} 
 - slot{"patient_weight": 80} 
 - utter_ask_patientheight
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7} 
 - utter_ask_examtime
* inform{"exam_time": 800} 
 - slot{"exam_time": 800} 
 - utter_ask_examsed
* inform{"exam_sed": 1200} 
 - slot{"exam_sed": 1200}
 - utter_ask_moreupdates
* inform{"patient_height": 1.75} 
 - slot{"patient_height": 1.75} 
 - utter_ask_moreupdates
* inform{"patient_weight": 78}  
 - slot{"patient_weight": 78}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_045
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"burn"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_patientheight
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7} 
 - utter_ask_patientweight
* inform{"patient_weight": 70} 
 - slot{"patient_weight": 70} 
 - utter_ask_examtime
* inform{"exam_time": 1200} 
 - slot{"exam_time": 1200} 
 - utter_ask_examsed
* inform{"exam_sed": 2000} 
 - slot{"exam_sed": 2000} 
 - utter_ask_moreupdates
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_moreupdates
* inform{"exam_sed": 2200}  
 - slot{"exam_sed": 2200}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_046
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900}
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientheight
* inform{"patient_height": 2.0} 
 - slot{"patient_height": 2.0} 
 - utter_ask_patientweight
* inform{"patient_weight": 120} 
 - slot{"patient_weight": 120} 
 - utter_ask_moreupdates
* inform{"exam_sed": 1700}  
 - slot{"exam_sed": 1700}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye 

## story_047
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heat"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 2000} 
 - slot{"exam_sed": 2000} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_moreupdates
* inform{"system": "1.5T"} 
 - slot{"system": "1.5T"} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye  

## story_048
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heat"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "RF Amplifier"}
 - slot{"error": "RF Amplifier"}
 - utter_ask_examsed
* inform{"exam_sed": 2500} 
 - slot{"exam_sed": 2500} 
 - utter_ask_examtime
* inform{"exam_time": 1200} 
 - slot{"exam_time": 1200} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8}
 - utter_ask_moreupdates
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7} 
 - utter_ask_moreupdates
* inform{"error": "RF Meter"} 
 - slot{"error": "RF Meter"} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye   

## story_049
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heat"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror
* inform{"error": "RF Meter"}
 - slot{"error": "RF Meter"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100}
 - utter_ask_moreupdates
* inform{"patient_height": 1.85}  
 - slot{"patient_height": 1.85}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye   

## story_050
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_systemtype
* inform{"error": "RF Amplifier"}
 - slot{"error": "RF Amplifier"}
 - utter_ask_patientheight
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_haserror 
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 80} 
 - slot{"patient_weight": 80} 
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_moreupdates
* inform{"patient_height": 1.7}  
 - slot{"patient_height": 1.7}  
 - utter_ask_moreupdates 
* inform{"damage_degree": "warm"}  
 - slot{"damage_degree": "warm"}
 - utter_ask_moreupdates 
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_051
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"heat"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_haserror
* inform{"error": "RF Meter"}
 - slot{"error": "RF Meter"}
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_patientweight
* inform{"patient_weight": 75} 
 - slot{"patient_weight": 75} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_examtime
* inform{"exam_time": 800} 
 - slot{"exam_time": 800} 
 - utter_ask_examsed
* inform{"exam_sed": 1200} 
 - slot{"exam_sed": 1200} 
 - utter_ask_moreupdates
* inform{"patient_height": 1.75} 
 - slot{"patient_height": 1.75} 
 - utter_ask_moreupdates
* inform{"patient_weight": 85}  
 - slot{"patient_weight": 85}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_052
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_patientheight
* inform{"patient_height": 1.7} 
 - slot{"patient_height": 1.7} 
 - utter_ask_patientweight
* inform{"patient_weight": 70} 
 - slot{"patient_weight": 70} 
 - utter_ask_examtime
* inform{"exam_time": 1200} 
 - slot{"exam_time": 1200} 
 - utter_ask_examsed
* inform{"exam_sed": 2000} 
 - slot{"exam_sed": 2000} 
 - utter_ask_moreupdates
* inform{"patient_weight": 80}  
 - slot{"patient_weight": 80}  
 - utter_ask_moreupdates
* inform{"patient_height": 1.8}  
 - slot{"patient_height": 1.8}
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye

## story_053
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"too hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_moreupdates
* inform{"exam_time": 780}  
 - slot{"exam_time": 780}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye 

## story_054
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot sensation"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "warm"} 
 - slot{"damage_degree": "warm"} 
 - utter_ask_haserror
* inform{"error": "Cable"}
 - slot{"error": "Cable"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_moreupdates
* inform{"exam_time": 750}  
 - slot{"exam_time": 750}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye  

## story_055
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"warm"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "redness"} 
 - slot{"damage_degree": "redness"} 
 - utter_ask_haserror
* inform{"error": "RF Amplifier"}
 - slot{"error": "RF Amplifier"}
 - utter_ask_systemtype
* inform{"system": "1.5T"}
 - slot{"system": "1.5T"}
 - utter_ask_examsed
* inform{"exam_sed": 2500} 
 - slot{"exam_sed": 2500}
 - utter_ask_examtime
* inform{"exam_time": 1000} 
 - slot{"exam_time": 1000} 
 - utter_ask_patientweight
* inform{"patient_weight": 100} 
 - slot{"patient_weight": 100} 
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_moreupdates
* inform{"patient_weight": 120}  
 - slot{"patient_weight": 120}
 - utter_ask_moreupdates
* inform{"exam_sed": 2700}  
 - slot{"exam_sed": 2700}  
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye   

## story_056
* greet
 - utter_ask_howcanhelp
* issue{"issue_burn":"hot"}
 - utter_on_it
 - utter_ask_damagedegree
* inform{"damage_degree": "1st_degree"} 
 - slot{"damage_degree": "1st_degree"} 
 - utter_ask_haserror
* inform{"error": "Unknown"}
 - slot{"error": "Unknown"}
 - utter_ask_systemtype
* inform{"system": "3.0T"}
 - slot{"system": "3.0T"}
 - utter_ask_examtime
* inform{"exam_time": 900} 
 - slot{"exam_time": 900} 
 - utter_ask_examsed
* inform{"exam_sed": 1500} 
 - slot{"exam_sed": 1500}
 - utter_ask_patientheight
* inform{"patient_height": 1.8} 
 - slot{"patient_height": 1.8} 
 - utter_ask_patientweight
* inform{"patient_weight": 110} 
 - slot{"patient_weight": 110}
 - utter_ask_moreupdates
* inform{"system": "1.5T"} 
 - slot{"system": "1.5T"} 
 - utter_ask_moreupdates
* deny
 - action_ticket
 - action_suggest
* thankyou
 - utter_welcome
* goodbye 
 - utter_goodbye     

## story_057
* greet
 - utter_ask_howcanhelp
* issue{"issue_image": "blur"}
 - utter_suggest_callservice
* affirm
 - utter_thankyou
* goodbye
 - utter_goodbye     

## story_058
* greet
 - utter_ask_howcanhelp
* issue{"issue_image": "spike"}
 - utter_suggest_callservice
* affirm
 - utter_thankyou
* thankyou
 - utter_welcome 
* goodbye
 - utter_goodbye

## story_059
* greet
 - utter_ask_howcanhelp
* issue{"issue_image": "not good"}
 - utter_suggest_callservice
* affirm
 - utter_thankyou
* thankyou
 - utter_welcome 
* goodbye
 - utter_goodbye  

## story_060
* greet
 - utter_ask_howcanhelp
* issue{"issue_image": "artifact"}
 - utter_suggest_callservice
* affirm
 - utter_thankyou
* goodbye
 - utter_goodbye    