# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, ForeignKeyConstraint, Integer, String, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Bezirk(Base):
    __tablename__ = 'bezirk'

    nummer = Column(Integer, primary_key=True, server_default=text("'0'"))
    wknr = Column(ForeignKey('wahlkreis.nummer'), index=True)
    bezeichnung = Column(String(255))

    wahlkreis = relationship('Wahlkreis')


class Hochrechnung(Base):
    __tablename__ = 'hochrechnung'

    whnr = Column(ForeignKey('wahl.nummer'), primary_key=True, nullable=False, index=True, server_default=text("'0'"))
    zeitpunkt = Column(Time, primary_key=True, nullable=False, server_default=text("'00:00:00'"))

    wahl = relationship('Wahl')


class Hrergebnis(Base):
    __tablename__ = 'hrergebnis'
    __table_args__ = (
        ForeignKeyConstraint(['whnr', 'zeitpunkthochrechnung'], ['hochrechnung.whnr', 'hochrechnung.zeitpunkt']),
    )

    whnr = Column(Integer, primary_key=True, nullable=False, server_default=text("'0'"))
    prozent = Column(Float)
    zeitpunkthochrechnung = Column(Time, primary_key=True, nullable=False, server_default=text("'00:00:00'"))
    parteinr = Column(ForeignKey('partei.nummer'), primary_key=True, nullable=False, index=True, server_default=text("'0'"))

    partei = relationship('Partei')
    hochrechnung = relationship('Hochrechnung')


class Kandidatur(Base):
    __tablename__ = 'kandidatur'

    listenplatz = Column(Integer)
    whnr = Column(ForeignKey('wahl.nummer'), primary_key=True, nullable=False, server_default=text("'0'"))
    wknr = Column(ForeignKey('wahlkreis.nummer'), primary_key=True, nullable=False, index=True, server_default=text("'0'"))
    parteinr = Column(ForeignKey('partei.nummer'), primary_key=True, nullable=False, index=True, server_default=text("'0'"))

    partei = relationship('Partei')
    wahl = relationship('Wahl')
    wahlkreis = relationship('Wahlkreis')


class Partei(Base):
    __tablename__ = 'partei'

    nummer = Column(Integer, primary_key=True)
    bezeichnung = Column(String(10))
    langbez = Column(String(255))


class Sprengel(Base):
    __tablename__ = 'sprengel'

    nummer = Column(Integer, primary_key=True, nullable=False)
    bznr = Column(ForeignKey('bezirk.nummer'), primary_key=True, nullable=False, index=True, server_default=text("'0'"))
    whnr = Column(ForeignKey('wahl.nummer'), primary_key=True, nullable=False, index=True, server_default=text("'0'"))
    wahlberechtigte = Column(Integer)
    ungueltige = Column(Integer)
    abgegebene = Column(Integer)

    bezirk = relationship('Bezirk')
    wahl = relationship('Wahl')


class Stimmen(Base):
    __tablename__ = 'stimmen'

    anzahl = Column(Integer)
    parteinr = Column(ForeignKey('partei.nummer'), primary_key=True, nullable=False, index=True, server_default=text("'0'"))
    spnr = Column(ForeignKey('sprengel.nummer'), primary_key=True, nullable=False, server_default=text("'0'"))
    bznr = Column(ForeignKey('bezirk.nummer'), primary_key=True, nullable=False, index=True, server_default=text("'0'"))
    whnr = Column(ForeignKey('wahl.nummer'), primary_key=True, nullable=False, index=True, server_default=text("'0'"))

    bezirk = relationship('Bezirk')
    partei = relationship('Partei')
    sprengel = relationship('Sprengel')
    wahl = relationship('Wahl')


class Wahl(Base):
    __tablename__ = 'wahl'

    nummer = Column(Integer, primary_key=True)
    termin = Column(Date, nullable=False)
    mandate = Column(Integer)


class Wahlkreis(Base):
    __tablename__ = 'wahlkreis'

    nummer = Column(Integer, primary_key=True, server_default=text("'0'"))
    bezeichnung = Column(String(255))


class Wahlstimmen(Base):
    __tablename__ = 'wahlstimmen'

    whnr = Column(ForeignKey('wahl.nummer'), primary_key=True, nullable=False, server_default=text("'0'"))
    parteinr = Column(ForeignKey('partei.nummer'), primary_key=True, nullable=False, index=True, server_default=text("'0'"))
    gesstimmen = Column(Integer)

    partei = relationship('Partei')
    wahl = relationship('Wahl')
