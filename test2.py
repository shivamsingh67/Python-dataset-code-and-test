import unittest
import most_run
import csv
from csv import DictReader

file = open('deliveries.csv', mode='r')
match_data = DictReader(file)

dict = [('V Kohli', 5878), ('SK Raina', 5368), ('DA Warner', 5254), ('RG Sharma', 5230), ('S Dhawan', 5197), ('AB de Villiers', 4849), ('CH Gayle', 4772), ('MS Dhoni', 4632), ('RV Uthappa', 4607), ('G Gambhir', 4217), ('AM Rahane', 3933), ('SR Watson', 3874), ('KD Karthik', 3823), ('AT Rayudu', 3659), ('MK Pandey', 3268), ('YK Pathan', 3204), ('KA Pollard', 3023), ('BB McCullum', 2880), ('PA Patel', 2848), ('Yuvraj Singh', 2750), ('V Sehwag', 2728), ('KL Rahul', 2647), ('M Vijay', 2619), ('SV Samson', 2584), ('SE Marsh', 2477), ('JH Kallis', 2427), ('DR Smith', 2385), ('SR Tendulkar', 2334), ('SPD Smith', 2333), ('F du Plessis', 2302), ('SS Iyer', 2200), ('R Dravid', 2174), ('RA Jadeja', 2159), ('RR Pant', 2079), ('AC Gilchrist', 2069), ('JP Duminy', 2029), ('SA Yadav', 2024), ('AJ Finch', 2005), ('WP Saha', 1979), ('MEK Hussey', 1977), ('Q de Kock', 1959), ('DA Miller', 1850), ('DPMD Jayawardene', 1802), ('JC Buttler', 1714), ('MK Tiwary', 1695), ('MA Agarwal', 1690), ('KC Sangakkara', 1687), ('Mandeep Singh', 1659), ('KS Williamson', 1619), ('NV Ojha', 1554), ('AD Russell', 1517), ('GJ Maxwell', 1505), ('DJ Bravo', 1490), ('KK Nair', 1480), ('S Badrinath', 1441), ('N Rana', 1437), ('BJ Hodge', 1400), ('SS Tiwary', 1379), ('SC Ganguly', 1349), ('HH Pandya', 1349), ('DJ Hussey', 1322), ('CA Lynn', 1280), ('EJG Morgan', 1272), ('Ishan Kishan', 1211), ('TM Dilshan', 1153), ('KM Jadhav', 1141), ('IK Pathan', 1139), ('ML Hayden', 1107), ('LMP Simmons', 1079), ('LRPL Taylor', 1017), ('M Vohra', 1012), ('KP Pietersen', 1001), ('KH Pandya', 1000), ('RA Tripathi', 988), ('Y Venugopal Rao', 985), ('A Symonds', 974), ('JA Morkel', 974), ('MC Henriques', 969), ('CL White', 954), ('Shubman Gill', 939), ('BA Stokes', 920), ('AR Patel', 913), ('SP Narine', 892), ('HH Gibbs', 886), ('STR Binny', 880), ('Harbhajan Singh', 829), ('PP Shaw', 826), ('MP Stoinis', 825), ('MS Bisla', 798), ('JM Bairstow', 790), ('ST Jayasuriya', 768), ('Shakib Al Hasan', 746), ('GC Smith', 739), ('AD Mathews', 724), ('TL Suman', 676), ('AM Nayar', 672), ('GJ Bailey', 663), ('V Shankar', 654), ('DJ Hooda', 625), ('JD Ryder', 604), ('PP Chawla', 584), ('HM Amla', 577), ('CH Morris', 551), ('CJ Anderson', 538), ('RS Bopara', 531), ('JP Faulkner', 527), ('N Pooran', 521), ('M Manhas', 514), ('Gurkeerat Singh', 511), ('OA Shah', 506), ('PC Valthaty', 505), ('D Padikkal', 473), ('DT Christian', 446), ('SN Khan', 441), ('E Lewis', 430), ('SA Asnodkar', 423), ('NLTC Perera', 422), ('JR Hopes', 417), ('R Ashwin', 412), ('J Botha', 409), ('LR Shukla', 405), ('AL Menaria', 401), ('MV Boucher', 394), ('CA Pujara', 390), ('Azhar Mahmood', 388), ('DB Ravi Teja', 375), ('S Sohal', 368), ('R Tewatia', 366), ('P Negi', 365), ('A Mishra', 362), ('R Bhatia', 342), ('P Kumar', 340), ('AP Tare', 339), ('SW Billings', 334), ('JEC Franklin', 327), ('RN ten Doeschate', 326), ('KV Sharma', 317), ('R Vinay Kumar', 310), ('MM Ali', 309), ('DB Das', 304), ('C de Grandhomme', 303), ('LA Pomersbach', 302), ('UBT Chand', 300), ('DJG Sammy', 295), ('SP Goswami', 293), ('Y Nagar', 285), ('GH Vihari', 284), ('VVS Laxman', 282), ('SM Curran', 281), ('B Chipli', 280), ('A Ashish Reddy', 280), ('MJ Lumb', 278), ('SO Hetmyer', 275), ('R Sathish', 270), ('MJ Guptill', 270), ('M Kaif', 259), ('R Parag', 246), ('SM Katich', 241), ('BCJ Cutting', 238), ('MD Mishra', 237), ('MR Marsh', 225), ('PJ Cummins', 223), ('K Goel', 218), ('AA Jhunjhunwala', 217), ('CA Ingram', 205), ('TM Head', 205), ('RD Gaikwad', 204), ('PD Collingwood', 203), ('SK Warne', 198), ('SP Fleming', 196), ('JC Archer', 195), ('AS Raut', 194), ('Salman Butt', 193), ('BJ Rohrer', 193), ('YV Takawale', 192), ('Bipul Sharma', 187), ('Washington Sundar', 186), ('K Gowtham', 186), ('FY Fazal', 183), ('B Kumar', 183), ('AC Voges', 181), ('CR Brathwaite', 181), ('AB Agarkar', 179), ('JJ Roy', 179), ('MF Maharoof', 177), ('C Munro', 177), ('DH Yagnik', 170), ('CM Gautam', 169), ('S Dube', 169), ('DW Steyn', 167), ('MN van Wyk', 167), ('MG Johnson', 167), ('PA Reddy', 164), ('S Gopal', 164), ('MN Samuels', 161), ('RE van der Merwe', 159), ('R McLaren', 159), ('R Dhawan', 153), ('AD Hales', 148), ('SM Pollock', 147), ('Mohammad Nabi', 146), ('S Vidyut', 145), ('Abhishek Sharma', 143), ('N Saini', 140), ('Rashid Khan', 139), ('Sachin Baby', 137), ('S Anirudha', 136), ('PK Garg', 133), ('SB Styris', 131), ('W Jaffer', 130), ('Kamran Akmal', 128), ('HV Patel', 128), ('P Dogra', 127), ('D Wiese', 127), ('UT Khawaja', 127), ('M Morkel', 126), ('BB Samantray', 125), ('MC Juneja', 125), ('K Rabada', 125), ('B Lee', 124), ('AB McDonald', 123), ('UT Yadav', 122), ('MM Sharma', 122), ('Niraj Patel', 121), ('DL Vettori', 121), ('AC Blizzard', 120), ('Z Khan', 117), ('Misbah-ul-Haq', 117), ('RJ Harris', 117), ('KK Cooper', 116), ('TG Southee', 115), ('DJM Short', 115), ('M Kartik', 113), ('DJ Harris', 111), ('Abdul Samad', 111), ('JDP Oram', 106), ('LJ Wright', 106), ('TK Curran', 106), ('DS Kulkarni', 104), ('JO Holder', 104), ('RJ Quiney', 103), ('MS Gony', 99), ('SD Chitnis', 99), ('CJ Ferguson', 98), ('MJ Clarke', 98), ('MA Starc', 96), ('PR Shah', 92), ('DJ Jacobs', 92), ('RT Ponting', 91), ('S Rana', 91), ('AJ Tye', 91), ('AD Nath', 90), ('Iqbal Abdulla', 88), ('SL Malinga', 88), ('Ankit Sharma', 87), ('AP Majumdar', 87), ('MK Lomror', 87), ('MJ McClenaghan', 85), ('RE Levi', 83), ('WPUJC Vaas', 81), ('Shahid Afridi', 81), ('LA Carseldine', 81), ('AD Mascarenhas', 79), ('DL Chahar', 78), ('JR Philippe', 78), ('NM Coulter-Nile', 77), ('RK Singh', 77), ('B Akhil', 76), ('IR Jaggi', 76), ('TR Birt', 75), ('RR Sarwan', 73), ('M Klinger', 73), ('SE Rutherford', 73), ('LS Livingstone', 70), ('AA Bilakhia', 69), ('RR Powar', 67), ('R Sharma', 66), ('H Klaasen', 66), ('Mohammad Hafeez', 64), ('JD Unadkat', 64), ('Anirudh Singh', 63), ('WD Parnell', 63), ('CR Woakes', 63), ('A Flintoff', 62), ('JDS Neesham', 61), ('S Aravind', 59), ('Kuldeep Yadav', 57), ('WA Mota', 56), ('Mohammed Shami', 56), ('M Rawat', 55), ('I Sharma', 55), ('J Suchith', 54), ('A Chopra', 53), ('RR Rossouw', 53), ('RP Singh', 52), ('Shoaib Malik', 52), ('KB Arun Karthik', 51), ('R Rampaul', 51), ('RV Gomez', 50), ('VR Aaron', 50), ('AS Yadav', 49), ('SB Bangar', 49), ('AG Paunikar', 49), ('SN Thakur', 48), ('Yashpal Singh', 47), ('Mohammed Siraj', 46), ('Sandeep Sharma', 44), ('LH Ferguson', 44), ('Sunny Singh', 43), ('SK Trivedi', 42), ('AB Barath', 42), ('A Nehra', 41), ('LPC Silva', 40), ('JJ Bumrah', 40), ('BR Dunk', 40), ('YBK Jaiswal', 40), ('DJ Thornely', 39), ('Umar Gul', 39), ('MM Patel', 39), ('AUK Pathan', 39), ('S Nadeem', 39), ('SP Jackson', 38), ('S Narwal', 37), ('Sohail Tanvir', 36), ('Joginder Sharma', 36), ('L Balaji', 36), ('AN Ahmed', 36), ('KW Richardson', 36), ('Anureet Singh', 36), ('A Kumble', 35), ('B Sumanth', 35), ('L Ronchi', 34), ('S Sreesanth', 34), ('A Mithun', 34), ('AP Dole', 34), ('D Salunkhe', 33), ('Imran Tahir', 33), ('N Jagadeesan', 33), ('RJ Peterson', 32), ('CJ Jordan', 32), ('Basil Thampi', 32), ('MJ Santner', 32), ('AT Carey', 32), ('T Taibu', 31), ('S Sriram', 31), ('NS Naik', 31), ('P Simran Singh', 31), ('J Syed Mohammad', 29), ('VH Zol', 29), ('NA Saini', 29), ('SB Jakati', 28), ('M Markande', 27), ('AB Dinda', 26), ('JM Kemp', 26), ('NL McCullum', 26), ('AS Rajpoot', 26), ('S Chanderpaul', 25), ('A Choudhary', 25), ('MA Khote', 24), ('PJ Sangwan', 24), ('KC Cariappa', 24), ('ER Dwivedi', 24), ('J Arunkumar', 23), ('SW Tait', 23), ('BMAJ Mendis', 23), ('Shivam Mavi', 23), ('MS Wade', 22), ('GB Hogg', 22), ('YS Chahal', 22), ('KL Nagarkoti', 22), ('DE Bollinger', 21), ('TU Deshpande', 21), ('RR Raje', 20), ('M Muralitharan', 20), ('AC Thomas', 20), ('Harpreet Singh', 20), ('NJ Maddinson', 20), ('Harpreet Brar', 20), ('A Mukund', 19), ('R Bishnoi', 19), ('DR Martyn', 19), ('Y Gnaneswara Rao', 19), ('R Shukla', 19), ('P Sahu', 19), ('Vishnu Vinod', 19), ('P Ray Barman', 19), ('DS Lehmann', 18), ('Harmeet Singh', 18), ('JJ van der Wath', 18), ('BJ Haddin', 18), ('PV Tambe', 18), ('KMA Paul', 18), ('T Banton', 18), ('Parvez Rasool', 17), ('RD Chahar', 17), ('CK Kapugedera', 16), ('PP Ojha', 16), ('VY Mahesh', 15), ('GR Napier', 15), ('C Madan', 15), ('SA Abbott', 15), ('SD Lad', 15), ('AS Joseph', 15), ('JL Pattinson', 15), ('I Udana', 15), ('MDKJ Perera', 14), ('F Behardien', 14), ('DT Patil', 13), ('KJ Abbott', 13), ('S Badree', 13), ('DR Shorey', 13), ('T Thushara', 12), ('AA Chavan', 12), ('DAJ Bracewell', 12), ('K Upadhyay', 12), ('S Kaul', 12), ('Karanveer Singh', 12), ('Swapnil Singh', 12), ('AR Bawne', 12), ('TA Boult', 12), ('T Kohli', 11), ('DNT Zoysa', 11), ('M Ntini', 11), ('T Henderson', 11), ('Mujeeb Ur Rahman', 11), ('D du Preez', 10), ('J Theron', 10), ('KAJ Roach', 10), ('TD Paine', 10), ('AG Murtaza', 10), ('SMSM Senanayake', 10), ('X Thalaivan Sargunam', 10), ('BB Sran', 10), ('CV Varun', 10), ('AA Noffke', 9), ('SM Harwood', 9), ('TM Srivastava', 8), ('Jaskaran Singh', 8), ('CK Langeveldt', 8), ('CJ McKay', 8), ('M Ashwin', 8), ('TS Mills', 8), ('P Chopra', 8), ('JPR Scantlebury-Searles', 8), ('Pankaj Singh', 7), ('AN Ghosh', 7), ('VS Malik', 7), ('I Malhotra', 7), ('UA Birla', 7), ('AF Milne', 7), ('Ankit Soni', 7), ('RK Bhui', 7), ('IS Sodhi', 7), ('A Nortje', 7), ('Ravi Bishnoi', 7), ('P Dubey', 7), ('SB Joshi', 6), ('SS Shaikh', 6), ('BA Bhatt', 6), ('PSP Handscomb', 6), ('J Yadav', 6), ('DM Bravo', 6), ('SJ Srivastava', 5), ('KMDN Kulasekara', 5), ('P Awana', 5), ('B Laughlin', 5), ('Shivam Sharma', 5), ('A Zampa', 5), ('B Stanlake', 5), ('Rasikh Salam', 5), ('VRV Singh', 4), ('GD McGrath', 4), ('CRD Fernando', 4), ('FH Edwards', 4), ('A Uniyal', 4), ('DP Nannes', 4), ('RS Sodhi', 4), ('A Chandila', 4), ('A Dananjaya', 4), ('Avesh Khan', 4), ('Kartik Tyagi', 4), ('D Kalyankrishna', 3), ('Mohammad Asif', 3), ('Younis Khan', 3), ('Kamran Khan', 3), ('BAW Mendis', 3), ('S Tyagi', 3), ('R Ninan', 3), ('JE Taylor', 3), ('M Prasidh Krishna', 3), ('GC Viljoen', 3), ('AJ Turner', 3), ('T Natarajan', 3), ('Shoaib Akhtar', 2), ('H Das', 2), ('VS Yeligati', 2), ('KP Appanna', 2), ('Mashrafe Mortaza', 2), ('A Singh', 2), ('Mohammad Ashraful', 2), ('RS Gavaskar', 2), ('SB Wagh', 2), ('S Randiv', 2), ('RG More', 2), ('PM Sarvesh Kumar', 1), ('DP Vijaykumar', 1), ('Shoaib Ahmed', 1), ('SE Bond', 1), ('NJ Rimmington', 1), ('P Parameswaran', 1), ('BE Hendricks', 1), ('M de Lange', 1), ('DJ Muthuswami', 1), ('MA Wood', 1), ('LE Plunkett', 1), ('Mustafizur Rahman', 1), ('HF Gurney', 1), ('Shahbaz Ahmed', 1), ('U Kaul', 0), ('Abdur Razzak', 0), ('C Nanda', 0), ('YA Abdulla', 0), ('S Ladda', 0), ('L Ablish', 0), ('ND Doshi', 0), ('RR Bhatkal', 0), ('V Pratap Singh', 0), ('Sunny Gupta', 0), ('IC Pandey', 0), ('S Kaushik', 0), ('S Lamichhane', 0), ('JL Denly', 0), ('KK Ahmed', 0), ('Y Prithvi Raj', 0), ('SS Cottrell', 0), ('Arshdeep Singh', 0), ('DR Sams', 0)]

