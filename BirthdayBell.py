from datetime import date, timedelta 

week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_birthdays_per_week(users):

    cur_date = date.today()   
    delta = timedelta(days=1)
    wb = {}

    def select_users(day, month):
        ul = []
        for u in users:
            ud = u["birthday"]
            if ((ud.month == month) and (ud.day == day)):
                ul.append(u["name"])
        return ul

    def create_wlist():
        wl = []
        for cd in range(7):
            d = cur_date + delta * cd
            wl.extend(select_users(d.day, d.month))

            print(f"weekday:{d.weekday()} -> {week_list[d.weekday()]}")

            if d.weekday() < 5:
                if len(wl) > 0:
                    wb[week_list[d.weekday()]] = wl[:]
                wl.clear()
                
    if len(users) > 0:
        create_wlist()
    return wb
