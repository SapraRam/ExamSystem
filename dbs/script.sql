CREATE TABLE if not exists Question(
   qid int,
   question TEXT,
   option1  TEXT,
   option2  TEXT,
   option3  TEXT,
   option4  TEXT,
   answer   TEXT
);

CREATE TABLE if not exists Test(
   tid int,
   name Text,
   created Text,
   creator Text
);

CREATE TABLE if not exists TestPaper(
   tid int,
   qid int,
   FOREIGN KEY (tid) REFERENCES Test(tid),
   FOREIGN KEY (qid) REFERENCES Question(qid)
);

INSERT INTO Question
VALUES(1,'Q1','Opt1-q1','Opt2-q1','Opt3-q1','Opt4-q1','1-0-1-1');
INSERT INTO Question
VALUES(2,'Q2','Opt1-q2','Opt2-q2','Opt3-q2','Opt4-q2','1-0-0-0');
INSERT INTO Question
VALUES(3,'Q3','Opt1-q3','Opt2-q3','Opt3-q3','Opt4-q3','1-0-1-1');
INSERT INTO Question
VALUES(4,'Q4','Opt1-q4','Opt2-q4','Opt3-q4','Opt4-q4','1-0-0-0');
INSERT INTO Question
VALUES(5,'Q5','Opt1-q5','Opt2-q5','Opt3-q5','Opt4-q5','1-1-1-1');
INSERT INTO Question
VALUES(6,'Q6','Opt1-q6','Opt2-q6','Opt3-q6','Opt4-q6','1-1-0-0');
INSERT INTO Question
VALUES(7,'Q7','Opt1-q7','Opt2-q7','Opt3-q7','Opt4-q7','1-0-1-1');
INSERT INTO Question
VALUES(8,'Q8','Opt1-q8','Opt2-q8','Opt3-q8','Opt4-q8','1-0-0-0');
INSERT INTO Question
VALUES(9,'Q9','Opt1-q9','Opt2-q9','Opt3-q9','Opt4-q9','1-0-1-1');
INSERT INTO Question
VALUES(10,'Q10','Opt1-q10','Opt2-q10','Opt3-q10','Opt4-q10','1-0-0-0');
INSERT INTO Question
VALUES(11,'Q11','Opt1-q11','Opt2-q11','Opt3-q11','Opt4-q11','1-1-1-1');
INSERT INTO Question
VALUES(12,'Q12','Opt1-q12','Opt2-q12','Opt3-q12','Opt4-q12','1-1-0-0');
INSERT INTO Question
VALUES(13,'Q13','Opt1-q13','Opt2-q13','Opt3-q13','Opt4-q13','1-1-0-0');
INSERT INTO Question
VALUES(14,'Q14','Opt1-q14','Opt2-q14','Opt3-q14','Opt4-q14','1-1-0-0');

INSERT INTO Test
VALUES (1, 'Test1', date('now', 'start of year'), 'amit');
INSERT INTO Test
VALUES (2, 'Test2', date('now', 'start of year', '+1 month'), 'rahul');
INSERT INTO Test
VALUES (3, 'Test3', date('now', 'start of year', '+2 months'), 'prashant');
INSERT INTO Test
VALUES (4, 'Test4', date('now', 'start of year', '+3 months'), 'kajal');

INSERT INTO TestPaper VALUES(1,1);
INSERT INTO TestPaper VALUES(1,2);
INSERT INTO TestPaper VALUES(1,3);
INSERT INTO TestPaper VALUES(1,4);
INSERT INTO TestPaper VALUES(1,5);
INSERT INTO TestPaper VALUES(1,6);
INSERT INTO TestPaper VALUES(2,4);
INSERT INTO TestPaper VALUES(2,5);
INSERT INTO TestPaper VALUES(2,6);
INSERT INTO TestPaper VALUES(2,7);
INSERT INTO TestPaper VALUES(2,8);
INSERT INTO TestPaper VALUES(2,9);
INSERT INTO TestPaper VALUES(3,7);
INSERT INTO TestPaper VALUES(3,8);
INSERT INTO TestPaper VALUES(3,9);
INSERT INTO TestPaper VALUES(3,10);
INSERT INTO TestPaper VALUES(3,11);
INSERT INTO TestPaper VALUES(3,12);
