from ics import Calendar
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# returns true, if the time is in Prague DST
def is_dst_in_prague(dt: datetime) -> bool:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=ZoneInfo("Europe/Prague"))
    else:
        dt = dt.astimezone(ZoneInfo("Europe/Prague"))

    return bool(dt.dst())

# load file
with open("input.ics", "r", encoding="utf-8") as f:
    calendar = Calendar(f.read())

start_date = datetime(2025, 1, 1, tzinfo=timezone.utc)

# filter dates
filtered_events = [
    event for event in calendar.events if event.begin.datetime >= start_date
]

# sort
sorted_events = sorted(filtered_events, key=lambda e: e.begin.datetime)

events = 0

sda_time = datetime(2007, 1, 1, tzinfo=timezone.utc).timestamp() - 60*60

for event in sorted_events:
    descr = ""
    loc = ""
    if event.description:
      descr = event.description.replace('\n', '#')
      
    if event.location:
      loc = '#' + event.location
    
    td = sda_time
    
    if is_dst_in_prague(event.begin):
      td -= 60*60
      
    # Print  
    print(event.name + "|" + descr + loc + "|" + str(int(event.begin.timestamp() - td)) + "|" + str(int(event.end.timestamp() - td)) + "|1|" + event.uid[:16])
    events += 1;

