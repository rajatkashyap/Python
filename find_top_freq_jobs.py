# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:01:34 2018

@author: U40MV02
"""
Hiring_jobs={'0': ['data scientist', 'IBM'], '1': ['data scientist', 'coca cola'], '2': ['data analyst', 'cnn'], '3': ['data scientist', 'google'], '4': ['business analyst', 'chase'], '5': ['data scientist', 'apple'], '6': ['scientist', 'biogen'], '7': ['scientist', 'broad institute'], '8': ['postdoc', 'mit'], '9': ['data engineer', 'microsoft']}
People={'0': {'0': {'title': 'data scientist', 'company': 'apple', 'status': 'apply'}, '1': {'title': 'data analyst', 'company': 'google', 'status': 'apply'}, '2': {'title': 'postdoc', 'company': 'georgia tech', 'status': 'current'}, '3': {'title': 'research assistant', 'company': 'georgia tech', 'status': 'previous'}}, '1': {'0': {'title': 'data scientist', 'company': 'google', 'status': 'apply'}, '1': {'title': 'data engineer', 'company': 'amazon', 'status': 'apply'}, '2': {'title': 'data scientist', 'company': 'facebook', 'status': 'apply'}, '3': {'title': 'data scientist', 'company': 'microsoft', 'status': 'apply'}, '4': {'title': 'data analyst', 'company': 'chase', 'status': 'previous'}}, '2': {'0': {'title': 'data scientist', 'company': 'apple', 'status': 'previous'}, '1': {'title': 'data analyst', 'company': 'google', 'status': 'previous'}, '2': {'title': 'postdoc', 'company': 'georgia tech', 'status': 'current'}, '3': {'title': 'research assistant', 'company': 'georgia tech', 'status': 'previous'}, '4': {'title': 'teaching assistant', 'company': 'georgia tech', 'status': 'previous'}}, '3': {'0': {'title': 'scientist', 'company': 'sentien biotechnologies', 'status': 'apply'}, '1': {'title': 'scientist', 'company': 'black diamond networks', 'status': 'apply'}, '2': {'title': 'scientist', 'company': 'surface oncology', 'status': 'apply'}, '3': {'title': 'scientist', 'company': 'akebia therapeutics', 'status': 'apply'}, '4': {'title': 'scientist', 'company': 'lifemine therapeutics', 'status': 'apply'}}, '4': {'0': {'title': 'scientist', 'company': 'dana-Farber cancer institute', 'status': 'apply'}, '1': {'title': 'scientist', 'company': 'agenus', 'status': 'apply'}, '2': {'title': 'bioinformatician', 'company': 'mitra biotech', 'status': 'apply'}, '3': {'title': 'data scientist', 'company': 'boston VA research institute', 'status': 'apply'}, '4': {'title': 'scientist', 'company': 'daley and associates', 'status': 'apply'}}}
def find_top_freq_jobs(Hiring_jobs, job_title):
    assert type(Hiring_jobs) is dict and len(Hiring_jobs) != 0
    d={}
    #print (Hiring_jobs)
    for i in Hiring_jobs:
        if job_title in Hiring_jobs[i]:
            d[i]=(job_title,Hiring_jobs[i][1])
    #print (len(d))
    return (d)

def rank_job(job_freq):
    assert type(job_freq) is dict or type(job_freq) is defaultdict
    if len(job_freq)==0:
        return []
    #return (sorted(job_freq,key=job_freq.get,reverse=True))
    #print (sorted(job_freq.items(), key=lambda x: (x[1],x[0])))
    #print (sorted(d.iteritems(), key=lambda (k,v):(-v, k)))
    #return ([v[0] for v in sorted(job_freq.items(), key=lambda x: (-x[1],x[0]))])
    return ([v[0] for v in sorted(job_freq.items(), key=lambda x: (-x[1],x[0]))])

    #return ([v[0] for v in sorted(job_freq.iteritems(), key=lambda k, v: (-v, k))])

def find_job_freq(applications):
    type(applications) is list
    d={}
    for i in applications:
        if i[0] in d:
            d[i[0]]=d[i[0]]+1
        else:
            d[i[0]]=1
    return d

def find_applications(People, pid):
    assert type(People) is dict and len(People) != 0
    assert type(pid) is str
    l=[]
    for i in People[pid]:
        if People[pid][i]['status']=='apply':
            l.append((People[pid][i]['title'],People[pid][i]['company']))
    return (l)

pid = '1'
applied_jobs = find_applications(People, pid)
print applied_jobs
job_freq = find_job_freq(applied_jobs)
print ('*')
print job_freq
rank = rank_job(job_freq)
print ('*')
print rank

top_freq_jobs = find_top_freq_jobs(Hiring_jobs, rank[0] if rank else '')
print ('*')
print top_freq_jobs
assert type(top_freq_jobs) is dict, "top_freq_jobs should be a dictionary." 
assert len(top_freq_jobs) == 1,len(top_freq_jobs)
assert '2' in top_freq_jobs and top_freq_jobs['2'] == ('data analyst', 'cnn')
#print_top_freq_jobs(rank, top_freq_jobs, pid)