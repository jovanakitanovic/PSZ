select * from dbo.CarAdds

select * from dbo.CarAds where marka='ford'

select marka, COUNT(marka) as 'broj automobila' from dbo.CarAds group by marka

select 'Beograd' as 'Oglasi iz Beograda', count(ads.lokacija) as 'broj automobila' from dbo.CarAds as ads where ads.lokacija in ('Železnik','Šimanovci','Železnik',
'Žarkovo','Altina','BanovoBrdo','Becmen','BeleVode','Bogoslovija','BraceJerkovic','CrveniKrst','Cukarica','Dobanovci','Dorcol','Kaluderica','KanarevoBrdo',
'Karaburma','Kotež','Krnjaca','Kumodraž','MaliMokriLug','Medakovic','Meljak','Padina','PetlovoBrdo','Rakovica','Ralja','Resnik','Ripanj','Rušanj','StariGrad',
'Surcin','Vidikovac','Voždovac','VojvodaStepa','ZemunPolje','Zvezdara','Zuce','VišnjickaBanja','SavskiVenac','Ovca','NoviBeograd','Mirijevo','Zemun','Jajinci','Cerak','Beograd')


select ads.lokacija, count(ads.lokacija) as 'broj automobila' from dbo.CarAds as ads group by ads.lokacija 

select  link as 'broj automobila' from dbo.CarAdds where lokacija='BraceJerkovic' 

select boja, COUNT(boja) as 'broj automobila' from dbo.CarAds group by boja

select top(30) marka, model, cena, godiste, kilometraza, karoserija, kubikaza, snagaMotora from dbo.CarAds order by cena desc

select top(30) marka, model, cena, godiste, kilometraza, karoserija, kubikaza, snagaMotora from dbo.CarAds where karoserija='Džip/SUV' order by cena desc

select top(30) * from dbo.CarAds where karoserija='Džip/SUV' order by cena desc


select marka, model, cena, godiste, kilometraza, karoserija, kubikaza, snagaMotora  from dbo.CarAds where godiste=2021 or godiste = 2022 order by cena desc


select * from Cars where kubikaza>7000 order by kubikaza desc

update Cars set kubikaza=1168 where id=20024

select * from Cars where id=16969

select * from dbo.CarAds where marka='Opel' order by godiste desc

select AVG(cena) from dbo.CarAds where model='C 180' 
select * from dbo.CarAds where model='Stelvio'

select * from dbo.CarAds where marka='jaguar'

select * from dbo.CarAds where kilometraza='130'

select marka, model, cena, godiste, kilometraza, karoserija, kubikaza, snagaMotora from dbo.CarAds where link='https://www.polovniautomobili.com/auto-oglasi/19912488/opel-astra-k-16-cdti-136-navled?attp=p0_pv0_pc0_pl1_plv0' or link = 'https://www.polovniautomobili.com/auto-oglasi/19945051/mercedes-benz-c-180-rata-od-380e?attp=p0_pv0_pc0_pl1_plv0'

select top(1) * from dbo.CarAds where LEN(snagaMotora)>14 order by snagaMotora desc

select top(1) * from dbo.CarAds  order by kilometraza desc

----------------------------------------------------------------------------------------------------------

drop table #NajzastupljenijeLokacije

CREATE TABLE #NajzastupljenijeLokacije
(
	lokacija VARCHAR(50),
	brojVozila int,
)

insert into #NajzastupljenijeLokacije 
select top (12) ads.lokacija, count(ads.lokacija) from dbo.CarAds as ads group by ads.lokacija order by COUNT(ads.lokacija) desc

update #NajzastupljenijeLokacije set brojVozila = (select  count(ads.lokacija) as 'broj automobila' from dbo.CarAds as ads where ads.lokacija in ('Železnik','Šimanovci','Železnik',
'Žarkovo','Altina','BanovoBrdo','Becmen','BeleVode','Bogoslovija','BraceJerkovic','CrveniKrst','Cukarica','Dobanovci','Dorcol','Kaluderica','KanarevoBrdo',
'Karaburma','Kotež','Krnjaca','Kumodraž','MaliMokriLug','Medakovic','Meljak','Padina','PetlovoBrdo','Rakovica','Ralja','Resnik','Ripanj','Rušanj','StariGrad',
'Surcin','Vidikovac','Voždovac','VojvodaStepa','ZemunPolje','Zvezdara','Zuce','VišnjickaBanja','SavskiVenac','Ovca','NoviBeograd','Mirijevo','Zemun','Jajinci','Cerak','Beograd')) where lokacija='Beograd'

delete from #NajzastupljenijeLokacije where lokacija='Zemun'
delete from #NajzastupljenijeLokacije where lokacija='NoviBeograd'

select * from #NajzastupljenijeLokacije

----------------------------------------------------------------------------------------------------------

drop table #brojAutomobilaPoKilometraži

CREATE TABLE #brojAutomobilaPoKilometraži
(
	klasa VARCHAR(50),
	brojVozila int,
)

insert into #brojAutomobilaPoKilometraži
select 'manje od 50 000', COUNT(kilometraza) from dbo.CarAds where kilometraza <50

insert into #brojAutomobilaPoKilometraži
select '50 000 do 100 000', COUNT(kilometraza) from dbo.CarAds where kilometraza >=50 and kilometraza <100

insert into #brojAutomobilaPoKilometraži
select '100 000 do 150 000', COUNT(kilometraza) from dbo.CarAds where kilometraza >=100 and kilometraza <150

insert into #brojAutomobilaPoKilometraži
select '150 000 do 200 000', COUNT(kilometraza) from dbo.CarAds where kilometraza >=150 and kilometraza <200