dict1 = [('V Kohli', 5878), ('SK Raina', 5368), ('DA Warner', 5254), ('RG Sharma', 5230), ('S Dhawan', 5197), ('AB de Villiers', 4849), ('CH Gayle', 4772), ('MS Dhoni', 4632), ('RV Uthappa', 4607), ('G Gambhir', 4217), ('AM Rahane', 3933), ('SR Watson', 3874), ('KD Karthik', 3823), ('AT Rayudu', 3659), ('MK Pandey', 3268), ('YK Pathan', 3204), ('KA Pollard', 3023), ('BB McCullum', 2880), ('PA Patel', 2848), ('Yuvraj Singh', 2750), ('V Sehwag', 2728), ('KL Rahul', 2647), ('M Vijay', 2619), ('SV Samson', 2584), ('SE Marsh', 2477), ('JH Kallis', 2427), ('DR Smith', 2385), ('SR Tendulkar', 2334), ('SPD Smith', 2333), ('F du Plessis', 2302), ('SS Iyer', 2200), ('R Dravid', 2174), ('RA Jadeja', 2159), ('RR Pant', 2079), ('AC Gilchrist', 2069), ('JP Duminy', 2029), ('SA Yadav', 2024), ('AJ Finch', 2005), ('WP Saha', 1979), ('MEK Hussey', 1977), ('Q de Kock', 1959), ('DA Miller', 1850), ('DPMD Jayawardene', 1802), ('JC Buttler', 1714), ('MK Tiwary', 1695), ('MA Agarwal', 1690), ('KC Sangakkara', 1687), ('Mandeep Singh', 1659), ('KS Williamson', 1619), ('NV Ojha', 1554), ('AD Russell', 1517), ('GJ Maxwell', 1505), ('DJ Bravo', 1490), ('KK Nair', 1480), ('S Badrinath', 1441), ('N Rana', 1437), ('BJ Hodge', 1400), ('SS Tiwary', 1379), ('SC Ganguly', 1349), ('HH Pandya', 1349), ('DJ Hussey', 1322), ('CA Lynn', 1280), ('EJG Morgan', 1272), ('Ishan Kishan', 1211), ('TM Dilshan', 1153), ('KM Jadhav', 1141), ('IK Pathan', 1139), ('ML Hayden', 1107), ('LMP Simmons', 1079), ('LRPL Taylor', 1017), ('M Vohra', 1012), ('KP Pietersen', 1001), ('KH Pandya', 1000), ('RA Tripathi', 988), ('Y Venugopal Rao', 985), ('A Symonds', 974), ('JA Morkel', 974), ('MC Henriques', 969), ('CL White', 954), ('Shubman Gill', 939), ('BA Stokes', 920), ('AR Patel', 913), ('SP Narine', 892), ('HH Gibbs', 886), ('STR Binny', 880), ('Harbhajan Singh', 829), ('PP Shaw', 826), ('MP Stoinis', 825), ('MS Bisla', 798), ('JM Bairstow', 790), ('ST Jayasuriya', 768), ('Shakib Al Hasan', 746), ('GC Smith', 739), ('AD Mathews', 724), ('TL Suman', 676), ('AM Nayar', 672), ('GJ Bailey', 663), ('V Shankar', 654), ('DJ Hooda', 625), ('JD Ryder', 604), ('PP Chawla', 584), ('HM Amla', 577), ('CH Morris', 551), ('CJ Anderson', 538), ('RS Bopara', 531), ('JP Faulkner', 527), ('N Pooran', 521), ('M Manhas', 514), ('Gurkeerat Singh', 511), ('OA Shah', 506), ('PC Valthaty', 505), ('D Padikkal', 473), ('DT Christian', 446), ('SN Khan', 441), ('E Lewis', 430), ('SA Asnodkar', 423), ('NLTC Perera', 422), ('JR Hopes', 417), ('R Ashwin', 412), ('J Botha', 409), ('LR Shukla', 405), ('AL Menaria', 401), ('MV Boucher', 394), ('CA Pujara', 390), ('Azhar Mahmood', 388), ('DB Ravi Teja', 375), ('S Sohal', 368), ('R Tewatia', 366), ('P Negi', 365), ('A Mishra', 362), ('R Bhatia', 342), ('P Kumar', 340), ('AP Tare', 339), ('SW Billings', 334), ('JEC Franklin', 327), ('RN ten Doeschate', 326), ('KV Sharma', 317), ('R Vinay Kumar', 310), ('MM Ali', 309), ('DB Das', 304), ('C de Grandhomme', 303), ('LA Pomersbach', 302), ('UBT Chand', 300), ('DJG Sammy', 295), ('SP Goswami', 293), ('Y Nagar', 285), ('GH Vihari', 284), ('VVS Laxman', 282), ('SM Curran', 281), ('B Chipli', 280), ('A Ashish Reddy', 280), ('MJ Lumb', 278), ('SO Hetmyer', 275), ('R Sathish', 270), ('MJ Guptill', 270), ('M Kaif', 259), ('R Parag', 246), ('SM Katich', 241), ('BCJ Cutting', 238), ('MD Mishra', 237), ('MR Marsh', 225), ('PJ Cummins', 223), ('K Goel', 218), ('AA Jhunjhunwala', 217), ('CA Ingram', 205), ('TM Head', 205), ('RD Gaikwad', 204), ('PD Collingwood', 203), ('SK Warne', 198), ('SP Fleming', 196), ('JC Archer', 195), ('AS Raut', 194), ('Salman Butt', 193), ('BJ Rohrer', 193), ('YV Takawale', 192), ('Bipul Sharma', 187), ('Washington Sundar', 186), ('K Gowtham', 186), ('FY Fazal', 183), ('B Kumar', 183), ('AC Voges', 181), ('CR Brathwaite', 181), ('AB Agarkar', 179), ('JJ Roy', 179), ('MF Maharoof', 177), ('C Munro', 177), ('DH Yagnik', 170), ('CM Gautam', 169), ('S Dube', 169), ('DW Steyn', 167), ('MN van Wyk', 167), ('MG Johnson', 167), ('PA Reddy', 164), ('S Gopal', 164), ('MN Samuels', 161), ('RE van der Merwe', 159), ('R McLaren', 159), ('R Dhawan', 153), ('AD Hales', 148), ('SM Pollock', 147), ('Mohammad Nabi', 146), ('S Vidyut', 145), ('Abhishek Sharma', 143), ('N Saini', 140), ('Rashid Khan', 139), ('Sachin Baby', 137), ('S Anirudha', 136), ('PK Garg', 133), ('SB Styris', 131), ('W Jaffer', 130), ('Kamran Akmal', 128), ('HV Patel', 128), ('P Dogra', 127), ('D Wiese', 127), ('UT Khawaja', 127), ('M Morkel', 126), ('BB Samantray', 125), ('MC Juneja', 125), ('K Rabada', 125), ('B Lee', 124), ('AB McDonald', 123), ('UT Yadav', 122), ('MM Sharma', 122), ('Niraj Patel', 121), ('DL Vettori', 121), ('AC Blizzard', 120), ('Z Khan', 117), ('Misbah-ul-Haq', 117), ('RJ Harris', 117), ('KK Cooper', 116), ('TG Southee', 115), ('DJM Short', 115), ('M Kartik', 113), ('DJ Harris', 111), ('Abdul Samad', 111), ('JDP Oram', 106), ('LJ Wright', 106), ('TK Curran', 106), ('DS Kulkarni', 104), ('JO Holder', 104), ('RJ Quiney', 103), ('MS Gony', 99), ('SD Chitnis', 99), ('CJ Ferguson', 98), ('MJ Clarke', 98), ('MA Starc', 96), ('PR Shah', 92), ('DJ Jacobs', 92), ('RT Ponting', 91), ('S Rana', 91), ('AJ Tye', 91), ('AD Nath', 90), ('Iqbal Abdulla', 88), ('SL Malinga', 88), ('Ankit Sharma', 87), ('AP Majumdar', 87), ('MK Lomror', 87), ('MJ McClenaghan', 85), ('RE Levi', 83), ('WPUJC Vaas', 81), ('Shahid Afridi', 81), ('LA Carseldine', 81), ('AD Mascarenhas', 79), ('DL Chahar', 78), ('JR Philippe', 78), ('NM Coulter-Nile', 77), ('RK Singh', 77), ('B Akhil', 76), ('IR Jaggi', 76), ('TR Birt', 75), ('RR Sarwan', 73), ('M Klinger', 73), ('SE Rutherford', 73), ('LS Livingstone', 70), ('AA Bilakhia', 69), ('RR Powar', 67), ('R Sharma', 66), ('H Klaasen', 66), ('Mohammad Hafeez', 64), ('JD Unadkat', 64), ('Anirudh Singh', 63), ('WD Parnell', 63), ('CR Woakes', 63), ('A Flintoff', 62), ('JDS Neesham', 61), ('S Aravind', 59), ('Kuldeep Yadav', 57), ('WA Mota', 56), ('Mohammed Shami', 56), ('M Rawat', 55), ('I Sharma', 55), ('J Suchith', 54), ('A Chopra', 53), ('RR Rossouw', 53), ('RP Singh', 52), ('Shoaib Malik', 52), ('KB Arun Karthik', 51), ('R Rampaul', 51), ('RV Gomez', 50), ('VR Aaron', 50), ('AS Yadav', 49), ('SB Bangar', 49), ('AG Paunikar', 49), ('SN Thakur', 48), ('Yashpal Singh', 47), ('Mohammed Siraj', 46), ('Sandeep Sharma', 44), ('LH Ferguson', 44), ('Sunny Singh', 43), ('SK Trivedi', 42), ('AB Barath', 42), ('A Nehra', 41), ('LPC Silva', 40), ('JJ Bumrah', 40), ('BR Dunk', 40), ('YBK Jaiswal', 40), ('DJ Thornely', 39), ('Umar Gul', 39), ('MM Patel', 39), ('AUK Pathan', 39), ('S Nadeem', 39), ('SP Jackson', 38), ('S Narwal', 37), ('Sohail Tanvir', 36), ('Joginder Sharma', 36), ('L Balaji', 36), ('AN Ahmed', 36), ('KW Richardson', 36), ('Anureet Singh', 36), ('A Kumble', 35), ('B Sumanth', 35), ('L Ronchi', 34), ('S Sreesanth', 34), ('A Mithun', 34), ('AP Dole', 34), ('D Salunkhe', 33), ('Imran Tahir', 33), ('N Jagadeesan', 33), ('RJ Peterson', 32), ('CJ Jordan', 32), ('Basil Thampi', 32), ('MJ Santner', 32), ('AT Carey', 32), ('T Taibu', 31), ('S Sriram', 31), ('NS Naik', 31), ('P Simran Singh', 31), ('J Syed Mohammad', 29), ('VH Zol', 29), ('NA Saini', 29), ('SB Jakati', 28), ('M Markande', 27), ('AB Dinda', 26), ('JM Kemp', 26), ('NL McCullum', 26), ('AS Rajpoot', 26), ('S Chanderpaul', 25), ('A Choudhary', 25), ('MA Khote', 24), ('PJ Sangwan', 24), ('KC Cariappa', 24), ('ER Dwivedi', 24), ('J Arunkumar', 23), ('SW Tait', 23), ('BMAJ Mendis', 23), ('Shivam Mavi', 23), ('MS Wade', 22), ('GB Hogg', 22), ('YS Chahal', 22), ('KL Nagarkoti', 22), ('DE Bollinger', 21), ('TU Deshpande', 21), ('RR Raje', 20), ('M Muralitharan', 20), ('AC Thomas', 20), ('Harpreet Singh', 20), ('NJ Maddinson', 20), ('Harpreet Brar', 20), ('A Mukund', 19), ('R Bishnoi', 19), ('DR Martyn', 19), ('Y Gnaneswara Rao', 19), ('R Shukla', 19), ('P Sahu', 19), ('Vishnu Vinod', 19), ('P Ray Barman', 19), ('DS Lehmann', 18), ('Harmeet Singh', 18), ('JJ van der Wath', 18), ('BJ Haddin', 18), ('PV Tambe', 18), ('KMA Paul', 18), ('T Banton', 18), ('Parvez Rasool', 17), ('RD Chahar', 17), ('CK Kapugedera', 16), ('PP Ojha', 16), ('VY Mahesh', 15), ('GR Napier', 15), ('C Madan', 15), ('SA Abbott', 15), ('SD Lad', 15), ('AS Joseph', 15), ('JL Pattinson', 15), ('I Udana', 15), ('MDKJ Perera', 14), ('F Behardien', 14), ('DT Patil', 13), ('KJ Abbott', 13), ('S Badree', 13), ('DR Shorey', 13), ('T Thushara', 12), ('AA Chavan', 12), ('DAJ Bracewell', 12), ('K Upadhyay', 12), ('S Kaul', 12), ('Karanveer Singh', 12), ('Swapnil Singh', 12), ('AR Bawne', 12), ('TA Boult', 12), ('T Kohli', 11), ('DNT Zoysa', 11), ('M Ntini', 11), ('T Henderson', 11), ('Mujeeb Ur Rahman', 11), ('D du Preez', 10), ('J Theron', 10), ('KAJ Roach', 10), ('TD Paine', 10), ('AG Murtaza', 10), ('SMSM Senanayake', 10), ('X Thalaivan Sargunam', 10), ('BB Sran', 10), ('CV Varun', 10), ('AA Noffke', 9), ('SM Harwood', 9), ('TM Srivastava', 8), ('Jaskaran Singh', 8), ('CK Langeveldt', 8), ('CJ McKay', 8), ('M Ashwin', 8), ('TS Mills', 8), ('P Chopra', 8), ('JPR Scantlebury-Searles', 8), ('Pankaj Singh', 7), ('AN Ghosh', 7), ('VS Malik', 7), ('I Malhotra', 7), ('UA Birla', 7), ('AF Milne', 7), ('Ankit Soni', 7), ('RK Bhui', 7), ('IS Sodhi', 7), ('A Nortje', 7), ('Ravi Bishnoi', 7), ('P Dubey', 7), ('SB Joshi', 6), ('SS Shaikh', 6), ('BA Bhatt', 6), ('PSP Handscomb', 6), ('J Yadav', 6), ('DM Bravo', 6), ('SJ Srivastava', 5), ('KMDN Kulasekara', 5), ('P Awana', 5), ('B Laughlin', 5), ('Shivam Sharma', 5), ('A Zampa', 5), ('B Stanlake', 5), ('Rasikh Salam', 5), ('VRV Singh', 4), ('GD McGrath', 4), ('CRD Fernando', 4), ('FH Edwards', 4), ('A Uniyal', 4), ('DP Nannes', 4), ('RS Sodhi', 4), ('A Chandila', 4), ('A Dananjaya', 4), ('Avesh Khan', 4), ('Kartik Tyagi', 4), ('D Kalyankrishna', 3), ('Mohammad Asif', 3), ('Younis Khan', 3), ('Kamran Khan', 3), ('BAW Mendis', 3), ('S Tyagi', 3), ('R Ninan', 3), ('JE Taylor', 3), ('M Prasidh Krishna', 3), ('GC Viljoen', 3), ('AJ Turner', 3), ('T Natarajan', 3), ('Shoaib Akhtar', 2), ('H Das', 2), ('VS Yeligati', 2), ('KP Appanna', 2), ('Mashrafe Mortaza', 2), ('A Singh', 2), ('Mohammad Ashraful', 2), ('RS Gavaskar', 2), ('SB Wagh', 2), ('S Randiv', 2), ('RG More', 2), ('PM Sarvesh Kumar', 1), ('DP Vijaykumar', 1), ('Shoaib Ahmed', 1), ('SE Bond', 1), ('NJ Rimmington', 1), ('P Parameswaran', 1), ('BE Hendricks', 1), ('M de Lange', 1), ('DJ Muthuswami', 1), ('MA Wood', 1), ('LE Plunkett', 1), ('Mustafizur Rahman', 1), ('HF Gurney', 1), ('Shahbaz Ahmed', 1), ('U Kaul', 0), ('Abdur Razzak', 0), ('C Nanda', 0), ('YA Abdulla', 0), ('S Ladda', 0), ('L Ablish', 0), ('ND Doshi', 0), ('RR Bhatkal', 0), ('V Pratap Singh', 0), ('Sunny Gupta', 0), ('IC Pandey', 0), ('S Kaushik', 0), ('S Lamichhane', 0), ('JL Denly', 0), ('KK Ahmed', 0), ('Y Prithvi Raj', 0), ('SS Cottrell', 0), ('Arshdeep Singh', 0), ('DR Sams', 1)]



class TestTask1(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(most_run.calculation(match_data), dict)


if __name__ == '__main__':
    unittest.main()