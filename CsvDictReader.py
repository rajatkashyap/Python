import csv
with open("movies.csv") as m:
	m_list=list(csv.DictReader(m))

print sum(int(m['movie_id']) for m in m_list)