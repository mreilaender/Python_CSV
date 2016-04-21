USE insy_wahl;
DROP TABLE IF EXISTS hrergebnis, hochrechnung, wahlstimmen, kandidatur, stimmen, partei, sprengel, bezirk, wahlkreis, wahl;

CREATE TABLE wahl (
  nummer INTEGER AUTO_INCREMENT,
  termin DATE NOT NULL,
  mandate INTEGER,
  PRIMARY KEY (nummer)
);

CREATE TABLE wahlkreis (
  nummer INTEGER,
  bezeichnung VARCHAR(255),
  PRIMARY KEY (nummer)
);

CREATE TABLE bezirk (
  nummer INTEGER,
  wknr INTEGER,
  bezeichnung VARCHAR(255),
  PRIMARY KEY(nummer),
  FOREIGN KEY(wknr) REFERENCES wahlkreis (nummer)
);

CREATE TABLE sprengel (
  nummer INTEGER NOT NULL,
  bznr INTEGER,
  whnr INTEGER,
  wahlberechtigte INTEGER,
	ungueltige INTEGER,
	abgegebene INTEGER,
  PRIMARY KEY (nummer, bznr, whnr),
  FOREIGN KEY(bznr) REFERENCES bezirk (nummer),
  FOREIGN KEY(whnr) REFERENCES wahl (nummer)
);

CREATE TABLE partei (
  nummer INTEGER AUTO_INCREMENT,
  bezeichnung VARCHAR(10),
  langbez VARCHAR(255),
  PRIMARY KEY (nummer)
);

CREATE TABLE stimmen (
  anzahl INTEGER,
  parteinr INTEGER,
  spnr INTEGER,
  bznr INTEGER,
  whnr INTEGER,
  PRIMARY KEY (spnr, bznr, whnr, parteinr),
  FOREIGN KEY(spnr) REFERENCES sprengel (nummer),
  FOREIGN KEY(bznr) REFERENCES bezirk (nummer),
  FOREIGN KEY(whnr) REFERENCES wahl (nummer),
  FOREIGN KEY(parteinr) REFERENCES partei (nummer)
);

CREATE TABLE kandidatur (
  listenplatz INTEGER,
  whnr INTEGER,
  wknr INTEGER,
  parteinr INTEGER,
  PRIMARY KEY (whnr, wknr, parteinr),
  FOREIGN KEY(whnr) REFERENCES wahl (nummer),
  FOREIGN KEY(wknr) REFERENCES wahlkreis (nummer),
  FOREIGN KEY(parteinr) REFERENCES partei (nummer)
);

CREATE TABLE wahlstimmen (
  whnr INTEGER,
  parteinr INTEGER,
  gesstimmen INTEGER,
  PRIMARY KEY (whnr, parteinr),
  FOREIGN KEY(whnr) REFERENCES wahl (nummer),
  FOREIGN KEY(parteinr) REFERENCES partei (nummer)
);

CREATE TABLE hochrechnung (
  whnr INTEGER,
  zeitpunkt TIME,
  PRIMARY KEY(zeitpunkt, whnr),
  FOREIGN KEY(whnr) REFERENCES wahl(nummer)
);

CREATE TABLE hrergebnis (
  whnr INTEGER,
  prozent FLOAT,
  zeitpunkthochrechnung TIME,
  parteinr INTEGER,
  PRIMARY KEY(whnr, zeitpunkthochrechnung, parteinr),
  FOREIGN KEY(whnr, zeitpunkthochrechnung) REFERENCES hochrechnung (whnr, zeitpunkt),
  FOREIGN KEY(parteinr) REFERENCES partei (nummer)
);

DROP TABLE IF EXISTS test;
CREATE TABLE test (
  test INT,
  zeitpunkthochrechnung TIME,
  PRIMARY KEY (test)
);

-- INSERTs

INSERT INTO wahl(termin, mandate) VALUES('2015-10-11', 100);

INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (0, 'Briefwahl');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (1, 'Wahlkreis Zentrum');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (2, 'Wahlkreis Innen-West');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (3, 'Wahlkreis Leopoldstadt');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (4, 'Wahlkreis Landstrasse');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (5, 'Wahlkreis Favoriten');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (6, 'Wahlkreis Simmering');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (7, 'Wahlkreis Meidling');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (8, 'Wahlkreis Hietzing');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (9, 'Wahlkreis Penzing');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (10, 'Wahlkreis Rudolfsheim-Fuenfhaus');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (11, 'Wahlkreis Ottakring');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (12, 'Wahlkreis Hernals');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (13, 'Wahlkreis Waehring');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (14, 'Wahlkreis Doebling');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (15, 'Wahlkreis Brigittenau');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (16, 'Wahlkreis Floridsdorf');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (17, 'Wahlkreis Donaustadt');
INSERT INTO wahlkreis (nummer, bezeichnung) VALUES (18, 'Wahlkreis Liesing');

INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (1, 1, 'Innere Stadt');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (2, 3, 'Leopoldstadt');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (3, 4, 'Landstrasse');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (4, 1, 'Wieden');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (5, 1, 'Margareten');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (6, 1, 'Mariahilf');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (7, 2, 'Neubau');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (8, 2, 'Josefstadt');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (9, 2, 'Alsergrund');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (10, 5, 'Favoriten');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (11, 6, 'Simmering');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (12, 7, 'Meidling');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (13, 8, 'Hietzing');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (14, 9, 'Penzing');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (15, 10, 'Rudolfsheim-Fuenfhaus');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (16, 11, 'Ottakring');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (17, 12, 'Hernals');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (18, 13, 'Waehring');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (19, 14, 'Doebling');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (20, 15, 'Brigittenau');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (21, 16, 'Floridsdorf');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (22, 17, 'Donaustadt');
INSERT INTO bezirk (nummer, wknr, bezeichnung) VALUES (23, 18, 'Liesing');

INSERT INTO partei (bezeichnung, langbez) VALUES ('SPOE','Soziale Partei Oesterreich');
INSERT INTO partei (bezeichnung, langbez) VALUES ('FPOE','Freiheitliche Partei Oesterreich');
INSERT INTO partei (bezeichnung, langbez) VALUES ('OEVP','Oesterreichische Volks Partei');
INSERT INTO partei (bezeichnung, langbez) VALUES ('GRUE','Gruene Partei Oesterreichs');
INSERT INTO partei (bezeichnung, langbez) VALUES ('NEOS','Das Neue Oesterreich und Liberales Forum');
INSERT INTO partei (bezeichnung, langbez) VALUES ('WWW','Wir Wollen Wahlfreiheit');
INSERT INTO partei (bezeichnung, langbez) VALUES ('ANDAS','Wien anders');
INSERT INTO partei (bezeichnung, langbez) VALUES ('GFW','Gemeinsam fuer Wien');
INSERT INTO partei (bezeichnung, langbez) VALUES ('SLP','Sozialistische Links Partei');
INSERT INTO partei (bezeichnung, langbez) VALUES ('WIFF','Wir fuer Floridsdorf');
INSERT INTO partei (bezeichnung, langbez) VALUES ('M','Maennerpartei - fuer ein faires Miteinander');
INSERT INTO partei (bezeichnung, langbez) VALUES ('FREIE','Freidemokraten');

