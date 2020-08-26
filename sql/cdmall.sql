
-- 가수생성 
insert into artist values(null, '아이유');

-- 장르 생성
insert into genre values(null, 'common','CM');

-- 배급사 생성
insert into company values(null, '로엔', null);

-- 앨범 생성
insert into album values(null, 'Last Fantasy', 1);

-- 노래
insert into song values(null, '비밀', null, 1, 1);

-- 노래 장르
insert into song_genre values(1, 1);

-- 비밀(Last Fantasy,common[CM])-아이유
select a.title, b.name, c.title, d.name, f.name, f.s_name
	from song a, artist b, album c, company d, song_genre e, genre f
    where a.artist_no = b.no
    and a.album_no = c.no
    and c.company_no = d.no
    and a.no = e.song_no
    and f.no = e.genre_no;
    