select a_end.machine_id,
round(avg(a_end.timestamp-a_start.timestamp)::numeric,3) as processing_time
from activity a_start
join activity a_end
on a_start.machine_id=a_end.machine_id
and a_start.process_id=a_end.process_id
and a_start.activity_type='start'
and a_end.activity_type='end'
group by a_end.machine_id