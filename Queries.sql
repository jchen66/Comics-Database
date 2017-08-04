# Milestone 2

# a) Print the brand group names with the highest number of Belgian indicia publishers. #RUN

SELECT BG.NAME
FROM BRAND_GROUP BG, (SELECT IP.PID 
                      FROM INDICIA_PUBLISHER IP, (SELECT Country.cid 
                                        			FROM Country 
                                          			WHERE Country.name='Belgium') A
                      WHERE IP.CID = A.CID
                      GROUP BY IP.PID
                      ORDER BY COUNT(IP.PID) DESC) B
WHERE B.PID = BG.PID;

# b) Print the ids and names of publishers of Danish book series.  # RUN

SELECT P.pid, P.name
FROM Publisher P, Country C, Series S, Publication_Type PT
WHERE C.name  = 'Denmark' AND PT.name = 'book' AND PT.ptid = S.ptid AND C.cid = S.cid AND S.pid = P.pid

# c) Print the names of all Swiss series that have been published in magazines.  # RUN

SELECT S.name
FROM Series S, Publication_Type PT, Country C
WHERE C.name  = 'Switzerland' AND PT.name = 'magazine' AND PT.ptid = S.ptid AND C.cid = S.cid

# d)  Starting from 1990, print the number of issues published each year.  # RUN 

SELECT COUNT(sid) AS AMOUNT, I.PUB_YEAR
FROM Issue I
WHERE I.PUB_YEAR >= 1990
GROUP BY I.PUB_YEAR

# e)  Print the number of series for each indicia publisher whose name resembles ‘DC comics’. # RUN

SELECT IP.NAME AS name, count(IP.ipid) AS amount 
FROM INDICIA_PUBLISHER IP JOIN SERIES S ON S.PID = IP.PID
WHERE IP.NAME LIKE '%DC Comics%'
GROUP BY IP.NAME

# f)  Print the titles of the 10 most reprinted stories  # RUN 

SELECT S.TITLE 
FROM STORY S, (SELECT S.SID
				FROM STORY_REPRINT SR
				JOIN STORY S ON SR.ORIGIN_ID = S.SID 
				GROUP BY S.SID
				ORDER BY COUNT(S.SID) DESC
				OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY) A
WHERE S.SID = A.SID;
									

# g) Print the artists that have scripted, drawn (pencils), and colored at least one of the stories they were involved in. # RUN 

SELECT DISTINCT A.NAME
FROM STORY_PENCIL_RELATIONSHIP SPRS, STORY_SCRIPT_RELATIONSHIP SSRS, STORY_COLOR_RELATIONSHIP SCRS, ARTIST A
WHERE SPRS.AID = SSRS.AID AND SPRS.AID = SCRS.AID AND SPRS.SID = SSRS.SID AND SPRS.SID = SCRS.SID AND A.AID = SPRS.AID;

# h) Print all non-reprinted stories involving Batman as a non-featured character. #RUN

SELECT DISTINCT S.TITLE  
FROM STORY S, STORY_REPRINT SR, CHARACTER C, STORY_CHARACTER_RELATIONSHIP SCRS
WHERE S.SID != SR.ORIGIN_ID AND C.NAME LIKE '%Batman%' AND SCRS.CID = C.CID AND SCRS.N_ID = C.N_ID AND SCRS.SID = S.SID AND SCRS.IS_FEATURE IS NULL;

# Milestone 3

# a) Print the series names that have the highest number of issues which contain a story whose type (e.g., cartoon) is
#    not the one occurring most frequently in the database (e.g, illustration). #RUN
SELECT S.NAME 
FROM SERIES S,(SELECT S.SID 
				FROM STORY S, (SELECT S.STID 
								FROM STORY S 
								GROUP BY S.STID 
								ORDER BY count(S.STID) DESC OFFSET 1 ROW) A 
				WHERE S.STID = A.STID
				GROUP BY S.SID
				ORDER BY COUNT(S.IID) DESC) B
WHERE S.SID = B.SID;

# b) Print the names of publishers who have series with all series types. #RUN 

SELECT DISTINCT P.NAME  
FROM PUBLISHER P, (SELECT S.PID FROM SERIES S WHERE S.PTID = 1) A, (SELECT S.PID FROM SERIES S WHERE S.PTID = 2) B, (SELECT S.PID FROM SERIES S WHERE S.PTID = 3) C
WHERE A.PID = B.PID AND A.PID = C.PID AND P.PID = A.PID;

