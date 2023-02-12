-- Query 1
select astrologer_level, sum(astrologer_chats_count) as count
from (select astrologer_id, count(*) as astrologer_chats_count from chats group by astrologer_id)
join (select astrologer_id, astrologer_level from astrologers) using (astrologer_id)
group by astrologer_level

-- Query 2

select astrologer_name, max_rating_count, users_count, max_session_duration
from (select astrologer_id, sum(is_max_rating) as max_rating_count, count(distinct user_id) as users_count, max(session_duration) as max_session_duration 
	 from chats 
	 join (select chat_id, (case when rating = 5 then 1 else 0 end) as is_max_rating from ratings) using (chat_id) 
	 group by astrologer_id)
join (select astrologer_id, astrologer_name from astrologers) using (astrologer_id)

-- Query 3
select astrologer_name, avg_astrologer_rating, (money_acumulated / sum(money_acumulated)) as money_share
from (select astrologer_id, astrologer_name, avg(rating) as avg_astrologer_rating, sum(price * session_duration) as money_acumulated
	 from chats 
	 join ratings using (chat_id)
	 join astrologers using (astrologer_id)
	 join chat_pricing using (astrologer_level)
	 group by astrologer_id)
order by money_share desc
limit 5