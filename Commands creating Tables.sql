# Entities

CREATE TABLE Story 	(sid INTEGER,
					title VARCHAR(400),
					editing VARCHAR(1000), 
					synopsis VARCHAR(4000),
					reprint_notes VARCHAR(2500),
					notes VARCHAR(4000),
					stid INTEGER NOT NULL,
					iid INTEGER NOT NULL,
					PRIMARY KEY (sid),
					FOREIGN KEY (stid) REFERENCES Story_Type(stid),
					FOREIGN KEY (iid) REFERENCES Issue(iid));

CREATE TABLE Issue 	(iid INTEGER,
					num VARCHAR(100),
					publication_year INTEGER,
					publication_month INTEGER,
					publication_day INTEGER,
					amount FLOAT(126),
					currency VARCHAR(50),
					page_count INTEGER,
					indicia_frequency VARCHAR(500),
					editing VARCHAR(1000),
					notes VARCHAR(4000),
					isbn VARCHAR(50),
					valid_isbn VARCHAR(13),
					barcode INTEGER,
					title VARCHAR(1000),
					on_sale_year INTEGER,
					on_sale_month INTEGER,
					on_sale_day INTEGER,
					rating VARCHAR(500),
					ipid INTEGER,
					sid INTEGER NOT NULL,
					PRIMARY KEY(iid),
					FOREIGN KEY (ipid) REFERENCES Indicia_Publisher(ipid),
					FOREIGN KEY (sid) REFERENCES Series(sid));					

CREATE TABLE Series (sid INTEGER,
					name VARCHAR(400) NOT NULL,
					format VARCHAR(200),
					year_began INTEGER,
					year_ended INTEGER,
					pub_start_year INTEGER,
					pub_start_month INTEGER,
					pub_start_day INTEGER,
					pub_end_year INTEGER,
					pub_end_month INTEGER,
					pub_end_day INTEGER,
					is_present VARCHAR(5),						#INSTEAD BOOLEAN 
					first_issue_id INTEGER,
					last_issue_id INTEGER,
					notes VARCHAR(4000),
					color VARCHAR(400),
					dimensions VARCHAR(400),
					paper_stock VARCHAR(400),
					binding VARCHAR(200),
					publishing_format VARCHAR(200),
					lid INTEGER NOT NULL,
					ptid INTEGER,
					cid INTEGER NOT NULL,
					pid INTEGER NOT NULL,
					PRIMARY KEY(sid),
					FOREIGN KEY(first_issue_id) REFERENCES Issue(iid),
					FOREIGN KEY(last_issue_id) REFERENCES Issue(iid),
					FOREIGN KEY(lid) REFERENCES Language(lid)
					FOREIGN KEY (ptid) REFERENCES Publication_Type(ptid)
					FOREIGN KEY (cid) REFERENCES Country(cid),
					FOREIGN KEY (pid) REFERENCES Publisher(pid));

CREATE TABLE Story_Type	(stid INTEGER,
						name VARCHAR(50),
						PRIMARY KEY (stid));

CREATE TABLE Publication_Type	(ptid INTEGER,
								 name VARCHAR(8),
								 PRIMARY KEY (ptid));

CREATE TABLE Character (cid INTEGER,
						n_id INTEGER,
					    name VARCHAR(800),
					    associated_name VARCHAR(200),
					    PRIMARY KEY(cid,n_id));

CREATE TABLE Language  	(lid INTEGER,
						code CHAR(3), 
						name VARCHAR(35),
						PRIMARY KEY (lid));

CREATE TABLE Country 	(cid INTEGER,
					  	code CHAR(4), 
					  	name VARCHAR(100),
					  	PRIMARY KEY (cid));

CREATE TABLE Publisher 	(pid INTEGER,
						name VARCHAR(200) NOT NULL,
						year_began INTEGER,
						year_ended INTEGER,
						notes VARCHAR(4000),
						url VARCHAR(200),
						cid INTEGER,
						PRIMARY KEY(pid)
						FOREIGN KEY (cid) REFERENCES Country(cid));

