from datetime import datetime, timedelta


user_list = [[], [], [], [], []]
week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
week_check = []

def get_birthdays_per_week(users):
    cur_date = datetime.now()
    delta = timedelta(days=1)
    i = 0
    while i < 7:
        newdate = cur_date + delta*i
        newweek = newdate.weekday()
        if (newweek == 5) or (newweek == 6):
            newweek = 0
        week_check.append((newdate.day, newdate.month, newweek))
        i +=1

    for u in users:
        for w in week_check:
            if (u["birthday"].day == w[0]) and (u["birthday"].month == w[1]):       
                user_list[w[2]].append(u["name"])   
                break  

    i = 0 
    ii = week_check[0][2]
    while i < 5:
        tmp = week_list[ii] + ':'
        if len(user_list[ii]) > 0:
            for n in user_list[ii]:
                tmp += (' ' if tmp[-1] == ':' else ', ') + n
        i +=1
        ii +=1
        if ii > 4:
            ii = 0 
        if tmp[-1] != ':':
            print(tmp)