# c) Print the 10 most-reprinted characters from Alan Moore's stories. #RUN

SELECT C.NAME
FROM CHARACTER C, STORY_CHARACTER_RELATIONSHIP SCRS, (SELECT DISTINCT SR.ORIGIN_ID 
														FROM STORY_REPRINT SR, (SELECT SSRS.SID 
																				FROM ARTIST A, STORY_SCRIPT_RELATIONSHIP SSRS 
																				WHERE A.NAME LIKE '%Alan Moore%' AND A.AID = SSRS.AID) A
														WHERE A.SID = SR.ORIGIN_ID
														GROUP BY SR.ORIGIN_ID
														ORDER BY COUNT(SR.ORIGIN_ID) DESC
														OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY) B
WHERE B.ORIGIN_ID = SCRS.SID AND SCRS.N_ID = C.N_ID AND SCRS.CID = C.CID;



# d) Print the writers of nature-related stories that have also done the pencilwork in all their nature-related stories. #RUN

SELECT DISTINCT AR.NAME
FROM STORY_SCRIPT_RELATIONSHIP SSRS, STORY_PENCIL_RELATIONSHIP SPRS, ARTIST AR, (SELECT SGRS.SID
                                                                      FROM STORY_GENRE_RELATIONSHIP SGRS, (SELECT G.GID FROM GENRE G WHERE G.NAME = 'Nature') A
                                                                      WHERE A.GID = SGRS.GID) B
WHERE B.SID = SSRS.SID AND B.SID = SPRS.SID AND AR.AID = SSRS.AID;


# e) For each of the top-10 publishers in terms of published series, print the 3 most popular languages of their series.  #WRONG 

SELECT L.NAME, COUNT(L.NAME) AS NUM 
FROM SERIES S,  ( SELECT p.Pid 
                          FROM SERIES S, PUBLISHER P
                          WHERE S.Pid = p.Pid 
                          GROUP BY p.Pid
                          ORDER BY COUNT(p.Pid) DESC
                          OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY)A, LANGUAGE L
WHERE A.Pid = s.Pid AND L.LID = S.Lid 
GROUP BY L.NAME 
ORDER BY NUM DESC
OFFSET 0 ROWS FETCH NEXT 3 ROWS ONLY;

# f) Print the languages that have more than 10000 original stories published in magazines, along with the number of those stories. # WRONG 

SELECT SR.ORIGIN_ID, COUNT(SR.ORIGIN_ID)
FROM STORY_REPRINT SR,  STORY S, (SELECT I.IID 
                                  FROM Publication_Type PT, SERIES SE, ISSUE I 
                                    WHERE PT.name LIKE '%magazine%' AND SE.PTID = PT.PTID AND SE.SID = I.SID) A
WHERE A.IID = S.IID
GROUP BY SR.ORIGIN_ID
HAVING COUNT(SR.ORIGIN_ID) >1000; 

#######

SELECT L.name, A.count
FROM Language L
JOIN (SELECT SE.lid, COUNT(SE.lid) as count
	  FROM SERIES SE
	  JOIN (SELECT ptid as mid
      		FROM PUBLICATION_TYPE
      		WHERE name='magazine')
	  ON SE.ptid=mid
	  JOIN Issue I
	  ON I.sid=SE.sid
	  JOIN Story S
	  ON S.iid=I.iid
	  JOIN Story_Reprint SR
	  ON S.sid=SR.origin_id
	  GROUP BY SE.lid
	  HAVING COUNT(SE.lid)>100) A
ON A.lid=L.lid

# g) Print all story types that have not been published as a part of Italian magazine series. #RUN

SELECT DISTINCT ST.NAME
FROM STORY_TYPE ST, (SELECT S.STID
					FROM STORY S, (SELECT I.IID
									FROM ISSUE I, (SELECT S.SID
													FROM SERIES S, (SELECT PT.PTID, C.CID
																	FROM PUBLICATION_TYPE PT, COUNTRY C
																	WHERE PT.NAME = 'magazine' AND C.NAME = 'Italy') A
													WHERE A.PTID != S.PTID AND A.CID != S.CID) B
									WHERE B.SID = I.SID) C
					WHERE C.IID = S.IID) D
WHERE D.STID = ST.STID;

# h) Print the writers of cartoon stories who have worked as writers for more than one indicia publisher. #WRONG