CREATE TABLE Indicia_Publisher 	(ipid INTEGER,
								name VARCHAR(200) NOT NULL,
								year_began INTEGER,
								year_ended INTEGER,
								notes VARCHAR(4000),
								url VARCHAR(200),
								cid INTEGER NOT NULL,
								pid INTEGER NOT NULL,
								PRIMARY KEY(ipid),
								FOREIGN KEY (cid) REFERENCES Country(cid),
								FOREIGN KEY (pid) REFERENCES Publisher(pid));

CREATE TABLE Brand_Group 	(bgid INTEGER,
							name VARCHAR(200) NOT NULL,
							year_began INTEGER,
							year_ended INTEGER,
							notes VARCHAR(1000),
							url VARCHAR(200),
							pid INTEGER NOT NULL,
							PRIMARY KEY(bgid),
							FOREIGN KEY (pid) REFERENCES Publisher(pid));

CREATE TABLE Genre (gid INTEGER,
					name VARCHAR(30),
					PRIMARY KEY(gid));

CREATE TABLE Artist (aid INTEGER,
					name VARCHAR(200),
					PRIMARY KEY(aid));

# Relationships

CREATE TABLE Story_Ink_Relationship (aid INTEGER,
									sid INTEGER,
									FOREIGN KEY (aid) REFERENCES Artist(aid),
									FOREIGN KEY (sid) REFERENCES Story(sid),
									PRIMARY KEY (aid,sid));

CREATE TABLE Story_Pencil_Relationship (aid INTEGER,
										sid INTEGER,
										FOREIGN KEY (aid) REFERENCES Artist(aid),
										FOREIGN KEY (sid) REFERENCES Story(sid),
										PRIMARY KEY (aid,sid));

CREATE TABLE Story_Script_Relationship (aid INTEGER,
										sid INTEGER,
										FOREIGN KEY (aid) REFERENCES Artist(aid),
										FOREIGN KEY (sid) REFERENCES Story(sid),
										PRIMARY KEY (aid,sid));

CREATE TABLE Story_Letter_Relationship (aid INTEGER,
										sid INTEGER,
										FOREIGN KEY (aid) REFERENCES Artist(aid),
										FOREIGN KEY (sid) REFERENCES Story(sid),
										PRIMARY KEY (aid,sid));

CREATE TABLE Story_Color_Relationship (aid INTEGER,
										sid INTEGER,
										FOREIGN KEY (aid) REFERENCES Artist(aid),
										FOREIGN KEY (sid) REFERENCES Story(sid),
										PRIMARY KEY (aid,sid));

CREATE TABLE Story_Reprint 	(srid INTEGER,
							origin_id INTEGER NOT NULL,
							target_id INTEGER NOT NULL,
							PRIMARY KEY (srid),
							FOREIGN KEY (origin_id) REFERENCES Story(sid),
							FOREIGN KEY (target_id) REFERENCES Story(sid));

CREATE TABLE Issue_Reprint 	(irid INTEGER,
							origin_issue_id INTEGER NOT NULL, 
							target_issue_id INTEGER NOT NULL,
							PRIMARY KEY (irid),
							FOREIGN KEY (origin_issue_id) REFERENCES Issue(iid),			 
							FOREIGN KEY (target_issue_id) REFERENCES Issue(iid));			


CREATE TABLE Story_Genre_Relationship (gid INTEGER,
									   sid INTEGER,
									   PRIMARY KEY(gid,sid)
									   FOREIGN KEY (gid) REFERENCES Genre(gid)
									   FOREIGN KEY sid REFERENCES Story(sid));


CREATE TABLE Story_Character_Relationship 	(cid INTEGER,
											n_id INTEGER,
					    					sid INTEGER,
					    				  	is_feature VARCHAR(5),			#INSTEAD OF BOOLEAN
					    					PRIMARY KEY(cid, sid, n_id)
					    					FOREIGN KEY (cid, n_id) REFERENCES Character(cid, n_id)
					    					FOREIGN KEY sid REFERENCES Story(sid));s

