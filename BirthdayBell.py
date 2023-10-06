from datetime import datetime, timedelta

week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_birthdays_per_week(users):
    cur_date = datetime.today()   
    delta = timedelta(days=1)
  
    def select_users(day, month):
        ul = []
        for u in users:
            ud = u["birthday"]
            if ((ud.month == month) and (ud.day == day)):
                ul.append(u)
        return ul

    def print_wl(wl, wd):
        if len(wl) > 0:
            print(week_list[wd]+": "+', '.join(p["name"] for p in wl))

    def create_wlist():
        wl = []
        for cd in range(7):
            d = cur_date + delta * cd
            wl.extend(select_users(d.day, d.month))
            if d.weekday() < 5:
                print_wl(wl, d.weekday())
                wl.clear()
    create_wlist()