insert into #brojAutomobilaPoKilometraži
select '200 000 do 250 000', COUNT(kilometraza) from dbo.CarAds where kilometraza >=200 and kilometraza <250

insert into #brojAutomobilaPoKilometraži
select '250 000 do 300 000', COUNT(kilometraza) from dbo.CarAds where kilometraza >=250 and kilometraza <300

insert into #brojAutomobilaPoKilometraži
select 'preko 300 000', COUNT(kilometraza) from dbo.CarAds where kilometraza >=300

select * from #brojAutomobilaPoKilometraži

----------------------------------------------------------------------------------------------------------

drop table #brojAutomobilaPoGodiniProizvodnje

CREATE TABLE #brojAutomobilaPoGodiniProizvodnje
(
	klasa VARCHAR(50),
	brojVozila int,
)

insert into #brojAutomobilaPoGodiniProizvodnje
select 'starije od 1960', COUNT(godiste) from dbo.CarAds where godiste <=1960

insert into #brojAutomobilaPoGodiniProizvodnje
select '1960 do 1970', COUNT(godiste) from dbo.CarAds where godiste >1960 and godiste<=1970

insert into #brojAutomobilaPoGodiniProizvodnje
select '1970 do 1980', COUNT(godiste) from dbo.CarAds where godiste >1970 and godiste<=1980

insert into #brojAutomobilaPoGodiniProizvodnje
select '1980 do 1990', COUNT(godiste) from dbo.CarAds where godiste >1980 and godiste<=1990

insert into #brojAutomobilaPoGodiniProizvodnje
select '1990 do 2000', COUNT(godiste) from dbo.CarAds where godiste >1990 and godiste<=2000

insert into #brojAutomobilaPoGodiniProizvodnje
select '2000 do 2005', COUNT(godiste) from dbo.CarAds where godiste >2000 and godiste<=2005

insert into #brojAutomobilaPoGodiniProizvodnje
select '2005 do 2010', COUNT(godiste) from dbo.CarAds where godiste >2005 and godiste<=2010

insert into #brojAutomobilaPoGodiniProizvodnje
select '2010 do 2015', COUNT(godiste) from dbo.CarAds where godiste >2010 and godiste<=2015

insert into #brojAutomobilaPoGodiniProizvodnje
select '2015 do 2020', COUNT(godiste) from dbo.CarAds where godiste >2015 and godiste<=2020

insert into #brojAutomobilaPoGodiniProizvodnje
select '2021 do 2022', COUNT(godiste) from dbo.CarAds where godiste >2020 and godiste<=2022

select * from #brojAutomobilaPoGodiniProizvodnje

----------------------------------------------------------------------------------------------------------

drop table #brojAutomobilaPoTipuMenjaca

CREATE TABLE #brojAutomobilaPoTipuMenjaca
(
	klasa VARCHAR(50),
	brojVozila int,
)

insert into #brojAutomobilaPoTipuMenjaca
select 'manuelni', COUNT(menjac) from dbo.CarAds where menjac like'%Manuelni%'

insert into #brojAutomobilaPoTipuMenjaca
select 'automatski', COUNT(menjac) from dbo.CarAds where menjac like'%Automatski%'

select * from #brojAutomobilaPoTipuMenjaca

----------------------------------------------------------------------------------------------------------

drop table #brojAutomobilaPoCeni

CREATE TABLE #brojAutomobilaPoCeni
(
	klasa VARCHAR(50),
	brojVozila int,
)

insert into #brojAutomobilaPoCeni
select 'manje od 2000', COUNT(cena) from dbo.CarAds where cena <2000

insert into #brojAutomobilaPoCeni
select '2000 do 5000', COUNT(cena) from dbo.CarAds where cena >=2000 and cena<5000

insert into #brojAutomobilaPoCeni
select '5000 do 10000', COUNT(cena) from dbo.CarAds where cena >=5000 and cena<10000

insert into #brojAutomobilaPoCeni
select '10000 do 15000', COUNT(cena) from dbo.CarAds where cena >=10000 and cena<15000

insert into #brojAutomobilaPoCeni
select '15000 do 20000', COUNT(cena) from dbo.CarAds where cena >=15000 and cena<20000

insert into #brojAutomobilaPoCeni
select '20000 do 25000', COUNT(cena) from dbo.CarAds where cena >=20000 and cena<25000

insert into #brojAutomobilaPoCeni
select '25000 do 30000', COUNT(cena) from dbo.CarAds where cena >=25000 and cena<30000

insert into #brojAutomobilaPoCeni
select 'preko 30000', COUNT(cena) from dbo.CarAds where cena >=30000

select * from #brojAutomobilaPoCeni

----------------------------------------------------------------------------------------------------------

drop table #cenaUOdnosuNaModel

CREATE TABLE #cenaUOdnosuNaModel
(
	model VARCHAR(50),
	prosecnaCena int,
)

insert into #cenaUOdnosuNaModel
select model, AVG(cena) from dbo.CarAds group by model

select * from #cenaUOdnosuNaModel order by prosecnaCena desc

select AVG(cena) as 'prosečna cena automobila' from dbo.CarAds

----------------------------------------------------------------------------------------------------------
drop table #cenaUOdnosuNaMarku

CREATE TABLE #cenaUOdnosuNaMarku
(
	marka VARCHAR(50),
	prosecnaCena int,
)

insert into #cenaUOdnosuNaMarku
select marka, AVG(cena) from dbo.CarAds group by marka

select * from #cenaUOdnosuNaMarku