-- Generated with Python v2.7.10
-- Parteien, die in allen Wahlkreisen kandidieren:
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(1,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(1,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(1,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(1,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(1,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(1,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(1,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(1,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(2,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(2,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(2,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(2,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(2,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(2,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(2,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(2,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(3,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(3,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(3,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(3,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(3,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(3,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(3,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(3,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(4,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(4,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(4,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(4,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(4,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(4,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(4,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(4,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(5,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(5,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(5,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(5,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(5,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(5,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(5,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(5,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(6,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(6,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(6,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(6,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(6,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(6,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(6,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(6,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(7,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(7,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(7,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(7,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(7,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(7,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(7,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(7,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(8,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(8,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(8,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(8,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(8,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(8,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(8,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(8,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(9,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(9,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(9,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(9,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(9,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(9,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(9,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(9,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(10,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(10,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(10,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(10,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(10,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(10,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(10,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(10,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(11,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(11,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(11,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(11,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(11,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(11,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(11,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(11,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(12,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(12,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(12,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(12,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(12,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(12,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(12,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(12,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(13,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(13,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(13,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(13,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(13,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(13,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(13,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(13,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(14,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(14,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(14,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(14,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(14,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(14,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(14,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(14,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(15,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(15,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(15,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(15,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(15,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(15,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(15,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(15,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(16,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(16,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(16,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(16,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(16,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(16,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(16,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(16,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(17,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(17,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(17,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(17,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(17,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(17,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(17,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(17,1,8,8);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(18,1,1,1);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(18,1,2,2);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(18,1,3,3);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(18,1,4,4);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(18,1,5,5);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(18,1,6,6);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(18,1,7,7);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(18,1,8,8);

-- Parteien, die nur in bestimmten Wahlkreisen kandidieren:
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(1,1,12,12);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(15,1,9,9);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(16,1,10,10);
INSERT INTO kandidatur(wknr, whnr, parteinr, listenplatz) VALUES(17,1,11,11);

-- Trigger

DELIMITER //
CREATE TRIGGER trigger_stimmen_insert AFTER INSERT ON stimmen FOR EACH ROW
BEGIN
	IF (SELECT whnr FROM wahlstimmen WHERE whnr = NEW.whnr AND parteinr = NEW.parteinr) THEN
		UPDATE wahlstimmen SET gesstimmen = gesstimmen + NEW.anzahl WHERE whnr=NEW.whnr AND parteinr=NEW.parteinr;
	ELSE
		INSERT INTO wahlstimmen VALUES(NEW.whnr, NEW.parteinr, NEW.anzahl);
	END IF;
END;//
DELIMITER ;

DELIMITER //
CREATE TRIGGER trigger_stimmen_update AFTER UPDATE ON stimmen FOR EACH ROW
BEGIN
	UPDATE wahlstimmen SET gesstimmen = gesstimmen + (NEW.anzahl - OLD.anzahl) WHERE whnr=NEW.whnr AND parteinr=NEW.parteinr;
END;//
DELIMITER ;

DELIMITER //
CREATE TRIGGER trigger_stimmen_delete AFTER DELETE ON stimmen FOR EACH ROW
BEGIN
	UPDATE wahlstimmen SET gesstimmen = gesstimmen - OLD.anzahl WHERE whnr=OLD.whnr AND parteinr=OLD.parteinr;
END;//
DELIMITER ;

-- Stored Routine

DROP PROCEDURE IF EXISTS erzeugeHochrechnung;
DELIMITER //
CREATE PROCEDURE erzeugeHochrechnung(IN whnr INT, IN zeitpunkt TIME)
BEGIN
	DECLARE totalStimmen INT DEFAULT 0;
	DECLARE n INT DEFAULT 0;
	DECLARE i INT DEFAULT 0;

	INSERT INTO hochrechnung VALUES(whnr, zeitpunkt);

	SELECT SUM(gesstimmen) FROM wahlstimmen INTO totalStimmen;
	SELECT COUNT(*) FROM partei INTO n;
	SET i=1;
	WHILE i<=n DO
    INSERT INTO test VALUES (i, zeitpunkt);
		INSERT INTO hrergebnis VALUES(whnr, COALESCE((SELECT gesstimmen FROM wahlstimmen WHERE whnr = whnr AND parteinr = i)/totalStimmen * 100, 0), zeitpunkt, i);
		SET i = i + 1;
	END WHILE;
END; //
DELIMITER ;