Select SSRS.AID 
FROM STORY_TYPE ST, STORY S, STORY_SCRIPT_RELATIONSHIP SSRS 
WHERE ST.NAME = 'cartoon' AND ST.STID=S.STID AND SSRS.SID = S.SID;

################
Select SSRS.AID, COUNT(SSRS.AID)
FROM STORY_SCRIPT_RELATIONSHIP SSRS
INNER JOIN STORY S ON S.iid=I.orig_id
INNER JOIN Indicia_Publisher IP ON IP.ipid=S.ipid
WHERE SSRS.SID=IP.SID AND IP.STID=(SELECT ST.STID FROM STORY_TYPE ST WHERE ST.NAME='cartoon') 
GROUP BY SSRS.AID
HAVING COUNT(SSRS.AID)>1



# i) Print the 10 brand groups with the highest number of indicia publishers. #RUN

SELECT BG.name 
FROM (SELECT BG.bgid
      FROM Brand_Group BG 
      JOIN Indicia_Publisher IP
      ON BG.pid=IP.pid
      GROUP BY BG.bgid
      ORDER BY COUNT(BG.bgid) DESC
      OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY) A
JOIN Brand_Group BG
ON BG.bgid=A.bgid;

# j) Print the average series length (in terms of years) per indicia publisher. #RUN 
SELECT IP.IPID, ROUND (AVG(S.YEAR_ENDED - S.YEAR_BEGAN))
FROM INDICIA_PUBLISHER IP, SERIES S
WHERE S.PID = IP.PID
GROUP BY IP.IPID

# k) Print the top 10 indicia publishers that have published the most single-issue series. #WRONG

SELECT IP.IPID
FROM INDICIA_PUBLISHER IP,  ( SELECT S.PID, COUNT (S.SID)
								FROM SERIES S, (SELECT I.SID
												FROM ISSUE I 
												GROUP BY I.SID 
												HAVING COUNT (I.SID) < 2) A
								WHERE A.SID = S.SID 
								GROUP BY S.PID
								ORDER BY COUNT (S.SID) DESC
								OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY) B
WHERE B.PID = IP.PID;

# l) Print the 10 indicia publishers with the highest number of script writers in a single story. #WRONG

SELECT I.IPID
FROM ISSUE I, (SELECT S.IID
				FROM STORY S,(SELECT SSRS.SID
								FROM STORY_SCRIPT_RELATIONSHIP SSRS
								GROUP BY SSRS.SID
								ORDER BY COUNT(SSRS.AID) DESC
								OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY) A
				WHERE A.SID = S.SID) B
WHERE B.IID = I.IID;

# m) Print all Marvel heroes that appear in Marvel-DC story cross overs. #RUN 

SELECT DISTINCT C.NAME 
FROM PUBLISHER P, INDICIA_PUBLISHER IP, ISSUE I, STORY S, STORY_CHARACTER_RELATIONSHIP SCRS, CHARACTER C 
WHERE P.NAME LIKE '%DC%' AND P.NAME LIKE '%Marvel%' AND IP.PID = P.PID AND I.IPID = IP.IPID AND S.IID = I.IID AND SCRS.SID = S.SID AND C.CID = SCRS.CID AND SCRS.N_ID = C.N_ID AND SCRS.IS_FEATURE = 'TRUE';

# n) Print the top 5 series with most issues #RUN

SELECT I.SID, COUNT(I.IID) AS NUM_OF_ISSUES 
FROM ISSUE I
GROUP BY I.SID
ORDER BY COUNT (I.IID) DESC
OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY;

# o) Given an issue, print its most reprinted story. #RUN

SELECT DISTINCT S.IID, COUNT(SR.ORIGIN_ID), S.SID 
FROM STORY S, STORY_REPRINT SR 
WHERE SR.ORIGIN_ID = S.SID
GROUP BY S.IID, S.SID
ORDER BY COUNT (SR.ORIGIN_ID) DESC

SELECT S.TITLE 
FROM STORY S, (SELECT SR.ORIGIN_ID
				FROM STORY S, STORY_REPRINT SR 
				WHERE SR.ORIGIN_ID = S.SID AND S.IID = 13646       # GIVEN IID 13646 
				GROUP BY SR.ORIGIN_ID
				ORDER BY COUNT (SR.ORIGIN_ID)
				OFFSET 0 ROWS FETCH NEXT 1 ROW ONLY) A
WHERE A.ORIGIN_ID = S.SID;



